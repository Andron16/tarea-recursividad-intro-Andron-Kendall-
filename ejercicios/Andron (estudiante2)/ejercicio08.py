#PILA

''' 
Ejercicio 8 
Dificultad: Media 
Desarrolle una función recursiva llamada detectar_valles(lista) que reciba una lista de números enteros y retorne 
una lista de listas con las secuencias de tres elementos consecutivos donde el elemento central sea menor que el 
anterior y menor que el siguiente. 
A estas secuencias se les llamará valles locales. 
Casos de prueba: 
• detectar_valles([5, 1, 6, 3, 8, 2, 7]) debe retornar [[5, 1, 6], [6, 3, 8], [8, 2, 7]] 
• detectar_valles([1, 2, 3, 4, 5]) debe retornar [] 
• detectar_valles([9, 4, 8, 2, 6]) debe retornar [[9, 4, 8], [8, 2, 6]] 
• detectar_valles([3, 1]) debe retornar []
'''

def detectar_valles(lista):
    if len(lista) < 3:
        return []
    if lista[1] < lista[0] and lista[1] < lista[2]:
        return [[lista[0], lista[1], lista[2]]] + detectar_valles(lista[1:])
    return detectar_valles(lista[1:])

print(detectar_valles([5, 1, 6, 3, 8, 2, 7]))
print(detectar_valles([1, 2, 3, 4, 5]))
print(detectar_valles([9, 4, 8, 2, 6]))
print(detectar_valles([3, 1]))