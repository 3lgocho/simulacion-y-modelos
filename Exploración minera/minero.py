import random

def simulacion_exploracion(intentos, barriles_medio=1000):
    costo_exploracion = 1_000_000
    prob_exito = 0.4
    ganancia_por_barril = 150
    ganancia_adicional = 300_000
    porcentaje_estado = 0.4
    porcentaje_empresa = 0.6

    ganancias_totales = 0
    exitos = 0  # Contador de éxitos

    for i in range(intentos):
        exito = (random.random() * 0.9) + 0.1 < prob_exito  # Genera un valor entre 0.1 y 1
        if exito:
            exitos += 1  # Incrementa el contador de éxitos
            # Barriles encontrados (suponemos una media y una variabilidad)
            barriles = int(random.gauss(barriles_medio, barriles_medio * 0.1))  # 10% de variabilidad
            ingresos_brutos = barriles * ganancia_por_barril + ganancia_adicional
            
            # Distribución de ingresos
            ingreso_empresa = ingresos_brutos * porcentaje_empresa
            ingreso_estado = ingresos_brutos * porcentaje_estado

            ganancia = ingreso_empresa - costo_exploracion
            ganancias_totales += ganancia
            print(f"Exploración {i + 1}: Éxito! Barriles = {barriles}, Ganancia para la empresa = ${ingreso_empresa}, Ganancia para el estado = ${ingreso_estado}")
        else:
            # Pérdida completa del costo de exploración
            ganancia = -costo_exploracion
            ganancias_totales += ganancia
            print(f"Exploración {i + 1}: Fallo. Pérdida = ${costo_exploracion}")

    # Cálculo del promedio de ganancias
    ganancia_promedio = ganancias_totales / intentos
    umbral_exito = (exitos / intentos) * 100  # Cálculo del umbral de éxito en porcentaje

    print(f"\nGanancia total después de {intentos} intentos: ${ganancias_totales}")
    print(f"Ganancia promedio por exploración: ${ganancia_promedio}")
    print(f"Umbral de éxito: {umbral_exito:.2f}%")
    return ganancia_promedio, umbral_exito

# Ejecutar la simulación con 100 exploraciones
simulacion_exploracion(200)
