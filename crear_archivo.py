import csv
import MySQLdb as mysql

# Conexión a la base de datos
try:
    db = mysql.connect("localhost", "root", "", "localidades")
    cursor = db.cursor()

# Eliminar tabla si existe
    cursor.execute("DROP TABLE IF EXISTS localidades")
    db.commit()
    print("Tabla eliminada correctamente.")

# Crear tabla localidades si no existe
    crear = """
    CREATE TABLE IF NOT EXISTS localidades (
        provincia VARCHAR(255),
        id INT,
        localidad VARCHAR(255),
        cp INT(255),
        id_prov_mstr INT(255)
    )
    """
    cursor.execute(crear)

# Manejo de errores
except mysql.Error as e:
    print("Error al conectar a la base de datos o al crear la tabla:", e)
    exit(1)


# Importar datos desde el archivo CSV a la base de datos
try:
    with open('localidades.csv', 
              'r', 
              newline='', 
              encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        datos = list(reader)

    # Insertar datos en la base de datos
    insertar = """
    INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr)
    VALUES (%s, %s, %s, %s, %s)
    """

    # Ejecutar la consulta
    cursor.executemany(insertar, datos)
    db.commit()
    print("Datos importados correctamente a la base de datos.")

# Manejo de errores
except mysql.Error as e:
    db.rollback()
    print("Error al importar datos:", e)

# Crea un archivo CSV por cada provincia
try:
    cursor.execute("SELECT DISTINCT provincia FROM localidades;")
    provincias = cursor.fetchall()
    for provincia in provincias:
        cursor.execute("SELECT * FROM localidades WHERE provincia = %s", (provincia[0],))

        localidades = cursor.fetchall()
        with open(f"provincias/{provincia[0]}.csv",
                  "w",
                  newline='',
                  encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(localidades)
    print("Archivos CSV por provincia creados correctamente.")
except mysql.Error as e:
    print("Error al crear archivos CSV por provincia:", e)

# Cerrar conexión
db.close()

    #(provincia[0]) sirve para acceder al primer elemento de la tupla provincia
    #writer.writerows(localidades) escribe todas las filas de la lista localidades en el archivo CSV
    #rollback() deshace todas las operaciones pendientes en la base de datos
    #cursor.execute() sirve para ejecutar consultas en la base de datos
    # fetchall() obtiene todas las filas de un cursor como una lista de tuplas