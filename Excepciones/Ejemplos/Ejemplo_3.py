try:
    # Intenta abrir el archivo en modo lectura ("r")
    with open("archivo_inexistente.txt", "r") as archivo:

        # Lee el contenido del archivo
        contenido = archivo.read()

except FileNotFoundError as error:
    # Se ejecuta si el archivo no existe
    print(f"Error: {error}")

    # Muestra un mensaje indicando que se creará un nuevo archivo
    print("Creando un archivo nuevo...")

    # Crea un nuevo archivo en modo escritura ("w")
    with open("archivo_inexistente.txt", "w") as archivo:

        # Escribe texto dentro del nuevo archivo
        archivo.write("Este es un archivo nuevo")