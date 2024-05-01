"""
Asigna a cada letra minúscula un valor, desde 1 para la 'a' hasta 26 para la 'z'. 
Crea una función que pida al usuario una cadena de letras minúsculas y responde la suma de los valores de las letras en la cadena. (Ejemplo: hola = 8 + 15 + 12 + 1 = 36). 
Si el usuario te da un número o una letra mayúscula, pídele que lo cambie (Input: Hola. Output: Cambia a minúscula la letra “H” en la posición 1. Input: int2. Output: Cambia el número en la posición 4 por una letra minúscula).
"""


def valor_letras():
    import string
    
    # Crea un diccionario para mapear cada letra con el valor que le corresponde
    letras = string.ascii_lowercase
    valores = {letra: idx + 1 for idx, letra in enumerate(letras)}
    
    # Le pide al usuario que ingrese una palabra
    cadena = input("Ingresa una cadena de letras minúsculas: ")
    
    # Valida si la cadena tiene caracteres que no sean permitidos
    errores = []
    for idx, char in enumerate(cadena):
        if char not in valores:
            if char.isdigit():
                errores.append(f'Cambia el número "{char}" en la posición {idx + 1} por una letra minúscula.')
            else:
                errores.append(f'Cambia a minúscula la letra "{char}" en la posición {idx + 1}.')
    
    # En caso de haber errores, mostrarlos y no calcular la suma
    if errores:
        for error in errores:
            print(error)
    else:
        # Calcula la suma de los valores de las letras
        suma = sum(valores[char] for char in cadena)
        print(f"La suma de los valores de las letras en '{cadena}' es: {suma}")

# Aqui llamas a la función
valor_letras()
