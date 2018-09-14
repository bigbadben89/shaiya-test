#!/bin/sh

# define iptables command
IPTABLES=/sbin/iptables

# define host
HOST=nat

# define interface
WAN=ppp0

# define external IP
EXTERNAL_IP=YOUR_EXTERNAL

# define ports
INCOMING_PORT_ARR=(80, 3389, 30800, 30810)

# Clear all the rules
$IPTABLES -F
$IPTABLES -X
$IPTABLES -Z
$IPTABLES -t $HOST -F
$IPTABLES -t $HOST -X
$IPTABLES -t $HOST -Z
$IPTABLES -t mangle -F
$IPTABLES -t mangle -X
$IPTABLES -t mangle -Z

### 
$IPTABLES -P INPUT DROP
$IPTABLES -P OUTPUT ACCEPT
$IPTABLES -P FORWARD ACCEPT

## Allow loopback OUTPUT 
$IPTABLES -A OUTPUT -o lo -j ACCEPT
$IPTABLES -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPTABLES -A INPUT -i lo -j ACCEPT

# Accept connection
$IPTABLES -A INPUT -i $WAN -m state --state ESTABLISHED,RELATED -j ACCEPT

# DROPspoofing packets
$IPTABLES -A INPUT -s 10.0.0.0/8 -j DROP 
$IPTABLES -A INPUT -s 169.254.0.0/16 -j DROP
$IPTABLES -A INPUT -s 172.16.0.0/12 -j DROP
$IPTABLES -A INPUT -s 127.0.0.0/8 -j DROP
$IPTABLES -A INPUT -s 192.168.0.0/24 -j DROP
$IPTABLES -A INPUT -s 224.0.0.0/4 -j DROP
$IPTABLES -A INPUT -d 224.0.0.0/4 -j DROP
$IPTABLES -A INPUT -s 240.0.0.0/5 -j DROP
$IPTABLES -A INPUT -d 240.0.0.0/5 -j DROP
$IPTABLES -A INPUT -s 0.0.0.0/8 -j DROP
$IPTABLES -A INPUT -d 0.0.0.0/8 -j DROP
$IPTABLES -A INPUT -d 239.255.255.0/24 -j DROP
$IPTABLES -A INPUT -d 255.255.255.255 -j DROP

#for SMURF attack protection
$IPTABLES -A INPUT -p icmp -m icmp --icmp-type address-mask-request -j DROP
$IPTABLES -A INPUT -p icmp -m icmp --icmp-type timestamp-request -j DROP
$IPTABLES -A INPUT -p icmp -m icmp -m limit --limit 1/second -j ACCEPT

# Droping all invalid packets
$IPTABLES -A INPUT -m state --state INVALID -j DROP
$IPTABLES -A FORWARD -m state --state INVALID -j DROP
$IPTABLES -A OUTPUT -m state --state INVALID -j DROP

# flooding of RST packets, smurf attack Rejection
$IPTABLES -A INPUT -p tcp -m tcp --tcp-flags RST RST -m limit --limit 2/second --limit-burst 2 -j ACCEPT

# Allow ping means ICMP port is open (If you do not want ping replace ACCEPT with REJECT)
$IPTABLES -A INPUT -p icmp -m icmp --icmp-type 8 -j REJECT

# SYN-Flooding Protection
$IPTABLES -N syn-flood
$IPTABLES -A INPUT -i $WAN -p tcp --syn -j syn-flood
$IPTABLES -A syn-flood -m limit --limit 1/s --limit-burst 4
$IPTABLES -A syn-flood -j DROP

$IPTABLES -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP 
$IPTABLES -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP 
$IPTABLES -A INPUT -p tcp --tcp-flags FIN,RST FIN,RST -j DROP 
$IPTABLES -A INPUT -p tcp --tcp-flags ACK,FIN FIN -j DROP

# Make sure that new TCP connections are SYN packets
$IPTABLES -A INPUT -i $WAN -p tcp ! --syn -m state --state NEW -j DROP


