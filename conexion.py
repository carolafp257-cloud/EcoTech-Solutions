import oracledb

USUARIO = "CARITO"
PASSWORD = "carito"
HOST = "192.168.56.1"
PUERTO = 1521
SID = "xe"

try:
    # Creamos el DSN exacto para SID
    dsn = oracledb.makedsn(HOST, PUERTO, sid=SID)

    conexion = oracledb.connect(
        user=USUARIO,
        password=PASSWORD,
        dsn=dsn
    )

    print("¡Conexión exitosa a Oracle Database!")

    with conexion.cursor() as cursor:
        cursor.execute("SELECT sysdate FROM dual")
        fecha = cursor.fetchone()
        print("Fecha actual en la BD:", fecha[0])

except oracledb.DatabaseError as e:
    error, = e.args
    print(f"Error Oracle: {error.code} - {error.message}")

finally:
    if "conexion" in locals():
        conexion.close()