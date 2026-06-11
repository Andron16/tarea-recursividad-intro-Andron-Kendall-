#PILA

'''  
Ejercicio 10 
Dificultad: Alta 
Desarrolle una función recursiva llamada comprimir_repetidos(lista) que reciba una lista de números enteros y 
retorne una lista de listas, donde cada sublista contenga el número y la cantidad de veces consecutivas que 
aparece. 
Casos de prueba: 
• comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]) debe retornar [[1, 3], [2, 2], [3, 1], [1, 2]] 
• comprimir_repetidos([5, 5, 5, 5]) debe retornar [[5, 4]] 
• comprimir_repetidos([1, 2, 3, 4]) debe retornar [[1, 1], [2, 1], [3, 1], [4, 1]] 
• comprimir_repetidos([]) debe retornar []
'''

def comprimir_repetidos(lista):
    if lista == []:
        return []
    resto = comprimir_repetidos(lista[1:])
    if resto != [] and resto[0][0] == lista[0]:
        return [[lista[0], resto[0][1] + 1]] + resto[1:]
    return [[lista[0], 1]] + resto

print(comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]))
print(comprimir_repetidos([5, 5, 5, 5]))
print(comprimir_repetidos([1, 2, 3, 4]))
print(comprimir_repetidos([]))