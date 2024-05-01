"""
1. Extraer la información del csv Prueba_Promociones
2. ⁠Generar un código donde el usuario pueda ingresar las siguientes variables
- fecha inicio (convertir a datetime)
- ⁠fecha fin (convertir a datetime)
- ⁠categoría (validar que sea string)
- ⁠uso (validar que sea string)
- ⁠sku (no permitir al usuario avanzar si no ingreso un valor string en el campo de SKU)
- ⁠% (validar que sea número decimal)
- ⁠inventario inicial (validar que sea entero)

"""

import pandas as pd
from datetime import datetime

def cargar_datos(ruta):
    # Aqui se carga el archivo CSV
    datos = pd.read_csv(ruta)
    # Imprime los nombres de las columnas para verificar
    print("Columnas disponibles:", datos.columns)
   
    if 'fecha' in datos.columns:
        datos['fecha'] = pd.to_datetime(datos['fecha'])
        datos['semana'] = datos['fecha'].dt.isocalendar().week
    else:
        print("La columna 'fecha' no se encuentra en el archivo.")
    return datos

def solicitar_datos():
    fecha_inicio = input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
    fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y") if fecha_inicio else None
    
    fecha_fin = input("Ingrese la fecha fin (dd-mm-aaaa): ")
    fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y") if fecha_fin else None

    categoria = input("Ingrese la categoría: ")
    uso = input("Ingrese el uso: ")
    
    sku = input("Ingrese el SKU: ")
    while not sku:
        print("Debe ingresar un valor para el SKU.")
        sku = input("Ingrese el SKU: ")
    
    porcentaje = float(input("Ingrese el porcentaje de crecimiento (%): "))
    inventario_inicial = int(input("Ingrese el inventario inicial: "))
    
    return fecha_inicio, fecha_fin, categoria, uso, sku, porcentaje, inventario_inicial

def aplicar_crecimiento(datos, fecha_inicio, fecha_fin, categoria, uso, porcentaje):
    
    if 'modelo' in datos.columns:
        condiciones = (datos['modelo'] != 'real')
    else:
        print("La columna 'modelo' no se encuentra en el archivo.")
        return datos
    
    if uso:
        condiciones &= (datos['uso'] == uso)
    if categoria:
        condiciones &= (datos['categoria'] == categoria)
    if fecha_inicio:
        condiciones &= (datos['fecha'] >= fecha_inicio)
    if fecha_fin:
        condiciones &= (datos['fecha'] <= fecha_fin)

    datos.loc[condiciones, 'piezas'] *= (1 + porcentaje / 100)
    return datos

def calcular_consumo_inventario(datos, sku, inventario_inicial):
    datos_sku = datos[datos['sku'] == sku]
    datos_sku = datos_sku.sort_values('fecha')
    inventario = inventario_inicial
    for index, row in datos_sku.iterrows():
        if 'modelo' in datos.columns and row['modelo'] != 'real':
            inventario -= row['piezas']
            if inventario < 0:
                print(f"El inventario se vuelve negativo el {row['fecha']}")
                break
    return datos_sku

# Esta es la ruta del archivo
ruta_archivo = r'C:\Users\JUANCARLOSJIMENEZMIL\Downloads\Examen IBSO_1_24-4-2024\Prueba_Promociones.csv'
datos = cargar_datos(ruta_archivo)

fecha_inicio, fecha_fin, categoria, uso, sku, porcentaje, inventario_inicial = solicitar_datos()
datos_modificados = aplicar_crecimiento(datos, fecha_inicio, fecha_fin, categoria, uso, porcentaje)
datos_filtrados = calcular_consumo_inventario(datos_modificados, sku, inventario_inicial)
