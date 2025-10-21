# Librerías
## Libería CV2
- te deja en 10 lineas de codigo leer el texto de una imágen

## Librería math
- para usar las librerías hacemos:
  `import math as m
  x = m.cos(m.pi)
  print(x)`

- las librerias que no son de python hay que cargarnos esas liberias
  - en la terminal hacemos install (eg: install pandas o xlrd)
  `import pandas as pd
  df = pd.read_excel("")
  printf(df)`

## Librería pandas
- nos permite sistematizar la conversión de un archivo de información en los tipos de datos que python maneja -> nosotros lo utilizamos para leer archivos conn info en filas/columnas como excel o csv
- se usa mucho en data science
- puede agregar columnas o eliminarlas
 `import pandas as pd
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
  `
  
