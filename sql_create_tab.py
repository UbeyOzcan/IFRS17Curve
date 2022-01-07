import pyodbc
# server = 'localhost\SQLEXPRESS'
# databaseName = 'master'
# sql.append("CREATE TABLE %s" % table + " ( %s" % col1 + " float, %s" % col2 + " float)")
# '{SQL Server Native Client 11.0}'

def SQL_create_table(srv, db,country, year, month):
    
     cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{ODBC Driver 13 for SQL Server}',server = srv , database = db)
     cursor = cnxn.cursor()
     sql = list()
     
     table = "IFRS17curve_" + country[0:3] + "_" + year + "_" + month
     
     sql.append("CREATE TABLE %s" % table + "(eiopa float, IFRS17curve float)")
     cursor.execute(str(sql[0]))
     cnxn.commit()
     cursor.close()
     cnxn.close()

