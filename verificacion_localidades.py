import csv
import os # Importar el módulo os para trabajar con archivos y directorios

# Función para leer las localidades desde los archivos CSV en la carpeta "provincias"
def leer_localidades():
    localidades_provincia = {}
    carpeta_provincias = 'provincias'
    archivos_csv = [archivo for archivo in os.listdir(carpeta_provincias) if archivo.endswith('.csv')]
    for archivo in archivos_csv:
        provincia = archivo.split('.')[0]
        localidades = []

#se abre el archivo CSV en modo lectura y se lee con el método csv.reader() para obtener un objeto lector
        with open(os.path.join(carpeta_provincias, archivo), 'r', newline='', encoding='utf-8') as csvfile: 
            reader = csv.reader(csvfile)
            for row in reader:
#se recorre el objeto lector con un bucle for y se añade la localidad a la lista localidades
                localidades.append(row[2])  # La localidad está en la tercera columna
        localidades_provincia[provincia] = localidades
    return localidades_provincia

# Leer las localidades de la carpeta "provincias"
carpeta_provincias = leer_localidades()

# Comparar las localidades del archivo con las localidades en los archivos CSV de la carpeta
faltan = False
for provincia, localidades_csv in carpeta_provincias.items():
    if provincia not in carpeta_provincias: 
        print(f"Faltan datos para la provincia {provincia}.")
        faltan = True
    else:
        localidades_archivo = carpeta_provincias[provincia]  
        if set(localidades_csv) != set(localidades_archivo):
            print(f"Las localidades para la provincia {provincia} no coinciden con el archivo en la carpeta.")
            faltan = True

if not faltan:
    print("Todos los datos están correctos. Las localidades en los archivos de la carpeta coinciden con las del archivo localidades.csv")
