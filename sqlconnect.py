import pyodbc


# Insert Dataframe into SQL Server:
#cursor.execute('''
#		CREATE TABLE Rates (
#			Belgium float,
#			IFRS17_Be float
#			)
#               ''')


# for index, row in df.iterrows():
#      cursor.execute('''
#                INSERT INTO dbo.Rates ([Belgium], [IFRS17_Be]) values (?,?)''',
#                row['Belgium'],
#                row['IFRS17_Be'])
# 
# '{ODBC Driver 17 for SQL Server}'

def SQL_upload(srv, db, country, df, year, month):
    
     

    cnxn = pyodbc.connect(Trusted_Connection='yes', driver = "{SQL Server Native Client 11.0}", server = srv , database = db)
    cursor = cnxn.cursor()
    sql = list()
    
    table = "IFRS17curve_" + country[0:3] + "_" + year + "_" + month
    
    sql.append("INSERT INTO dbo.%s" % table + " ([eiopa], [IFRS17curve]) values (?,?)")
     
    for index, row in df.iterrows():
          cursor.execute(str(sql[0]),
                    row["eiopa"],
                    row["IFRS17curve"])

    cnxn.commit()
    cursor.close()
    cnxn.close()


