# Ejercicio 9: sublistas_ascendentes
# Tipo de recursividad: PILA
# Estudiante: Kendall Vargas Palma

def sublistas_ascendentes(lista):
    
    if len(lista) == 0:
        return []
    
    if len(lista) == 1:
        return [[lista[0]]]
    
    resultado = sublistas_ascendentes(lista[1:])
    
    primera_sublista = resultado[0]
    
    if lista[0] < primera_sublista[0]:
        return [[lista[0]] + primera_sublista] + resultado[1:]
    
    else:
        return [[lista[0]]] + resultado


# Casos de prueba
sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]) # esperado: [[1, 2, 3], [1, 4, 5], [2]] 
sublistas_ascendentes([5, 4, 3, 2])  # esperado: [[5], [4], [3], [2]] 
sublistas_ascendentes([1, 3, 5, 7])  # esperado: [[1, 3, 5, 7]] 
sublistas_ascendentes([2, 2, 3, 1, 2])  # esperado: [[2], [2, 3], [1, 2]] 
sublistas_ascendentes([])  # esperado: []