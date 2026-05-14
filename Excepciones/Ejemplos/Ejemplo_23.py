# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta abrir el archivo "datos.txt" en modo lectura
    archivo = open("datos.txt", "r")

    # Lee el contenido del archivo
    contenido = archivo.read()

# Se ejecuta si el archivo no existe
except FileNotFoundError:

    # Muestra un mensaje indicando que el archivo no existe
    print("El archivo no existe.")

    # Guarda una cadena vacía en la variable contenido
    contenido = ""

# Se ejecuta únicamente si no ocurrió ninguna excepción
else:

    # Muestra un mensaje indicando que el archivo fue leído correctamente
    print("Archivo leído correctamente.")

    # Cierra el archivo porque se abrió correctamente
    archivo.close()  # Solo cerramos si se abrió con éxito