# Autor: Bernardo Velasco Ortega
# Matrícula: AL07127004
# Descripción: Cálculo y registro de entrega/devolución de un libro en biblioteca

import sys
from datetime import datetime


def registrar_entrega(titulo: str, usuario: str, fecha_limite_str: str, fecha_entrega_str: str, multa_por_dia: float = 15.0) -> dict:
    """
    Calcula los días de retraso y la multa correspondiente al devolver un libro.
    Formato de fechas esperado: 'YYYY-MM-DD'
    """
    fecha_limite = datetime.strptime(fecha_limite_str, "%Y-%m-%d").date()
    fecha_entrega = datetime.strptime(fecha_entrega_str, "%Y-%m-%d").date()

    diferencia_dias = (fecha_entrega - fecha_limite).days
    dias_retraso = max(0, diferencia_dias)
    multa_total = dias_retraso * multa_por_dia
    estado = "Entrega a tiempo" if dias_retraso == 0 else f"Entrega con retraso ({dias_retraso} día(s))"

    return {
        "titulo": titulo,
        "usuario": usuario,
        "fecha_limite": fecha_limite,
        "fecha_entrega": fecha_entrega,
        "dias_retraso": dias_retraso,
        "multa_total": multa_total,
        "estado": estado
    }


def main():
    print("=== REGISTRO DE ENTREGA DE LIBRO ===")

    # Si se pasan argumentos por consola se usan; si no (como en GitHub Actions), usa datos de prueba
    titulo = sys.argv[1] if len(sys.argv) > 1 else "Clean Code"
    usuario = sys.argv[2] if len(sys.argv) > 2 else "Bernardo Velasco (AL07127004)"
    fecha_limite = sys.argv[3] if len(sys.argv) > 3 else "2026-11-15"
    fecha_entrega = sys.argv[4] if len(sys.argv) > 4 else "2026-11-20"

    registro = registrar_entrega(titulo, usuario, fecha_limite, fecha_entrega)

    print("\n--- COMPROBANTE DE DEVOLUCIÓN ---")
    print(f"Libro:          {registro['titulo']}")
    print(f"Usuario:        {registro['usuario']}")
    print(f"Fecha límite:   {registro['fecha_limite']}")
    print(f"Fecha entrega:  {registro['fecha_entrega']}")
    print(f"Estado:         {registro['estado']}")
    print(f"Multa a pagar:  ${registro['multa_total']:,.2f} MXN")


if __name__ == "__main__":
    main()
