from os import getenv
#import pymssql

server = getenv("PYMSSQL_TEST_SERVER")
user = getenv("PYMSSQL_TEST_USERNAME")
password = getenv("PYMSSQL_TEST_PASSWORD")

print server
dbFile = "../config/db.txt"

def parseConfig():
    sql = {}
    with open(dbFile) as f:
        for line in f.readlines():
            l = line.strip().split("=")
            sql[l[0]] = l[1]
    return sql 

def main():
    sql = parseConfig()
    print sql
    
if __name__== "__main__":
    main()    
