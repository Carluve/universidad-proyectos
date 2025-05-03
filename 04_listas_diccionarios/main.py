"""
¡Organizando Información con Listas y Diccionarios en Python!

Este archivo te muestra cómo usar listas y diccionarios.
Son como cajas especiales para guardar tus cosas ordenadas.
"""

class OrganizadorDeDatos:
    """
    Esta clase tiene ejemplos para usar listas y diccionarios.
    """

    def trabajar_con_lista_compra(self):
        """
        Ejemplo 1: Usando una Lista para la compra.

        Una lista es como una hoja de papel donde anotas cosas una debajo de otra.
        ¡Mantienen el orden! Puedes añadir más cosas al final o ver qué hay
        en una posición específica (la primera, la segunda...).
        Se escriben con corchetes: [ ]
        """
        print("\n--- Ejemplo con Listas: La Lista de la Compra ---")

        # Creamos una lista vacía
        lista_compra = []
        print(f"Lista de la compra inicial (vacía): {lista_compra}")

        # Añadimos elementos con append()
        print("Añadiendo cosas a la lista...")
        lista_compra.append("manzanas")
        lista_compra.append("leche")
        lista_compra.append("pan")
        print(f"Lista después de añadir cosas: {lista_compra}")

        # Acceder a un elemento por su posición (índice). ¡Ojo! Se empieza a contar desde 0.
        print(f"El primer elemento (índice 0) es: {lista_compra[0]}")
        print(f"El segundo elemento (índice 1) es: {lista_compra[1]}")

        # Recorrer la lista con un bucle 'for' (¡como vimos antes!)
        print("Recorriendo la lista para ver todo:")
        for item in lista_compra:
            print(f"- Necesito comprar {item}")

        print("¡Lista de la compra completa!")

    def trabajar_con_diccionario_contactos(self):
        """
        Ejemplo 2: Usando un Diccionario para guardar contactos.

        Un diccionario es como una agenda. No buscas por posición, sino por
        un nombre o 'clave' (key). A cada clave le corresponde un 'valor' (value).
        Por ejemplo, la clave 'nombre' tiene el valor 'Ana'.
        Se escriben con llaves: { } y pares clave: valor.
        """
        print("\n--- Ejemplo con Diccionarios: Agenda de Contactos ---")

        # Creamos un diccionario con información de un contacto
        contacto_ana = {
            "nombre": "Ana",
            "telefono": "123-456-789",
            "email": "ana@ejemplo.com"
        }
        print(f"Información del contacto Ana: {contacto_ana}")

        # Acceder a un valor usando su clave
        print(f"El teléfono de Ana es: {contacto_ana['telefono']}")

        # Añadir un nuevo par clave-valor
        print("Añadiendo la ciudad de Ana...")
        contacto_ana["ciudad"] = "Madrid"
        print(f"Información actualizada de Ana: {contacto_ana}")

        # Recorrer las claves y valores del diccionario
        print("Viendo toda la información de Ana:")
        for clave, valor in contacto_ana.items():
            print(f"- {clave.capitalize()}: {valor}") # capitalize() pone la primera letra en mayúscula

        print("¡Agenda de contactos revisada!")


# Punto de entrada principal del script
if __name__ == "__main__":
    # Creamos una instancia de nuestra clase
    organizador = OrganizadorDeDatos()

    # --- Probando las listas ---
    organizador.trabajar_con_lista_compra()

    # --- Probando los diccionarios ---
    organizador.trabajar_con_diccionario_contactos()