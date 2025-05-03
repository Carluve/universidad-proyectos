"""
¡Aprendiendo a Tomar Decisiones con Python!

Este archivo te enseña a usar 'if', 'elif' y 'else'.
Son como las reglas que usamos para decidir qué hacer.
"""

class TomadorDeDecisiones:
    """
    Esta clase tiene ejemplos para mostrar cómo Python toma decisiones.
    """

    def decidir_ropa_segun_clima(self, clima):
        """
        Ejemplo 1: Decidir qué ropa usar según el clima.

        Imagina que miras por la ventana.
        SI ('if') hace sol, te pones gafas de sol.
        SI NO, PERO SI ('elif') está lloviendo, coges un paraguas.
        SI NO ('else'), (significa que no hace sol ni llueve), quizás te pones una chaqueta.
        """
        print(f"\n--- Decisión 1: ¿Qué me pongo si el clima es '{clima}'? ---")

        if clima == "soleado":
            print("¡Hace sol! Ponte gafas de sol. 😎")
        elif clima == "lluvioso":
            print("¡Está lloviendo! Coge el paraguas. ☔")
        elif clima == "nublado":
            print("Está nublado, quizás una chaqueta ligera. ☁️")
        else: # Si no es ninguno de los anteriores
            print(f"Hmm, clima '{clima}'. No estoy seguro, ¡vístete como quieras! 🤔")

    def verificar_numero(self, numero):
        """
        Ejemplo 2: Comprobar si un número es positivo, negativo o cero.

        Python puede mirar un número y decidir:
        SI ('if') el número es mayor que 0, dice que es positivo.
        SI NO, PERO SI ('elif') el número es menor que 0, dice que es negativo.
        SI NO ('else'), (solo queda una opción), dice que es cero.
        """
        print(f"\n--- Decisión 2: Analizando el número {numero} ---")

        if numero > 0:
            print(f"El número {numero} es positivo. 👍")
        elif numero < 0:
            print(f"El número {numero} es negativo. 👎")
        else:
            print(f"El número {numero} es cero. 🤷")


# Punto de entrada principal del script
if __name__ == "__main__":
    # Creamos una instancia de nuestra clase
    decisiones = TomadorDeDecisiones()

    # --- Probando la decisión del clima ---
    decisiones.decidir_ropa_segun_clima("soleado")
    decisiones.decidir_ropa_segun_clima("lluvioso")
    decisiones.decidir_ropa_segun_clima("ventoso") # Un caso para el 'else'

    # --- Probando la decisión del número ---
    decisiones.verificar_numero(10)
    decisiones.verificar_numero(-5)
    decisiones.verificar_numero(0)