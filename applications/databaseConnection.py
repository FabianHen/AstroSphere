#python: pip install cx_Oracle
#Desktopentwicklung für C++ könnte notwendig sein
#Oracle Client muss heruntergeladen und in die Systemvariablen eingetragen sein: https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html


import cx_Oracle
from basicDatabaseStatements import*

#global variables for the database connection
dsn = cx_Oracle.makedsn("rs03-db-inf-min.ad.fh-bielefeld.de", 1521, sid="orcl")
user = "AstroSphere"
password = "astrosphere"


def execute_sql_query_list_of_dicts(sql_query: str) -> list:
    global dsn, user, password

    connection = None
    cursor = None

    #print("User: ", user, "; Password: ", password, "; DSN: ", dsn)
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding="UTF-8")
        cursor = connection.cursor()

        cursor.execute(sql_query)
        
       # Spaltennamen aus cursor.description extrahieren
        columns = [col[0] for col in cursor.description]

        # Daten als Liste von Dictionaries speichern
        result = []
        for row in cursor:
            result.append(dict(zip(columns, row)))

        return result
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Datenbankfehler:", error.message)
    except Exception as e:
        print("Allgemeiner Fehler:", str(e))
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def execute_sql_query(sql_query):
    global dsn, user, password

    connection = None
    cursor = None

    #print("User: ", user, "; Password: ", password, "; DSN: ", dsn)
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding="UTF-8")
        cursor = connection.cursor()

        cursor.execute(sql_query)
        
        results = cursor.fetchall()

        for row in results:
            processedRow=[]
            for col in row:
                if isinstance(col, cx_Oracle.LOB):
                    processedRow.append(col.read())
                else:
                    processedRow.append(col)
            #print(processedRow)
        
        return results
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Datenbankfehler:", error.message)
    except Exception as e:
        print("Allgemeiner Fehler:", str(e))
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


#method to execute a stored Procedure
# params: procedure_name = "Name of stored Procedure", params = [x, ...] Array of Values
def execute_procedure(procedure_name, params):
    connection = None
    cursor = None
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding="UTF-8")
        cursor = connection.cursor()

        cursor.callproc(procedure_name, params)
        
        return True
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Datenbankfehler:", error.message)
        return False
    except Exception as e:
        print("Allgemeiner Fehler:", str(e))
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



#check if cx_Oracle works
#print(cx_Oracle.clientversion())


#example of sql Query
sql_query = "SELECT * FROM BESTAENDE_MERCH"
print(execute_sql_query(sql_query))

#example of stored Procedure
#procedure = "VERKAUFEN_MERCH"
#params = [1,4]
#execute_procedure(procedure, params)