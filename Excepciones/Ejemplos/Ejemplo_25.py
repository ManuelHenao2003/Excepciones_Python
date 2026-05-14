# Función para retirar dinero de una cuenta
def retirar_dinero(cuenta, cantidad):

    # Verifica si la cuenta está activa
    if not cuenta.esta_activa:

        # Genera un error si la cuenta no está activa
        raise ValueError("La cuenta no está activa")

    # Verifica si la cantidad es menor o igual a 0
    if cantidad <= 0:

        # Genera un error porque la cantidad debe ser positiva
        raise ValueError("La cantidad debe ser positiva")

    # Verifica si la cantidad es mayor que el saldo disponible
    if cantidad > cuenta.saldo:

        # Genera un error por saldo insuficiente
        raise ValueError("Saldo insuficiente")

    # Resta la cantidad retirada al saldo de la cuenta
    cuenta.saldo -= cantidad

    # Retorna el saldo actualizado
    return cuenta.saldo