import csv
import os

# Conteo total de localidades desde el archivo localidades.csv
conteo_total_localidades = 0
with open('localidades.csv', 'r') as file:
    next(file)
    for line in file:
        conteo_total_localidades += 1

# Conteo total de localidades desde archivos CSV en la carpeta 'provincias'
carpeta = 'provincias/'
conteo_total_provincias = 0
archivos_csv = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.csv')]
for archivo in archivos_csv:
    with open(os.path.join(carpeta, archivo), 'r') as file:
        conteo_total_provincias += sum(1 for line in file)

# Imprimimos los resultados
print(f"Total de localidades en localidades.csv: {conteo_total_localidades}")
print(f"Total de localidades en archivos de la carpeta provincias: {conteo_total_provincias}")




