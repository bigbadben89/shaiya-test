import sys

def execute(scriptPath):
    with open(scriptPath, 'r') as inp:
        for line in inp:
            if line == 'GO\n':
                c.execute(sqlQuery)
                sqlQuery = ''
            elif 'PRINT' in line:
                disp = line.split("'")[1]
                print(disp, '\r')
            else:
                sqlQuery = sqlQuery + line
    inp.close()

def main():
    sqlFile = sys.argv[1];
    print 'Executing %s' % sqlFile
    execute(sqlFile);
    
if __name__== "__main__":
    main()    