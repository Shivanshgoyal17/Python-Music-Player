import cx_Oracle
import traceback
conn=None
try:
    dsn_tns=cx_Oracle.makedsn("localhost","1521",service_name="xe")
    conn=cx_Oracle.connect(user="system",password="oracle",dsn=dsn_tns)
    print("Connected Successfully to the DB")
    print("DataBase version:",conn.version)
    print("DB User:",conn.username)
except cx_Oracle.DatabaseError:
    print("DB Error")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Disconnected Successfully from the DB")