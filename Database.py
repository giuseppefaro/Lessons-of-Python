import sqlite3
## Variable
connection = sqlite3.connect("database/company.db")

def FileR():
    #global sql_imp
    print('almost ready to check the file')
    doc_r = open("database/database.sql", "r")
    sql_imp = doc_r.read()
    doc_r.close()
    return sql_imp

#open the TB
cursor = connection.cursor()

# all SQL commands (split on ';')
sqlCommands = FileR().split(';')
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    cursor.execute(FileR())


#write
cursor.execute(FileR())
#save
connection.commit()
#close connection
connection.close()