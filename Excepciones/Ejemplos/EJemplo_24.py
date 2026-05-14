# Intenta ejecutar el código dentro del bloque try
try:

    # Obtiene datos desde una API
    datos = obtener_datos_de_api()

    # Valida que los datos tengan el formato correcto
    validar_formato(datos)

# Se ejecuta si ocurre un error de conexión con el servidor
except ConexionError:

    # Muestra un mensaje indicando que no se pudo conectar
    print("No se pudo conectar con el servidor.")

# Se ejecuta si los datos tienen un formato incorrecto
except FormatoInvalidoError:

    # Muestra un mensaje indicando que el formato es inválido
    print("Los datos recibidos tienen un formato incorrecto.")

# Se ejecuta únicamente si no ocurrió ninguna excepción
else:

    # Procesa los datos obtenidos y validados
    resultados = procesar_datos(datos)

    # Guarda los resultados procesados
    guardar_resultados(resultados)