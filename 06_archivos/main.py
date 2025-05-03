"""
¡Hablando con Archivos en Python!

Este archivo te enseña cómo guardar información en archivos
y cómo leerla después.
"""

# Nombre del archivo con el que vamos a trabajar
NOMBRE_ARCHIVO = "tareas.txt"

def escribir_tareas_en_archivo(tareas):
    """
    Esta función recibe una lista de tareas y las escribe
    en un archivo de texto, una tarea por línea.
    """
    print(f"\n--- Escribiendo tareas en el archivo '{NOMBRE_ARCHIVO}' ---")
    # 'with open(...)' es la forma segura de trabajar con archivos.
    # Se asegura de que el archivo se cierre correctamente al final.
    # 'w' significa que abrimos el archivo en modo escritura (write).
    # Si el archivo ya existe, ¡se borrará su contenido anterior!
    try:
        with open(NOMBRE_ARCHIVO, 'w') as archivo:
            for tarea in tareas:
                # Escribimos cada tarea seguida de un salto de línea '\n'
                archivo.write(tarea + "\n")
        print("¡Tareas escritas correctamente!")
    except Exception as e:
        print(f"¡Oh no! Ocurrió un error al escribir el archivo: {e}")


def leer_tareas_de_archivo():
    """
    Esta función lee las tareas del archivo de texto
    y las muestra en pantalla.
    """
    print(f"\n--- Leyendo tareas del archivo '{NOMBRE_ARCHIVO}' ---")
    try:
        # 'r' significa que abrimos el archivo en modo lectura (read).
        with open(NOMBRE_ARCHIVO, 'r') as archivo:
            print("Contenido del archivo:")
            # Podemos leer todo el contenido de golpe con read()
            # o línea por línea con un bucle for:
            for linea in archivo:
                # .strip() quita espacios en blanco y saltos de línea del principio/final
                print(f"- {linea.strip()}")
        print("¡Archivo leído correctamente!")
    except FileNotFoundError:
        print(f"¡Error! El archivo '{NOMBRE_ARCHIVO}' no se encontró. ¿Lo escribiste primero?")
    except Exception as e:
        print(f"¡Oh no! Ocurrió un error al leer el archivo: {e}")


# Punto de entrada principal del script
if __name__ == "__main__":
    # Lista de tareas que queremos guardar
    mis_tareas = [
        "Comprar leche",
        "Estudiar Python",
        "Pasear al perro",
        "Llamar a mamá"
    ]

    # 1. Escribimos las tareas en el archivo
    escribir_tareas_en_archivo(mis_tareas)

    # 2. Leemos las tareas del archivo que acabamos de crear
    leer_tareas_de_archivo()

    # Intenta ejecutar de nuevo. Verás que el archivo se sobrescribe.
    # Si quieres añadir sin borrar, usa el modo 'a' (append) en lugar de 'w'.