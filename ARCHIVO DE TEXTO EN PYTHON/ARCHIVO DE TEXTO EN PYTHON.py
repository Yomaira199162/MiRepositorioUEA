# ============================================
# Trabajo con Archivos de Texto en Python
# Autor: [Yomaira]
# Fecha: [05/10/2025]
# Descripción: Escritura y lectura de un archivo de texto
# ============================================

# --- 1. Escritura de Archivo de Texto ---

with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Recordar repasar Python todos los días.\n")
    file.write("Nota 2: Subir las tareas al repositorio de GitHub.\n")
    file.write("Nota 3: Practicar lectura y escritura de archivos en Python.\n")


# --- 2. Lectura de Archivo de Texto ---

file = open("my_notes.txt", "r")

print("Contenido del archivo 'my_notes.txt':\n")

linea = file.readline()  # Leer la primera linea
while linea:  # Mientras haya texto
    print(linea.strip())  # .strip() elimina los saltos de línea extra
    linea = file.readline()  # Leer la siguiente línea
#======================

file.close()  # Cerramos el archivo manualmente

print("\nArchivo cerrado correctamente.")