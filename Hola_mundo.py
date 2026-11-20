# Autor: Bernardo Velasco Ortega
# Matrícula: AL07127004
# Descripción: Cálculo de tarifa de estacionamiento por tiempo transcurrido

import math

def calcular_tarifa(minutos_totales: int, boleto_perdido: bool = False) -> float:
    """
    Calcula el costo total de estacionamiento en MXN bajo las siguientes reglas:
    - Boleto perdido: tarifa fija de $250.00 MXN.
    - Tolerancia: primeros 15 minutos gratis.
    - Primera hora (16 a 60 min): $30.00 MXN.
    - Hora adicional o fracción (después de la 1ra hora): $20.00 MXN por hora.
    - Tarifa máxima por día (24 horas): $220.00 MXN.
    """
    if boleto_perdido:
        return 250.00

    if minutos_totales < 0:
        raise ValueError("El tiempo transcurrido no puede ser negativo.")

    # Tolerancia de 15 minutos
    if minutos_totales <= 15:
        return 0.00

    tarifa_primera_hora = 30.00
    tarifa_hora_adicional = 20.00
    tarifa_maxima_diaria = 220.00

    # Cálculo por días completos + horas restantes
    minutos_por_dia = 24 * 60
    dias_completos = minutos_totales // minutos_por_dia
    minutos_restantes = minutos_totales % minutos_por_dia

    costo_restante = 0.00
    if minutos_restantes > 0:
        if minutos_restantes <= 60:
            costo_restante = tarifa_primera_hora
        else:
            horas_adicionales = math.ceil((minutos_restantes - 60) / 60)
            costo_restante = tarifa_primera_hora + (horas_adicionales * tarifa_hora_adicional)
        
        # Aplicar tope diario si el fracción del día supera el máximo
        costo_restante = min(costo_restante, tarifa_maxima_diaria)

    total = (dias_completos * tarifa_maxima_diaria) + costo_restante
    return total


def main():
    print("=== SISTEMA DE COBRO DE ESTACIONAMIENTO ===")
    try:
        perdido_input = input("¿El usuario perdió su boleto? (s/n): ").strip().lower()
        boleto_perdido = perdido_input == "s"

        if boleto_perdido:
            total = calcular_tarifa(0, boleto_perdido=True)
            print(f"\nConcepto: Boleto perdido")
            print(f"Total a pagar: ${total:,.2f} MXN")
            return

        horas = int(input("Ingresa las horas completas de estancia: "))
        minutos = int(input("Ingresa los minutos adicionales (0-59): "))

        if horas < 0 or not (0 <= minutos <= 59):
            print("Error: Verifica que las horas sean >= 0 y los minutos estén entre 0 y 59.")
            return

        minutos_totales = (horas * 60) + minutos
        total = calcular_tarifa(minutos_totales)

        print(f"\nTiempo total: {horas}h {minutos}m ({minutos_totales} min)")
        print(f"Total a pagar: ${total:,.2f} MXN")

    except ValueError:
        print("Error: Por favor ingresa únicamente valores numéricos enteros.")


if __name__ == "__main__":
    main()
