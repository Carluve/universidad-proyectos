"""
Este es nuestro primer módulo personalizado.
Contiene herramientas (funciones y variables) que podemos usar en otros archivos.
"""

print("-> El módulo 'mi_modulo.py' se está cargando...")

MENSAJE_SECRETO = "¡Python es genial!"

def multiplicar_por_dos(numero):
  """
  Una función simple que multiplica un número por 2.
  """
  print(f"    (Dentro de mi_modulo: multiplicando {numero} * 2)")
  return numero * 2