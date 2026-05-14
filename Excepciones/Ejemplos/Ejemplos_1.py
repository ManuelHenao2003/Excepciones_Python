try:
    # Se intenta ejecutar este bloque de código
    numero1 = 10  # Guarda el valor 10 en la variable numero1
    numero2 = 0   # Guarda el valor 0 en la variable numero2

    # Intenta dividir 10 entre 0
    resultado = numero1 / numero2

    # Muestra el resultado de la división
    # Esta línea no se ejecuta porque ocurre un error antes
    print(f"El resultado es:{resultado}")

except:
    # Este bloque se ejecuta cuando ocurre un error
    # En este caso, porque no se puede dividir entre cero
    print("¡Ups! No se puede dividir entre cero.")