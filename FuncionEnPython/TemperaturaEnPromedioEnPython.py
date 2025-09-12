
temperatura = [
    [  # Ciudad 1 (Cuenca)
        [1, 2, 3],     # Día 1 (3 semanas)
        [4, 5, 6],
        [7, 8, 9]
    ],
    [  # Ciudad 2 (Guayaquil)
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
]

ciudades = ["Cuenca", "Guayaquil"]
semanas = ["Semana1", "Semana2", "Semana3"]

def calcularPromedioTemperaturas(datos, ciudades, semanas):
    for i, ciudad in enumerate(datos):  # recorre ciudades
        print(f"Promedios para {ciudades[i]}:")
        for s in range(len(semanas)):   # recorre semanas
            suma = sum(ciudad[d][s] for d in range(len(ciudad)))  # suma días
            promedio = suma / len(ciudad)  # divide entre número de días
            print(f"  {semanas[s]}: {promedio:.2f}ºC")
        print()

calcularPromedioTemperaturas(temperatura, ciudades, semanas)
