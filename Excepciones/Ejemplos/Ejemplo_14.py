# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta abrir el archivo protegido "/etc/passwd" en modo escritura
    with open("/etc/passwd", "w") as archivo:

        # Intenta escribir el texto "datos" en el archivo
        archivo.write("datos")

# Se ejecuta si el programa no tiene permisos para modificar el archivo
except PermissionError:

    # Muestra un mensaje indicando que no hay permisos suficientes
    print("No tienes permisos para modificar este archivo")