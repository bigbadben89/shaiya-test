import utils 

dbFile = "../config/db.txt"

def parseConfig():
    utils.show("Parsing database config: " + dbFile)
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
