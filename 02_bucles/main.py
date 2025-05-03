"""
¡Aprendiendo sobre Bucles con Python!

Este archivo te enseñará cómo usar los bucles 'for' y 'while'.
¡Son como juegos de repetición!
"""

class JuegosDeRepeticion:
    """
    Esta clase tiene juegos (métodos) para mostrar cómo funcionan los bucles.
    """

    def contar_juguetes_for(self, lista_de_juguetes):
        """
        Juego 1: Contar juguetes con el bucle 'for'.

        Imagina que tienes una caja de juguetes (eso es la 'lista_de_juguetes').
        El bucle 'for' es como sacar cada juguete de la caja, uno por uno,
        y decir su nombre en voz alta. Repite la acción de "decir nombre"
        para CADA juguete que haya en la caja.
        """
        print("\n--- Juego del Bucle For: Contando Juguetes ---")
        print(f"Tenemos estos juguetes en la caja: {lista_de_juguetes}")
        print("¡Vamos a sacarlos uno por uno!")

        # Este es el bucle 'for'.
        # 'juguete' será el nombre de cada ítem en 'lista_de_juguetes' en cada repetición.
        for juguete in lista_de_juguetes:
            print(f"¡He sacado un {juguete}!")

        print("¡Hemos sacado todos los juguetes de la caja!")

    def esperar_hasta_numero_while(self, numero_limite):
        """
        Juego 2: Esperar hasta un número con el bucle 'while'.

        Imagina que estás contando números hasta llegar a uno especial ('numero_limite').
        El bucle 'while' es como decir: "MIENTRAS (while) el número que tengo
        sea MÁS PEQUEÑO que el número especial, seguiré contando y sumando 1".
        Solo se detiene CUANDO el número ya NO es más pequeño que el límite.
        """
        print(f"\n--- Juego del Bucle While: Contando hasta {numero_limite} ---")
        contador = 0 # Empezamos a contar desde 0
        print(f"Empezamos a contar desde {contador}")

        # Este es el bucle 'while'.
        # Se repetirá MIENTRAS la condición (contador < numero_limite) sea Verdadera.
        while contador < numero_limite:
            print(f"El contador ahora es {contador}. ¡Aún no llegamos a {numero_limite}!")
            contador = contador + 1 # Sumamos 1 al contador en cada repetición

        # Cuando la condición (contador < numero_limite) se vuelve Falsa, el bucle termina.
        print(f"¡Ahora el contador es {contador}! Ya no es menor que {numero_limite}, ¡así que paramos!")
        print("¡Hemos terminado de contar!")


# Punto de entrada principal del script
if __name__ == "__main__":
    # Creamos una instancia de nuestra clase de juegos
    juegos = JuegosDeRepeticion()

    # --- Probando el bucle FOR ---
    # Creamos una lista de juguetes de ejemplo
    caja_de_juguetes = ["coche", "muñeca", "pelota", "robot"]
    # Llamamos al método que usa el bucle 'for'
    juegos.contar_juguetes_for(caja_de_juguetes)

    # --- Probando el bucle WHILE ---
    # Definimos hasta qué número queremos contar
    numero_magico = 5
    # Llamamos al método que usa el bucle 'while'
    juegos.esperar_hasta_numero_while(numero_magico)