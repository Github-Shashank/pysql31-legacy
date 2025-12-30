import os,csv,json,webbrowser
from tabulate import tabulate

"""
pysql31.py
Created before 2025
Filesystem-based database engine
Uses folders as databases and tables
Uploaded for archival purposes
"""

# Code use at end of comment algorithm code work error 

yourPath = r"E:/pysql"#r"C:/pysql3.1"
default = {"path":yourPath}
data = {"database":""}

# Creats your folder to save data 1110
if not os.path.exists(default["path"]):
    try:
        drive, _ = os.path.splitdrive(yourPath)
        if drive == yourPath:
            None
        else:
            os.mkdir(default["path"])
    except:
        print("Create folder manually something error while creating folder %s"%(yourPath))
        

# Shows available databases in C:/pysql3.1 1110
def showDatabases():
    l = os.listdir(default["path"])
    database = []
    for i in range(len(l)):
        if l[i][-3:] == "_db":
            database.append([l[i]])
    print(tabulate(database,["Databases"],"outline"))

# Creates new database folder in C:/pysql3.1 1110
def createDatabase(s):
    os.mkdir( "%s//%s_db"%(default["path"],s) )
    print( "Database %s has been created"%(s) )

def dropDatabase(s):
    os.rename("%s//%s_db"%(default["path"],s), "%s//%s_db_B"%(default["path"],s) )
    print( "Database %s has removed from database"%(s) )

def restoreDatabase(s):
    os.rename("%s//%s_db_B"%(default["path"],s), "%s//%s_db"%(default["path"],s) )
    print( "Database %s is restored"%(s) )

# Select database 1110
def useDatabase(s):
    l = os.listdir(default["path"])
    if s+"_db" in l:
        data["database"] = s
        print("You are using %s database"%(s))
    else:
        
        # Error Section
        
        print("%s database doesn't exist"%(s))
        showDatabases()
        print()
        #Error retreat
        e = input("Select database :- ")
        useDatabase(e)

# Show all tables in selected database 1110
def showTables():
    if os.path.exists("%s//%s_db"%(default["path"], data['database'] )):
        l = os.listdir("%s//%s_db"%(default["path"], data['database'] ))
        tables = []
        for i in range(len(l)):
            if l[i][-3:] == "_tb":
                tables.append([l[i]])
        print(tabulate(tables,["Tables"],"outline"))
    else:
        
        # Error Section
        
        print('Error! No database selected')
        showDatabases()
        e = input("Select database :- ")
        useDatabase(e)
        print()
        #Error retreat
        showTables()

# Creats new Table folder in selected database 1110
def createTable(s):
    if os.path.exists("%s//%s_db" % (default["path"], data["database"])):
        os.mkdir("%s//%s_db//%s_tb" % (default["path"], data["database"], s))
        print("%s table has been created" % s)
    else:
        
        # Error Section
        
        print('Error! No database selected')
        showDatabases()
        e = input("Select database :- ")
        useDatabase(e)
        print()
        #Error retreat
        createTable(s)

# Creates given table structure and table 1110
def createTableRows(t,r):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ) and type(r) == type([]):
        if not os.path.exists("%s//%s_db//%s_tb//table.txt" % (default["path"], data["database"], t )):
            d = {}
            for i in r:
                d[i] = {"type":"","condition":[],"null":""}
            file = open("%s//%s_db//%s_tb//structure.txt" % (default["path"], data["database"], t ) , 'w' )
            file.write(str(d))
            file.close()
            file = open("%s//%s_db//%s_tb//table.txt" % (default["path"], data["database"], t ) , 'w' )
            file.write(str([r]))
            file.close()
        else:
            print('Error! table already exists')
    else:
        
        # Error Section
        
        if type(r) == type([]) and os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! Row enter format')
            print()
            row = input("Enter rows in list form :- ")
            showTables()
            print()
            table = input("Enter your table :- ")
            #Errro retreat
            createTableRows(table, row)
        elif os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print("Error! Table %s doesn't exist"%(t))
            showTables()
            e = input("Select table :- ")
            # Error retreat
            createTableRows(e,r)
        else:
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            #Error retreat
            createTableRows(t,r)            
            

# Defines Structure of given table 1110
def defineTableStructure(t):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
        file = open("%s//%s_db//%s_tb//structure.txt" % (default["path"], data["database"], t ) , 'r' )
        d = eval(file.readline())
        rows = list(d.keys())
        file.close()
        print(d)
        new_d = input('Edit the structure of %s table :- '%(t))
        # Error Section 1
        if not type(eval(new_d)) == type({}):
            print("Error! Unreadable Data")
            print("Data format is not recognised")
            print()
            print("Renter your data")
            print()
            print("defineTableStructure(%s)"%(t))
            defineTableStructure(t)
        else:
            new_s = eval(new_d)
            print(new_s)
            print(new_d)
            error = 0
            if list(new_s.keys()) == rows:
                for i in rows:
                    if list(new_s[i].keys()) == ['type', 'condition', 'null']:
                        print(new_s[i])
                    else:
                        print(new_s[i],'Inappropriate Structure')
                        error = 1
                # Error Section 2
                if error == 1:
                    file = open("%s//%s_db//%s_tb//structure.txt" % (default["path"], data["database"], t ) , 'w' ) 
                    file.write(d)
                    file.close()
                    print("Error! Inappropriate structure")
                    print()
                    print("Renter your data")
                    print()
                    print("defineTableStructure(%s)"%(t))
                    defineTableStructure(t)
                else:
                    file = open("%s//%s_db//%s_tb//structure.txt" % (default["path"], data["database"], t ) , 'w' )
                    file.write(str(new_s))
                    file.close()
    else:

        # Error Section 4

        if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            print()
            #Error retreat
            defineTableStructure(t)
        else:
            print("Error! table doesn't exist")
            showTables()
            print()
            table = input("Enter your table :- ")
            # Error retreat
            defineTableStructure(table)


