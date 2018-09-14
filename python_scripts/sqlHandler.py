import utils 
import sys
import subprocess
import os

dbFile = "../config/db.conf"
dbBackUpPath = "C:\\DATABASE_BACKUP\\"

sqlCommon = "sqlcmd -U %s -P %s -S %s"
sqlBackUpQuery = "BACKUP DATABASE %s TO DISK = \"%s\" GO"
sqlExecuteFile = ""
sqlExecuteQuery = ""

def loadDbConfig(dbFile):
    isFileExisted = utils.checkIfFileExisted(dbFile)
    if not isFileExisted:
        sys.exit()
        return

    sql = {}
    with open(dbFile) as f:
        for line in f.readlines():
            l = line.strip().split("=")
            sql[l[0]] = l[1]
    return sql 

def executeSqlFile(sqlFile):
    if not utils.checkIfFileExisted(sqlFile):
        utils.show("Failed to execute %s" % sqlFile)
        return
    executeCmd(sqlExecuteFile % sqlFile)   

def executeSqlQuery(query):
    utils.show("Executing %s" % query)
    executeCmd(query)

def executeCmd(cmd):
    subprocess.call(cmd, shell=False)    

if __name__== "__main__":
    operation = sys.argv[1]
    if not operation:
        utils.show("No operation has been given!!!")
        sys.exit()

    sqlConf = loadDbConfig(dbFile)

    if sqlConf:
        sqlCommon = sqlCommon % (sqlConf["db.user"], sqlConf["db.pass"], sqlConf["db.host"])
        sqlExecuteFile = sqlCommon + " -i %s"
        sqlExecuteQuery = sqlCommon + " -Q %s"

    if operation == "execute":
        executeSqlFile(sys.argv[2])
    elif operation == "backup":
        currentTime = utils.getCurrentTime()
        newDbBackUpPath = dbBackUpPath + currentTime     
        utils.show("Creating  %s" % newDbBackUpPath)
        os.mkdir(newDbBackUpPath)
    
        backUpQuery = sqlExecuteQuery % sqlBackUpQuery
        executeSqlQuery(backUpQuery % ("PS_Billing", (newDbBackUpPath + "\\PS_Billing_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_ChatLog", (newDbBackUpPath + "\\PS_ChatLog_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GameData", (newDbBackUpPath + "\\PS_GameData_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GameDefs", (newDbBackUpPath + "\\PS_GameDefs_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GameLog", (newDbBackUpPath + "\\PS_GameLog_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GMTool", (newDbBackUpPath + "\\PS_GMTool_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_Statics", (newDbBackUpPath + "\\PS_Statics_" + currentTime)))
        executeSqlQuery(backUpQuery % ("PS_UserData", (newDbBackUpPath + "\\PS_UserData_" + currentTime)))
    else:
        utils.show("Operation failed! We do not have %s operation" % operation)