INCOMING_PORT_ARR=(22 80)
for PORT in ${INCOMING_PORT_ARR[@]}; do
    echo "Applying log chain for incoming tcp/udp on port $PORT..."
    $IPTABLES -N PORT-$PORT-INCOMING-LOG
    $IPTABLES -A PORT-$PORT-INCOMING-LOG -j LOG --log-ip-options --log-prefix "# P$PORT-INCOMING: "
    $IPTABLES -A PORT-$PORT-INCOMING-LOG -j ACCEPT

    echo "Applying log chain for dropping tcp/udp brute force on port $PORT..."
    $IPTABLES -N PORT-$PORT-BRUTE-FORCE-LOG
    $IPTABLES -A PORT-$PORT-BRUTE-FORCE-LOG -j LOG --log-ip-options --log-prefix "*** P$PORT-BRUTE-FORCE: "
    $IPTABLES -A PORT-$PORT-BRUTE-FORCE-LOG -j DROP

    $IPTABLES -A INPUT -i $INTERFACE -p tcp -m tcp --dport $PORT -m state --state NEW -m recent --set --name TCP-PORT$PORT --rsource
    $IPTABLES -A INPUT -i $INTERFACE -p tcp -m tcp --dport $PORT -m recent --rcheck --seconds 5 --hitcount 3 --rttl --name TCP-PORT$PORT --rsource -j PORT-$PORT-BRUTE-FORCE-LOG
    $IPTABLES -A INPUT -i $INTERFACE -p tcp -m tcp --dport $PORT -j PORT-$PORT-INCOMING-LOG

    $IPTABLES -A INPUT -i $INTERFACE -p udp -m udp --dport $PORT -m state --state NEW -m recent --set --name UDP-PORT$PORT --rsource
    $IPTABLES -A INPUT -i $INTERFACE -p udp -m udp --dport $PORT -m recent --rcheck --seconds 5 --hitcount 3 --rttl --name UDP-PORT$PORT --rsource -j PORT-$PORT-BRUTE-FORCE-LOG
    $IPTABLES -A INPUT -i $INTERFACE -p udp -m udp --dport $PORT -j PORT-$PORT-INCOMING-LOG
done

# NAT Reflection (For LAN go to external IP)
#echo "NAT Reflection"
#$IPTABLES -t $HOST -A PREROUTING -d $EXTERNAL_IP/32 -p tcp -m multiport --dports 54321,30800,30810,9876,21 -j DNAT --to-destination 192.168.10.5
#$IPTABLES -t $HOST -A POSTROUTING -s 192.168.10.0/24 -d 192.168.10.5/24 -p tcp -m multiport --dports 54321,30800,30810,  9876,21 -j MASQUERADE

# Port forwarding
#$IPTABLES -t nat -A PREROUTING -i $WAN -p tcp -m multiport --dport 50000:50015 -j DNAT --to 192.168.10.5

# Block ip then log
#$IPTABLES -N BLOCKED-IP
#$IPTABLES -A BLOCKED-IP -j LOG --log-prefix "BLOCKED: "
#$IPTABLES -A BLOCKED-IP -j DROP
#$IPTABLES -A INPUT -s 203.76.172.134 -j BLOCKED-IP

# Trusted ip
#$IPTABLES -A INPUT -p tcp -s YOUR_IP_ADDRESS -j ACCEPT
# Allow ip to connect port 22
#$IPTABLES -A INPUT -p tcp -s YOUR_IP_ADDRESS -m tcp --dport 22 -j ACCEPT

# Block MAC
# $IPTABLES -A INPUT -m mac --mac-source 00:0F:EA:91:04:08 -j DROP

# Log all dropped 
$IPTABLES -N DROPPED-LOG
$IPTABLES -A DROPPED-LOG -j LOG --log-prefix "* DEFAULT-DROPPED: "
$IPTABLES -A DROPPED-LOG -j DROP
$IPTABLES -A INPUT -j DROPPED-LOG


$SERVICE iptables save # save rules to /etc/sysconfig/iptables
$SERVICE iptables reload # reload rules 
$SERVICE iptables restart 
$IPTABLES-save > rules # save rules to file named "rules"

### NOTE
# DROP - Prohibit a packet from passing. Send no response.
# REJECT - Prohibit a packet from passing. Send an ICMP destination-unreachable back to the source host

