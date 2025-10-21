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
  printf(df) //estructura de datos nativa de pandas
  import wget as w
  w.get(url)
  alumno = df.loc[0] //te agarra al primer alumno con todas su info
  print(alumno["Quimica"] // te da la nota de Química de ese alumno
  d = df.to_dict("list")
  print(d) //obtengo un diccionario cuyas claves son el nombre de las columnas
  print(d["Quimica"]) // me da en un array las notas de Quimica
  // si en vez de "list" pongo "records" se me da la info por persona osea por fila
  // dependiendo lo que queremos tener o agarrar es lo que metemos dentro de to_dict
  df = pd.read_excel("Datos.xlsx", index_col = "legajo")
  alumno = df.loc[64498] //osea lo de antes te lo organiza o divide por legajo
  print(alumno) //esto tambien es lowkey un array de la info de ese alumno con ese legajo
  ```
### .to_dict("List")
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

for i in range(3): //3 iteraciones osea de 0 a 2
  data["random"].append( n.randint(1, 30)) //te mete en esa fila los siguientes valores
print(data)
df = pd.DataFrame(data) // te da un dataframe de data
print(df)  //te lo imprime como un dataframe
```

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


