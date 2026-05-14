# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta importar un módulo que no existe
    import modulo_que_no_existe

# Se ejecuta si el módulo no es encontrado
except ModuleNotFoundError:

    # Muestra un mensaje indicando que el módulo no existe
    print("El módulo no existe")