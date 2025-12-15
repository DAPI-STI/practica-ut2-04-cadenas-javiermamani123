"""
Ejercicio 10: leer una lista de productos separados por comas y mostrar cada uno en una línea.

La función:

Recibe una cadena tipo "pan, leche, huevos".

Devuelve una lista con ["pan", "leche", "huevos"], sin espacios sobrantes.
"""

def split_products(csv_line: str) -> list[str]:
    """Devuelve una lista de productos sin espacios extra a partir de una línea CSV simple."""
    # TODO: usa .split(",") y .strip() para limpiar espacios
    raise NotImplementedError("Implementa split_products(csv_line)")

def split_products(csv_line: str) -> list[str]:
    """Devuelve una lista de productos sin espacios extra y sin vacíos."""
    items = csv_line.split(",")
    # Filtramos elementos vacíos después de strip
    return [item.strip() for item in items if item.strip()]

