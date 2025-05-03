"""
Documentación Inicial de Python

Este archivo sirve como punto de partida para proyectos en Python.
A continuación, se describen algunos conceptos básicos y útiles.

Variables:
En Python, las variables se crean cuando les asignas un valor por primera vez.
No necesitas declarar el tipo de variable explícitamente.
Ejemplo:
    mensaje = "Hola"  # Variable de tipo string
    numero = 10      # Variable de tipo integer
    precio = 99.99   # Variable de tipo float
    es_valido = True # Variable de tipo boolean

Parámetros (en funciones/métodos):
Los parámetros son variables listadas dentro de los paréntesis en la definición de una función o método.
Permiten pasar información a la función/método.
Ejemplo:
    def saludar(nombre):  # 'nombre' es un parámetro
        print(f"Hola, {nombre}")

Temas Útiles en Python:
- Tipos de Datos: int, float, str, bool, list, tuple, dict, set.
- Estructuras de Control: if/elif/else, for, while.
- Funciones: Definición con 'def', parámetros, valor de retorno con 'return'.
- Clases y Objetos: Programación Orientada a Objetos (POO) con 'class'.
- Módulos y Paquetes: Importar código de otros archivos ('import').
- Manejo de Errores: Bloques 'try'/'except'.
- Entornos Virtuales: Aislar dependencias del proyecto (venv, conda).
- Gestores de Paquetes: pip para instalar librerías externas.
"""

class Saludo:
    """
    Una clase simple para demostrar el concepto de 'Hello World'.
    """
    def __init__(self, texto="Hello World"):
        """
        Constructor de la clase. Inicializa el texto a mostrar.
        """
        self.texto_saludo = texto

    def mostrar_saludo(self):
        """
        Método que imprime el saludo almacenado.
        """
        print(self.texto_saludo)

# Punto de entrada principal del script
if __name__ == "__main__":
    # Crear una instancia de la clase Saludo
    mi_saludo = Saludo()
    # Llamar al método para mostrar el saludo
    mi_saludo.mostrar_saludo()

    # Ejemplo con un saludo personalizado
    saludo_personalizado = Saludo("¡Hola, Python!")
    saludo_personalizado.mostrar_saludo()