"""
¡Profundizando en la Programación Orientada a Objetos (OOP) en Python!

Este archivo muestra cómo crear clases más detalladas con atributos (datos)
y métodos (comportamientos). Modelaremos un 'Coche'.
"""

class Coche:
    """
    Representa un coche con sus características y acciones.
    """
    # Atributo de clase (compartido por todos los coches, si no se modifica)
    numero_ruedas = 4

    def __init__(self, marca, modelo, color):
        """
        El constructor (__init__) se llama al crear un nuevo objeto Coche.
        Inicializa los atributos específicos de esta instancia (este coche).
        """
        print(f"Creando un nuevo coche: {marca} {modelo} {color}")
        # Atributos de instancia (propios de cada coche)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_actual = 0 # El coche empieza parado
        self.esta_arrancado = False # El coche empieza apagado

    # --- Métodos (Comportamientos del coche) ---

    def arrancar(self):
        """Enciende el motor del coche si estaba apagado."""
        if not self.esta_arrancado:
            self.esta_arrancado = True
            print(f"¡El {self.marca} {self.modelo} ha arrancado! Brum brum...")
        else:
            print(f"El {self.marca} {self.modelo} ya estaba arrancado.")

    def apagar(self):
        """Apaga el motor del coche si estaba encendido y parado."""
        if self.esta_arrancado:
            if self.velocidad_actual == 0:
                self.esta_arrancado = False
                print(f"El {self.marca} {self.modelo} se ha apagado.")
            else:
                print(f"¡No puedes apagar el {self.marca} {self.modelo} en movimiento!")
        else:
            print(f"El {self.marca} {self.modelo} ya estaba apagado.")

    def acelerar(self, incremento):
        """Aumenta la velocidad del coche si está arrancado."""
        if self.esta_arrancado:
            if incremento > 0:
                self.velocidad_actual += incremento
                print(f"El {self.marca} {self.modelo} acelera. Velocidad actual: {self.velocidad_actual} km/h")
            else:
                print("El incremento de velocidad debe ser positivo.")
        else:
            print(f"Necesitas arrancar el {self.marca} {self.modelo} primero.")

    def frenar(self, decremento):
        """Disminuye la velocidad del coche."""
        if self.velocidad_actual > 0:
            if decremento > 0:
                # Asegura que la velocidad no sea negativa
                self.velocidad_actual = max(0, self.velocidad_actual - decremento)
                print(f"El {self.marca} {self.modelo} frena. Velocidad actual: {self.velocidad_actual} km/h")
            else:
                print("El decremento de velocidad debe ser positivo.")
        else:
            print(f"El {self.marca} {self.modelo} ya está parado.")

    def mostrar_info(self):
        """Muestra la información actual del coche."""
        print("\n--- Información del Coche ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Ruedas: {self.numero_ruedas}")
        estado = "Arrancado" if self.esta_arrancado else "Apagado"
        print(f"Estado: {estado}")
        print(f"Velocidad: {self.velocidad_actual} km/h")
        print("---------------------------")


# Punto de entrada principal del script
if __name__ == "__main__":
    # Creamos instancias (objetos) de la clase Coche
    mi_coche = Coche("Seat", "Ibiza", "Rojo")
    coche_vecino = Coche("Ford", "Focus", "Azul")

    # Interactuamos con los objetos
    mi_coche.mostrar_info()
    coche_vecino.mostrar_info()

    print("\n--- Acciones con mi coche ---")
    mi_coche.arrancar()
    mi_coche.acelerar(50)
    mi_coche.acelerar(30)
    mi_coche.frenar(20)
    mi_coche.mostrar_info()
    mi_coche.apagar() # Intentamos apagar en movimiento
    mi_coche.frenar(60) # Frenamos hasta parar
    mi_coche.apagar() # Ahora sí podemos apagar
    mi_coche.mostrar_info()

    print("\n--- Acciones con coche vecino ---")
    coche_vecino.acelerar(10) # Intentamos acelerar sin arrancar
    coche_vecino.arrancar()
    coche_vecino.acelerar(20)
    coche_vecino.mostrar_info()