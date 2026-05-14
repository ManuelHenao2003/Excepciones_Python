try:
    # Intenta abrir el archivo "datos.txt" en modo lectura
    archivo = open("datos.txt", "r")

    # Lee la primera línea del archivo, elimina espacios
    # y la convierte en número entero
    valor = int(archivo.readline().strip())

    # Divide 100 entre el valor obtenido del archivo
    resultado = 100 / valor

except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    # Se ejecuta si ocurre alguno de estos errores:
    # FileNotFoundError -> el archivo no existe
    # ValueError -> el contenido no es un número válido
    # ZeroDivisionError -> el valor es 0 y no se puede dividir

    # Muestra el tipo de error ocurrido
    print(f"Ocurrió un error: {type(e).__name__}")

    # Muestra la descripción detallada del error
    print(f"Descripción: {e}")