import random

# Definir las opciones
COOPERAR = "cooperar"
TRAICIONAR = "traicionar"

# Resultados de las sentencias según las decisiones
RESULTADOS = {
    (COOPERAR, COOPERAR): (1, 1),  # Ambos cooperan
    (COOPERAR, TRAICIONAR): (5, 0),  # El primero coopera, el segundo traiciona
    (TRAICIONAR, COOPERAR): (0, 5),  # El primero traiciona, el segundo coopera
    (TRAICIONAR, TRAICIONAR): (3, 3)  # Ambos traicionan
}

# Función que simula el dilema del prisionero
def dilema_prisionero(eleccion_prisionero_1, eleccion_prisionero_2):
    # Obtener las sentencias de ambos prisioneros
    sentencia_prisionero_1, sentencia_prisionero_2 = RESULTADOS[(eleccion_prisionero_1, eleccion_prisionero_2)]
    return sentencia_prisionero_1, sentencia_prisionero_2

# Estrategia automática: elige aleatoriamente (cooperar o traicionar)
def estrategia_aleatoria():
    return random.choice([COOPERAR, TRAICIONAR])

# Simulación del dilema por 100 iteraciones
def simular_dilema(iteraciones):
    for i in range(1, iteraciones + 1):
        # Ambos prisioneros usan la estrategia aleatoria
        eleccion_prisionero_1 = estrategia_aleatoria()
        eleccion_prisionero_2 = estrategia_aleatoria()
        
        # Obtener las sentencias
        sentencia_1, sentencia_2 = dilema_prisionero(eleccion_prisionero_1, eleccion_prisionero_2)
        
        # Mostrar la iteración y los resultados
        print(f"Iteración {i}:")
        print(f"  Prisionero 1 elige: {eleccion_prisionero_1}")
        print(f"  Prisionero 2 elige: {eleccion_prisionero_2}")
        print(f"  Sentencia del Prisionero 1: {sentencia_1} años")
        print(f"  Sentencia del Prisionero 2: {sentencia_2} años\n")

# Ejecutar el dilema del prisionero 100 veces
simular_dilema(100)
