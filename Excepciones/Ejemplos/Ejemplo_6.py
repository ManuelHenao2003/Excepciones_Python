# ---------------- MAL EJEMPLO ----------------

# Intenta ejecutar todo el bloque de código
try:

    # Abre el archivo "datos.txt" en modo lectura
    archivo = open("datos.txt", "r")

    # Lee todo el contenido del archivo
    contenido = archivo.read()

    # Divide el contenido por espacios y convierte cada dato en entero
    numeros = [int(x) for x in contenido.split()]

    # Suma todos los números y calcula el promedio
    resultado = sum(numeros) / len(numeros)

    # Muestra el promedio
    print(f"El promedio es:{resultado}")

    # Cierra el archivo
    archivo.close()

# Captura cualquier error que ocurra
except:

    # Muestra un mensaje genérico de error
    print("Ocurrió un error")  # Mensaje poco útil



# ---------------- BUEN EJEMPLO ----------------

# Intenta abrir el archivo
try:

    # Abre el archivo "datos.txt"
    archivo = open("datos.txt", "r")

# Se ejecuta si el archivo no existe
except FileNotFoundError:

    # Muestra un mensaje indicando que el archivo no existe
    print("El archivo 'datos.txt' no existe")

    # Finaliza la ejecución
    return


# Intenta leer y convertir los datos
try:

    # Lee el contenido del archivo
    contenido = archivo.read()

    # Convierte los datos en números enteros
    numeros = [int(x) for x in contenido.split()]

# Se ejecuta si algún dato no es un número válido
except ValueError:

    # Muestra un mensaje de error
    print("El archivo contiene datos que no son números")

    # Cierra el archivo
    archivo.close()

    # Finaliza la ejecución
    return


# Intenta calcular el promedio
try:

    # Calcula el promedio de los números
    resultado = sum(numeros) / len(numeros)

    # Muestra el resultado
    print(f"El promedio es:{resultado}")

# Se ejecuta si ocurre división entre cero
except ZeroDivisionError:

    # Muestra un mensaje indicando que el archivo está vacío
    print("El archivo está vacío, no se puede calcular el promedio")

# Cierra el archivo
archivo.close()