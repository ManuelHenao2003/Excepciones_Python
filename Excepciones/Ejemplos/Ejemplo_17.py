# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta importar un módulo llamado "biblioteca_inexistente"
    import biblioteca_inexistente

# Se ejecuta si el módulo no existe o no puede importarse
except ImportError:

    # Muestra un mensaje indicando que el módulo no pudo importarse
    print("No se pudo importar el módulo")