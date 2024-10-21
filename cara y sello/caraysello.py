import random
import pandas as pd

# Solicitar una apuesta inicial válida
def obtener_apuesta():
    while True:
        try:
            apuesta_inicial = float(input("Ingresa tu apuesta inicial (mayor a 0 y menor o igual a 1000): "))
            if 0 < apuesta_inicial <= 1000:
                return apuesta_inicial
            else:
                print("La apuesta debe ser mayor a 0 y menor o igual a 1000.")
        except ValueError:
            print("Por favor ingresa un número válido.")

# Juego de cara o sello
def jugar():
    apuesta = obtener_apuesta()
    rondas = 0
    dinero = 1000

    # Lista para almacenar los datos de cada ronda
    datos_rondas = []

    while rondas < 100 and dinero > 1:
        moneda = random.randint(0, 1)  # Random para cara o sello
        dado = random.randint(0, 1)    # Random para el dado

        if moneda == 1 and dado == 1:  # Si ambos son 1, ganas la apuesta
            dinero += apuesta
            print(f"¡Ganaste! Ahora tienes {dinero} de dinero.")

            # Guardar los datos de la ronda en la lista
            datos_rondas.append({
                'Ronda': rondas + 1,
                'Dinero Actual': dinero,
                'Apuesta': apuesta})
            apuesta = apuesta / 2
        else:
            dinero -= apuesta  # Se pierde la mitad de la apuesta
            print(f"Perdiste esta ronda. Ahora tienes {dinero} de dinero.")  
            datos_rondas.append({
                'Ronda': rondas + 1,
                'Dinero Actual': dinero,
                'Apuesta': apuesta
        })
            apuesta = apuesta * 2



        rondas += 1
        print(f"Ronda {rondas} finalizada.\n")

    # Crear un DataFrame de pandas con los datos de las rondas
    df = pd.DataFrame(datos_rondas)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel("resultados_juego.xlsx", index=False)
    print("Los resultados del juego se han guardado en 'resultados_juego.xlsx'.")

    if dinero <= 0:
        print("Te has quedado sin dinero. Fin del juego.")
    else:
        print(f"Has alcanzado las {rondas} rondas. Te quedan {dinero} de dinero.")

jugar()
