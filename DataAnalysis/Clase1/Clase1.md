# Librerías
## Libería CV2
- te deja en 10 lineas de codigo leer el texto de una imágen

## Librería math
- para usar las librerías hacemos:
  ``` python
  import math as m
  x = m.cos(m.pi)
  print(x)```

- las librerias que no son de python hay que cargarnos esas liberias
  - en la terminal hacemos install (eg: install pandas o xlrd)
  ``` python
  import pandas as pd
  df = pd.read_excel("")
  printf(df)```

## Librería pandas
- nos permite sistematizar la conversión de un archivo de información en los tipos de datos que python maneja -> nosotros lo utilizamos para leer archivos conn info en filas/columnas como excel o csv
- se usa mucho en data science
- puede agregar columnas o eliminarlas

 ``` python
  import pandas as pd
  url = ""
  df = pd.read_excel(url)
  printf(df)  # estructura de datos nativa de pandas
  import wget as w
  w.get(url)
  alumno = df.loc[0]  # te agarra al primer alumno con todas su info
  print(alumno["Quimica"]   # te da la nota de Química de ese alumno
  d = df.to_dict("list")
  print(d)  # obtengo un diccionario cuyas claves son el nombre de las columnas
  print(d["Quimica"])   # me da en un array las notas de Quimica
  # si en vez de "list" pongo "records" se me da la info por persona osea por fila
  # dependiendo lo que queremos tener o agarrar es lo que metemos dentro de to_dict
  df = pd.read_excel("Datos.xlsx", index_col = "legajo")
  alumno = df.loc[64498]  # osea lo de antes te lo organiza o divide por legajo
  print(alumno)   # esto tambien es lowkey un array de la info de ese alumno con ese legajo
  ```
### .to_dict("List")
- te hace un diccionario que no es la mismo que un dataframe (que es lo que te devuelve read)
- si hacemos datos = archivo.to_dict("List") -> almacenamos cada columna como una lista
- los indices no son numeros sino son el nombre de cada columna tipo datos['Apellido']
- ahora si queremos hacer datos['Apellido'][0] ahí si me da el primer apellido en la lista
- List -> te genera un diccionario en el que las claves son el nombre de las columnas
### .to_dict("records")
- significa que vamos a obtener el contenido separado por fila
- data[2] -> te da la tercera fila
- data[2]['Nombre'] -> accedemos la categoria Nombre de la tercera fila
### .read_excel("Datos.xlsx", index_col ="Apellido")
- decimos que la columna de indexación será Apellido
- donde la clave será los apellidos (es nuestra fila)
- donde los elementos de cada clave son los otros campos
### pd.DataFrame(data)
- te da un dataframe (que es muy parecido a un excel) de data (una matriz ponele) 
### dataFrame.to_excel("miArchivo.xlsx")
- te convierte el dataframe a ese archivo

## DataFrames (de Pandas)
### Creación de DataFrames
``` python 
import pandas as pd
import random as n

data = {
    "usuario": ["pato", "nato", "gato"],
    "pass": ["abc123", "contra", "xasda"],
    "random": []
}

for i in range(3): # 3 iteraciones osea de 0 a 2
  data["random"].append( n.randint(1, 30)) # te mete en esa fila los siguientes valores
print(data)
df = pd.DataFrame(data) # te da un dataframe de data
print(df)  # te lo imprime como un dataframe


```

### Atributos y métodos de Pandas
``` python
import pandas as pd
url = "https://covid.ourworldindata.org/algo.csv"

import wget as w
w.wget(url)  # esto hace que se te bajen los datos osea ya ni necesitas el url porque te guarda algo.csv

df = pd.read_csv(url)               # es igual al de abajo
df = pd.read_csv("full_data.csv")   # hace lo mismo que arriba

print(df) # te corta los datos (osea te saca algunas columnas)

# para que no suceda lo de arriba hay que hacer primero:
pd.set_option("display.max_columns", 10) # esto despues del read
print(df) # ahí te dice la maxima cantidad de columnas que te muestra

print(df.shape) # te deuvelve el tamaño
# => (num1, num2) siendo num1 #filas y num2 #columnas

print(df.size) 
# => te devuelve #celdas

print(df.info())
# => nos da información sobre qué hay en cada columna tipo datatype count, etc

print(df["new_cases"].sum() / 2, df["total_cases"].max()) # osea acá las filas son tus columnas tipo es como si estuvieras filas con cada titulo que contiene sus respectivos datos

print( df[ df["new_cases"] == df["new_cases"].max()])
# me va a buscar las filas en donde los nuevos casos son iguales a los maxima cantidad de nuevos casos

# otra opción
df = df[ df["location"] != "World" ] 
aprobados = datos[ datos['Quimica'] >= 4 ] # aca lo que hace es darte todos los datos de aquellos alumnos que aprobaron quimica
# si quisieras solamente las notas de quimica ahi podrias hacer despues:
aprobados["Quimica"]
# => osea te da los df que no sean world
print( df[ df["new_cases"] == df["new_cases"].max()])
```
- es como que dentro de df podes poner condiciones dentro de los data frames
- podes poner hasta & que es como nuetro &&

# Interesante de los desafíos
``` python 
archivo = pd.read_excel("Tabla1.xlsx", index_col = "Puntos")
data = archivo.to_dict("index")
puntos = archivo.to_dict("List")
print("El campeón es: " + data[max(data)]["Equipo"])
print("El perdedor es: " + data[min(data)]["Equipo"])
```
=> 
El campeón es: Equipo A
El perdedor es: Equipo D

