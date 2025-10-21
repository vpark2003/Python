#!/usr/bin/env python3
# Si no estamos en un entorno linux podemos definir nuestra propia wget
# Esta función nos ayuda a descargar archivos desde la web y no es necesaria para archivos locales
# No es necesario entender cómo funciona, se las mostramos sólo por si alguno llega a necesitarla
# uso: ./wget_personal.py linkDelArchivo
# Importamos la libreria requests
import requests
import sys
import os

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

# --- Programa principal ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 wget_personal.py <URL>")
    else:
        wget(sys.argv[1])

