#COLA

''' 
Ejercicio 9 
Dificultad: Alta 
Desarrolle una función recursiva llamada sublistas_ascendentes(lista) que reciba una lista de números enteros y 
retorne una lista de sublistas. 
Cada sublista debe contener una secuencia de números consecutivos estrictamente ascendentes. 
Cuando el siguiente número sea menor o igual que el anterior, se debe iniciar una nueva sublista. 
No puede usar ciclos. 
Casos de prueba: 
• sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]) debe retornar [[1, 2, 3], [1, 4, 5], [2]] 
• sublistas_ascendentes([5, 4, 3, 2]) debe retornar [[5], [4], [3], [2]] 
• sublistas_ascendentes([1, 3, 5, 7]) debe retornar [[1, 3, 5, 7]] 
• sublistas_ascendentes([2, 2, 3, 1, 2]) debe retornar [[2], [2, 3], [1, 2]] 
• sublistas_ascendentes([]) debe retornar []
'''

def sublistas_ascendentes(lista, actual=[], res=[]):
    if lista == []:
        return res + [actual]
    if actual == [] or lista[0] > actual[-1]:
        return sublistas_ascendentes(lista[1:], actual + [lista[0]], res)
    return sublistas_ascendentes(lista[1:], [lista[0]], res + [actual])

print(sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]))
print(sublistas_ascendentes([5, 4, 3, 2]))
print(sublistas_ascendentes([1, 3, 5, 7]))
print(sublistas_ascendentes([2, 2, 3, 1, 2]))
print(sublistas_ascendentes([]))