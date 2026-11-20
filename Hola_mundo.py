# Autor: Bernardo Velasco Ortega
# Matrícula: AL07127004
# Descripción: Cálculo y registro de entrega/devolución de un libro en biblioteca

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
    try:
        titulo = input("Título del libro: ").strip()
        usuario = input("Nombre del usuario o matrícula: ").strip()
        fecha_limite = input("Fecha límite de entrega (AAAA-MM-DD): ").strip()
        fecha_entrega = input("Fecha real de entrega (AAAA-MM-DD): ").strip()

        registro = registrar_entrega(titulo, usuario, fecha_limite, fecha_entrega)

        print("\n--- COMPROBANTE DE DEVOLUCIÓN ---")
        print(f"Libro:          {registro['titulo']}")
        print(f"Usuario:        {registro['usuario']}")
        print(f"Fecha límite:   {registro['fecha_limite']}")
        print(f"Fecha entrega:  {registro['fecha_entrega']}")
        print(f"Estado:         {registro['estado']}")
        print(f"Multa a pagar:  ${registro['multa_total']:,.2f} MXN")

    except ValueError:
        print("Error: Verifica que las fechas tengan el formato correcto (AAAA-MM-DD).")


if __name__ == "__main__":
    main()
