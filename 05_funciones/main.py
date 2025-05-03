"""
¡Creando Nuestras Propias Herramientas con Funciones en Python!

Este archivo te enseña a crear y usar funciones.
Son como recetas o mini-programas que puedes usar muchas veces.
"""

# --- Definición de Funciones ---
# Usamos 'def' para definir una función.

def saludar_a(nombre):
  """
  Esta es una función simple que recibe un nombre (parámetro)
  e imprime un saludo personalizado.
  No devuelve ningún valor, solo realiza una acción (imprimir).
  """
  print(f"¡Hola, {nombre}! Encantado de saludarte.")

def sumar_dos_numeros(num1, num2):
  """
  Esta función recibe dos números (parámetros: num1, num2).
  Calcula su suma y la devuelve usando la palabra clave 'return'.
  El valor devuelto se puede guardar en una variable o usar directamente.
  """
  resultado = num1 + num2
  return resultado

# --- Uso de las Funciones ---

# Punto de entrada principal del script
if __name__ == "__main__":
  print("--- Usando la función saludar_a ---")
  # Llamamos a la función 'saludar_a' pasándole un nombre
  saludar_a("Carlos")
  saludar_a("Maria")

  print("\n--- Usando la función sumar_dos_numeros ---")
  # Llamamos a la función 'sumar_dos_numeros' y guardamos el resultado
  suma1 = sumar_dos_numeros(5, 3)
  print(f"La suma de 5 y 3 es: {suma1}")

  # También podemos usar el resultado directamente
  print(f"La suma de 10 y 20 es: {sumar_dos_numeros(10, 20)}")

  # Podemos usar variables como parámetros
  numero_a = 7
  numero_b = 8
  suma2 = sumar_dos_numeros(numero_a, numero_b)
  print(f"La suma de {numero_a} y {numero_b} es: {suma2}")

  print("\n¡Hemos usado nuestras funciones!")