# Describe table properties
def describeTable(t):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
        file = open("%s//%s_db//%s_tb//structure.txt" % (default["path"], data["database"], t ) , 'r' )
        d = eval(file.readline())
        l = []
        for i in d:
            u =  []
            u.append(i)
            for j in d[i]:
                u.append(d[i][j])
            l.append(u)
        file.close()
        print('%s table structure :-'%t)
        print(tabulate(l,['Row','Type','Condition','Null'],"outline"))
        print()
    else:

        # Error Section

        if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            print()
            #Error retreat
            describeTable(t)
        else:
            print("Error! table doesn't exist")
            showTables()
            print()
            table = input("Enter your table :- ")
            # Error retreat
            describeTable(table)


# Insert data by appending table.txt 1111
def insertData(t,l):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ) and type(l) == type([]):

        # Reads structure of your table
        file = open("%s//%s_db//%s_tb//structure.txt" % (default["path"], data["database"], t ) , 'r' )
        strh = eval(file.readline())
        file.close()

        # Reads data of your table to append safely
        file = open("%s//%s_db//%s_tb//table.txt" % (default["path"], data["database"], t ) , 'r' )
        dat = eval(file.readline())
        length = len(dat)
        file.close()

        # Checks your given list to append data
        n = 0
        error = 0
        errorL = []
        newDat = []
        for i in strh:

            if type(l[n]) == eval(strh[i]['type']):
                error = 0
            else:
                error = 1
                if l[n] == '':
                    pass
                else:
                    print("Error! Type error")
                    print( '%s type is not %s' % (l[n],strh[i]['type'] ) )

            if strh[i]['null'] == 'not null' and l[n] == '':
                error = 1
                print('Error! not null')
            else:
                error = 0
            
            if len(strh[i]['condition']) != 0:

                if 'sno' in strh[i]['condition']:
                    l[n] = length
                
                column = []
                k = dat[0].index(i)
                for j in dat[1:]:
                    try:
                        column.append(j[k])
                    except:
                        None
                
                s2 = strh[i]['condition']
                if 'unique' in s2 or 'primary' in s2:
                    if l[n] in column:
                        error = 1
                        print('%s key error'%(s2))
                    else:
                        None
                
                cnd = ''
                dfalt = ''
                for cnd in s2:
                    if cnd[:7] == 'default':
                        dfalt = cnd
                        break
                    
                if len(dfalt) != 0:
                    if dfalt[:7] == 'default':
                        if dfalt.count('=') == 1:
                            if strh[i]['type'] == 'int':
                                l[n] = int(dfalt[dfalt.index('=')+1:])
                            elif strh[i]['type'] == 'float' :
                                l[n] = float(dfalt[dfalt.index('=')+1:])
                            else:
                                l[n] = dfalt[dfalt.index('=')+1:]
                            error = 0
                        else:
                            error = 1  
                            print('Error! Default key error')
                            
            errorL.append(error)
            if error == 0:
                newDat.append(l[n])
                print(l[n],'has been written down')
            else:
                print('Key error')
            
            n += 1

        # Check for any error else appends data to table
        if not 1 in errorL :
            dat.append(newDat)
            file = open("%s//%s_db//%s_tb//table.txt" % (default["path"], data["database"], t ) , 'w' )
            file.write(str(dat))
            file.close()

    else:
        
        # Error Section

        if not type(l) == type([]):
            print("Error! Unreadable data")
            print("InsertData(<table>,<list>)")
            describeTable(t)
            print()
            new_l = input("Renter your data in the for of list")
            insertData(t,new_l)
        elif not os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            print()
            #Error retreat
            insertData(t,l)
        else:
            print("Error! table doesn't exist")
            showTables()
            print()
            table = input("Enter your table :- ")
            # Error retreat
            insertData(table,l)

def showTable(t,l):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
        file = open("%s//%s_db//%s_tb//table.txt" % (default["path"], data["database"], t ) , 'r' )
        dat = eval(file.readline())
        file.close()
        print(tabulate(dat[1:],dat[0],"outline"))

    else:
        
        if not os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            print()
            #Error retreat
            insertData(t,l)
        else:
            print("Error! table doesn't exist")
            showTables()
            print()
            table = input("Enter your table :- ")
            # Error retreat
            insertData(table,l)
        

def openFolder(t):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
        webbrowser.open( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) )
    else:

        if not os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            print()
            #Error retreat
            openFolder(t)
        else:
            print("Error! table doesn't exist")
            showTables()
            print()
            table = input("Enter your table :- ")
            # Error retreat
            openFolder(t)


def update(t):
    if os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
        webbrowser.open( "%s//%s_db//%s_tb//table.txt" % (default["path"], data["database"], t ) )
    else:

        if not os.path.exists( "%s//%s_db//%s_tb" % (default["path"], data["database"], t ) ):
            print('Error! No database selected')
            showDatabases()
            e = input("Select database :- ")
            useDatabase(e)
            print()
            #Error retreat
            update(t)
        else:
            print("Error! table doesn't exist")
            showTables()
            print()
            table = input("Enter your table :- ")
            # Error retreat
            update(t)
