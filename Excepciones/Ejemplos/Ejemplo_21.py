# Importa la librería requests para realizar solicitudes HTTP
import requests

# Intenta ejecutar el código dentro del bloque try
try:

    # Realiza una solicitud GET a la URL indicada
    # timeout=1 significa que esperará máximo 1 segundo
    respuesta = requests.get("https://api.ejemplo.com/datos", timeout=1)

    # Genera una excepción si la respuesta HTTP contiene un error
    # como 404 o 500
    respuesta.raise_for_status()

# Se ejecuta si no se puede conectar al servidor
except requests.exceptions.ConnectionError:

    # Muestra un mensaje indicando que falló la conexión
    print("No se pudo conectar al servidor")

# Se ejecuta si la solicitud tarda demasiado tiempo
except requests.exceptions.Timeout:

    # Muestra un mensaje indicando que el tiempo de espera fue excedido
    print("La solicitud excedió el tiempo de espera")

# Se ejecuta si ocurre un error HTTP
except requests.exceptions.HTTPError as e:

    # Muestra el error HTTP ocurrido
    print(f"Error HTTP:{e}")