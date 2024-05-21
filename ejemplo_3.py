# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    csvfile = open('alturas.csv')
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    personas = list(csv.DictReader(csvfile))

    # Una vez leido los datos, cerrar el archivo
    csvfile.close()

    cantidad = 0
    totalAltura = 0
    
    for persona in personas:
            if persona["genero"] == genero: 
                cantidad += 1
                totalAltura += float(persona["altura"])

    promedio = totalAltura / cantidad

    print(f"El promedio de la altura entre el genero {genero} es {promedio}")        
   

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("femenino")
