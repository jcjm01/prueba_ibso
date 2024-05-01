"""
Ejercicio 1: 
1.	Crea un diccionario llamado datos_climaticos donde cada clave es el nombre de una ciudad y el valor es una lista de temperaturas (en grados Celsius) registradas a lo largo de una semana.
2.	Para cada ciudad, calcula la temperatura promedio, la temperatura máxima y la mínima de la semana.
3.	Determina cuál fue la ciudad con la temperatura promedio más alta y la más baja durante la semana.
"""

# 1: Crear diccionario con los datos del clima.

datos_climaticos = {
    'CDMX': [22, 24, 23, 25, 26, 27, 24],
    'Queretaro': [20, 22, 21, 23, 24, 25, 26],
    'Oaxaca': [25, 27, 26, 28, 29, 30, 28],
    'Toluca': [28, 30, 31, 33, 34, 32, 31]
}

# 2: Este ciclo calcula temperatura promedio, máxima y mínima para cada ciudad

resultados = {}

for ciudad, temperaturas in datos_climaticos.items():
    promedio = sum(temperaturas) / len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    resultados[ciudad] = (promedio, maxima, minima)

# Imprime en pantalla los resultados de calcular la temperatura promedio,la máxima y la mínima
for ciudad, (promedio, maxima, minima) in resultados.items():
    print(f'{ciudad}: Promedio = {promedio:.2f}, Máxima = {maxima}, Mínima = {minima}')



# 3:Encontrar la ciudad con la temperatura promedio más alta y más baja

max_temp_promedio = min_temp_promedio = None
for ciudad, (promedio, _, _) in resultados.items():
    if max_temp_promedio is None or promedio > max_temp_promedio[1]:
        max_temp_promedio = (ciudad, promedio)
    if min_temp_promedio is None or promedio < min_temp_promedio[1]:
        min_temp_promedio = (ciudad, promedio)

print(f'\nCiudad con la temperatura promedio más alta: {max_temp_promedio[0]} ({max_temp_promedio[1]:.2f} °C)')
print(f'Ciudad con la temperatura promedio más baja: {min_temp_promedio[0]} ({min_temp_promedio[1]:.2f} °C)')
