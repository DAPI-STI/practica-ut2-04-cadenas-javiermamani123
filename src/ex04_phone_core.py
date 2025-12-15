"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    raise NotImplementedError("Implementa phone_core(s)")

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    s = s.strip()  # eliminar espacios al inicio y final
    parts = s.split("-")
    
    if len(parts) != 3:
        raise ValueError("El teléfono debe tener exactamente 3 partes separadas por '-'")
    
    prefix, number, extension = parts
    
    if not prefix.startswith("+"):
        raise ValueError("El prefijo debe comenzar con '+'")
    
    if not number.isdigit():
        raise ValueError("La parte central debe ser numérica")
    
    return number
