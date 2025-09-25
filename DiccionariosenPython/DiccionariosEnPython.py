#Hola!
"""
Tarea: Trabajando con Diccionarios en Python

Objetivo: Utilizar diccionarios en Python para representar
información estructurada y realizar operaciones comunes.

Instrucciones:

Crear un Diccionario:

Crea un diccionario llamado informacion_personal que contenga
información ficticia sobre una persona, incluyendo al menos las
claves "nombre", "edad", "ciudad" y "profesion".
Acceder y Modificar Valores:

Accede al valor asociado con la clave "ciudad" y modifícalo con una
ciudad diferente.
Agrega una nueva clave-valor al diccionario que represente la
"profesion" de la persona.
Verificar Existencia de Claves:

Verifica si la clave "telefono" existe en el diccionario.
Si no existe, agrégala con un número de teléfono ficticio.
Eliminar una Clave:

Elimina la clave "edad" del diccionario, ya que esa información no es
necesaria.
Imprimir el Diccionario Final:

Imprime el diccionario resultante después de realizar todas las
operaciones.
"""

# Crear un diccionario con datos ingresados por el usuario
informacion_personal = {
    "nombre": input("Ingresa tu nombre: "),
    "edad": input("Ingresa tu edad: "),
    "ciudad": input("Ingresa tu ciudad: "),
    "profesion": input("Ingresa tu profesión: ")
}

print("\nDiccionario inicial:")
print(informacion_personal)

# Acceder y modificar el valor de la clave "ciudad"
nueva_ciudad = input("\nIngresa una nueva ciudad para actualizar: ")
informacion_personal["ciudad"] = nueva_ciudad

# Agregar o actualizar la clave "profesion"
nueva_profesion = input("Ingresa una nueva profesión (o la misma si no quieres cambiarla): ")
informacion_personal["profesion"] = nueva_profesion

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    telefono = input("No se encontró teléfono. Ingresa un número ficticio: ")
    informacion_personal["telefono"] = telefono

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("\nDiccionario final después de todas las operaciones:")
print(informacion_personal)
