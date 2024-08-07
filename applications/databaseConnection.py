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

    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding="UTF-8")
        cursor = connection.cursor()
        cursor.execute(sql_query)

        columns = [col[0] for col in cursor.description]
        results = []

        for row in cursor.fetchall():
            processed_row = {}
            for col_name, col_value in zip(columns, row):
                if isinstance(col_value, cx_Oracle.LOB):
                    processed_row[col_name] = col_value.read()  # Read LOB content
                else:
                    processed_row[col_name] = col_value
            results.append(processed_row)

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


#method to execute a stored Procedure
# params: procedure_name = "Name of stored Procedure", params = [x, ...] Array of Values
def execute_procedure_list_of_dicts(procedure_name: str, params):
    connection = None
    cursor = None
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding="UTF-8")
        cursor = connection.cursor()

        out = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc(procedure_name, [params, out])

        # Ergebnisse abrufen
        result_cursor = out.getvalue()
        
        # Spaltennamen aus cursor.description extrahieren
        columns = [col[0] for col in result_cursor.description]

        # Daten abrufen und in eine Liste von Dictionaries schreiben
        result = []
        for row in result_cursor:
            processed_row = {}
            for col_name, col_value in zip(columns, row):
                if isinstance(col_value, cx_Oracle.LOB):
                    processed_row[col_name] = col_value.read()  # Read LOB content
                else:
                    processed_row[col_name] = col_value
            row_dict = dict(processed_row)
            result.append(row_dict)

        return result
    
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
#sql_query = "SELECT * FROM SNACK"
#print(execute_sql_query(sql_query))

#example of stored Procedure
#procedure = "VERKAUFEN_MERCH"
#params = [1,4]
#execute_procedure(procedure, params)
