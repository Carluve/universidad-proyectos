"""
¡Usando Módulos para Organizar y Reutilizar Código!

Este archivo importa y usa código de nuestro propio 'mi_modulo.py'
y también del módulo 'math' que viene con Python.
"""

# --- Importando nuestro propio módulo ---
# Python buscará un archivo llamado mi_modulo.py en la misma carpeta (o en otras carpetas configuradas)
print("Importando 'mi_modulo'...")
import mi_modulo
print("¡'mi_modulo' importado!")

# --- Importando un módulo incorporado de Python ---
print("\nImportando el módulo 'math'...")
import math
print("¡Módulo 'math' importado!")


# --- Usando el código importado ---

# Punto de entrada principal del script
if __name__ == "__main__":
    print("\n--- Usando nuestro 'mi_modulo' ---")

    # Usamos la función del módulo. Necesitamos poner 'mi_modulo.' delante.
    resultado = mi_modulo.multiplicar_por_dos(7)
    print(f"Resultado de multiplicar 7 * 2 usando mi_modulo: {resultado}")

    # Usamos la variable del módulo. También necesita 'mi_modulo.' delante.
    print(f"El mensaje secreto de mi_modulo es: {mi_modulo.MENSAJE_SECRETO}")


    print("\n--- Usando el módulo 'math' ---")

    # Usamos una función del módulo 'math' (sqrt calcula la raíz cuadrada)
    numero = 16
    raiz_cuadrada = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

    # Usamos una constante del módulo 'math' (pi)
    print(f"El valor de Pi según el módulo math es: {math.pi}")

    print("\n¡Hemos usado código de diferentes módulos!")