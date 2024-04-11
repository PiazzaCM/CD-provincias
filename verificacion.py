import csv
import MySQLdb as mysql

conteo = {}

with open('localidades.csv', 'r') as file:
    next(file)
    for line in file:
        campos = line.strip().split(',')
        provincia = campos[0]
        if provincia in conteo:
            conteo[provincia] += 1
        else:
            conteo[provincia] = 1
for provincia, conteo in conteo.items():
    print(f"{provincia}: {conteo}")



