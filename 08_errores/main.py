"""
¡Manejando Errores y Excepciones en Python!

Este archivo te enseña a usar 'try', 'except', 'else' y 'finally'
para controlar situaciones inesperadas y evitar que tu programa se detenga.
"""

def convertir_a_entero(texto):
    """
    Intenta convertir un texto a un número entero.
    Maneja el error si el texto no es un número válido.
    """
    print(f"\n--- Intentando convertir '{texto}' a entero ---")
    try:
        # Intentamos ejecutar este código, que podría fallar
        numero = int(texto)
        print(f"¡Éxito! El número es: {numero}")
    except ValueError:
        # Si ocurre un error de tipo 'ValueError' dentro del 'try',
        # se ejecuta este bloque 'except'.
        print("¡Error! El texto ingresado no parece ser un número entero válido.")
    except Exception as e:
        # Podemos capturar otros tipos de errores inesperados
        print(f"¡Ocurrió otro tipo de error inesperado!: {e}")
    else:
        # Este bloque (opcional) se ejecuta SOLO SI NO hubo errores en el 'try'.
        print("(Bloque 'else': Se ejecutó porque no hubo errores)")
    finally:
        # Este bloque (opcional) se ejecuta SIEMPRE, haya habido error o no.
        # Es útil para limpiar recursos (como cerrar archivos).
        print("(Bloque 'finally': Esto se ejecuta siempre al final)")

def dividir_numeros(dividendo, divisor):
    """
    Intenta dividir dos números.
    Maneja el error específico de división por cero.
    """
    print(f"\n--- Intentando dividir {dividendo} / {divisor} ---")
    try:
        resultado = dividendo / divisor
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        # Capturamos específicamente el error de dividir por cero.
        print("¡Error! No se puede dividir por cero.")
    except TypeError:
        # Capturamos si los tipos no son correctos para dividir
        print("¡Error! Asegúrate de que ambos sean números.")
    except Exception as e:
        print(f"¡Ocurrió otro error inesperado!: {e}")
    finally:
        print("(Bloque 'finally': Fin del intento de división)")


# Punto de entrada principal del script
if __name__ == "__main__":
    # --- Probando la conversión ---
    convertir_a_entero("123")   # Caso exitoso
    convertir_a_entero("hola")  # Caso con ValueError
    convertir_a_entero("5.5")   # Caso con ValueError (int() no convierte flotantes directamente)

    # --- Probando la división ---
    dividir_numeros(10, 2)      # Caso exitoso
    dividir_numeros(10, 0)      # Caso con ZeroDivisionError
    dividir_numeros(10, "dos")  # Caso con TypeError