----------------------------------
``` python
archivo = pd.read_excel("Tabla1.xlsx", index_col = "Puntos")
data = archivo.to_dict("index")
print(data)

ordenada = sorted(data, reverse=True)
print(ordenada)

for punto in ordenada:
    if punto > 20:
      print(data[punto]["Equipo"] + " tiene a siguiente diferencia de goles: " + str(data[punto]["Goles a favor"] - data[punto]["Goles en contra"]))
```
=> 
- lo interesante aca es que no puedo cambiar data con ordenada porque lowkey cuando hago for in data teniendo en cuenta que lo indexo con "Puntos" me toma el nombre data como si fuera un array con valores que son los Puntos por ende cuando hago ordenada, (ordenar de mayor a menor), lo que hace es crearme un arreglo con los puntos ordenados

``` python
columna = 'Quimica'
print(datos[columna])
```
=> te devuelve:
``` python
0    10
1     4
2     2
3     9
4     8
5     1
Name: Quimica, dtype: int64
```
- osea a diferencia de un dictionary, el dataframe te da el indice de cada fila, el nombre de la columna y el tipo de dato

``` python
indice = 0
alumno = datos.loc[indice] # te da la primera fila (acordarse que las categorias estan por columna)

datos["nombreColumna"] # acá estamos agarrando toda una columna
print(alumno) 
```

``` python
len(dataFrame) # te da la cantidad de filas del dataframe
```

- pandas tiene muchas funciones también para desglozar informacion
``` python

horas = [0] * 24
for hora in pd.to_datetime(archivo["Fecha de inicio"]).dt.hour: #te da básicamente un array de horas siendo que en fecha de inicio aparace tambien la fecha y horas y minutos + segundos osea te agarra cierta data
  horas[hora] += 1
maxHora = horas.index(max(horas))
print("de " + str(maxHora) + "hs a " + str(horas.index(max(horas))+1) + "hs") 

#ej4: ¿Cuántas estaciones diferentes fueron utilizadas?
idsDeEstacion = pd.concat([archivo['Id de estación de fin de viaje'], archivo['Id de estación de inicio']], ignore_index=True)
idsUnicos = np.unique(idsDeEstacion)
print("Fueron utilizadas " + str(len(idsUnicos)) + " estaciones diferentes.")

#ej5: : Para cada estación utilizada como inicio de un viaje, imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
unicos_ids = archivo[['Id de estación de inicio']].drop_duplicates() # te da un dataframe de esa columna sin duplicados
unicos_ids['Cantidad de viajes'] = [0] * len(unicos_ids)
print(len(unicos_ids))

for ids in unicos_ids['Id de estación de inicio']:
  # lo siguiente no funciona porque no entiende si queres hacer una copia o modificar el posta
  # unicos_ids[unicos_ids['Id de estación de inicio'] == ids]['Cantidad de viajes'] = len(archivo[archivo['Id de estación de inicio'] == ids])

  #lo siguiente hace lo que queremos: el .loc[filtro, columna] => entonces ahí filtramos y los que quedan afectamos su columna columna
  unicos_ids.loc[unicos_ids['Id de estación de inicio'] == ids, 'Cantidad de viajes'] = len(archivo[archivo['Id de estación de inicio'] == ids])
print(unicos_ids.sort_values(by='Cantidad de viajes')) #ordenamos de menor a mayor el dataframe segun la columna Cantidad de viajes 

```
``` Python
#lo que hace es leerte la pagina Usuarios del excel
usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios",index_col="Usuario")

#si hicieramos lo siguiente: (luego no podriamos usar como índice la columna Usuario)
usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios")
# Supongamos que la columna "Usuario" existe, pero NO es índice

# Esto NO funcionará:
usuarios_archivo.loc["juan123"]
# ❌ KeyError, porque "juan123" no es un índice
```

- otro ej interesante:
``` Python
usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios", index_col="Usuario")
#leemos los usuarios "indexados" por su nombre

transferencias_archivo = pd.read_excel("Finanzas.xlsx", "Transferencias")
print(transferencias_archivo)
print(usuarios_archivo)
usuarios_newArchivo = usuarios_archivo.copy()
transferencias_archivo = transferencias_archivo.set_index('Emisor')
for emisor in transferencias_archivo.index: #porque una vez que volvimos a una columna en un index ya no se considera como columna
  monto = transferencias_archivo.loc[emisor, 'Monto'] #podemos usar .loc sin volverlo en indice pero si hacemos eso python considera que estas agarrando un conjunto de valores, no un valor solo
  usuarios_newArchivo.loc[emisor, 'Presupuesto'] -= monto
  usuarios_newArchivo.loc[transferencias_archivo.loc[emisor, 'Receptor'], 'Presupuesto'] += monto
usuarios_newArchivo = usuarios_newArchivo.reset_index()
print(usuarios_newArchivo)
```

- si quiero cambiar valores si o si lo tengo que hacer con un loc

- es re interesante saber que los dataframes te ignoran los nan al hacer ecuaciones y cosas así 

- para mergear dataframes

``` python
lista_merged = pd.merge(lista1, lista2, on=['Nombre', 'Apellido', 'Mail'], how='outer') # on son las columnas en comun. mientras que how le dice que si no tiene esa columna, esa fila, entonces que meta un nan
print("Esto es la lista final")
print(lista_merged)
```