"""
¡Explorando Bibliotecas Estándar de Python!

Este archivo muestra cómo usar módulos útiles que vienen incluidos
con Python, como 'random' y 'datetime'.
"""

# Importamos los módulos que vamos a usar
import random
import datetime

def generar_numero_loteria(minimo, maximo, cantidad):
    """
    Genera una lista de números aleatorios únicos para una lotería simple.
    Usa el módulo 'random'.
    """
    print(f"\n--- Generando {cantidad} números de lotería entre {minimo} y {maximo} ---")
    if cantidad > (maximo - minimo + 1):
        print("¡Error! No se pueden generar más números únicos que el rango disponible.")
        return []

    # random.sample() elige una cantidad de elementos únicos de una secuencia
    numeros_ganadores = random.sample(range(minimo, maximo + 1), cantidad)
    numeros_ganadores.sort() # Los ordenamos para que sea más fácil leerlos
    print(f"¡Los números de la suerte son: {numeros_ganadores}!")
    return numeros_ganadores

def mostrar_fecha_hora_actual():
    """
    Muestra la fecha y hora actuales.
    Usa el módulo 'datetime'.
    """
    print("\n--- Obteniendo la fecha y hora actual ---")
    # datetime.datetime.now() nos da la fecha y hora actuales
    ahora = datetime.datetime.now()
    print(f"Fecha y hora completa: {ahora}")

    # Podemos formatear la fecha y hora para mostrarla como queramos
    # %Y: Año con 4 dígitos, %m: Mes (01-12), %d: Día (01-31)
    # %H: Hora (00-23), %M: Minuto (00-59), %S: Segundo (00-59)
    formato_bonito = ahora.strftime("%d/%m/%Y a las %H:%M:%S")
    print(f"Formateado: {formato_bonito}")

    print(f"Solo la fecha: {ahora.date()}")
    print(f"Solo la hora: {ahora.time()}")
    print(f"Año actual: {ahora.year}")
    print(f"Día de la semana (0=Lunes, 6=Domingo): {ahora.weekday()}")


# Punto de entrada principal del script
if __name__ == "__main__":
    # --- Usando el módulo random ---
    generar_numero_loteria(1, 49, 6) # Lotería típica 6 de 49

    # --- Usando el módulo datetime ---
    mostrar_fecha_hora_actual()

    print("\n¡Hemos usado módulos estándar de Python!")