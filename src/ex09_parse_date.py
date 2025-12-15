"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    raise NotImplementedError("Implementa parse_date(date_str)")

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    date_str = date_str.strip()
    parts = date_str.split("/")
    
    if len(parts) != 3:
        raise ValueError("La fecha debe tener formato d/m/aaaa")
    
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        raise ValueError("Los componentes de la fecha deben ser enteros")
    
    if not (1 <= day <= 31):
        raise ValueError("El día debe estar entre 1 y 31")
    if not (1 <= month <= 12):
        raise ValueError("El mes debe estar entre 1 y 12")
    if year < 1:
        raise ValueError("El año debe ser positivo")
    
    return day, month, year
