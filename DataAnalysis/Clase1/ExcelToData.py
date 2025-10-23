
# ejemplo1.py
import pandas as pd

archivo = pd.read_excel("Datos.xlsx")
# La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'
print(archivo)


data = archivo.to_dict("List") # "list" significa que vamos a almacenar a cada columna como una lista con su contenido

print(data)
print(data['Nombre'])     # Accedemos a los datos de una columna
print(data['Nombre'][2])  # Accedemos al índice 2 de la columna 'Nombres'

data = archivo.to_dict("records")
# "records" significa que vamos a obtener el contenido separado por cada fila

print(data)
print(data[2])            # Accedemos a los datos de una fila
print(data[2]['Nombre'])  # Accedemos a la columna 'Nombres' de la fila con índice 2

# Indicamos que la columna de indexación será apellido.
archivo = pd.read_excel("archivo.xslsx", "Apellido") # esto te da un dataframe
print(archivo)

data = archivo.to_dict("index") #esto un diccionario
# "index" significa que vamos a obtener el contenido como diccionarios
# donde la clave es algun campo de cada fila, en este caso la clave de los
# diccionarios será la clave "Apellido"

# convertimos el tipo de dato de pandas a un dict de python

print(data)
print(data['Martinez'])           # Accedemos a los datos de una fila (usando el dato de índice apropiado)
print(data['Martinez']['Legajo']) # Accedemos a la columna 'Legajo' de la fila con índice 'Martinez'