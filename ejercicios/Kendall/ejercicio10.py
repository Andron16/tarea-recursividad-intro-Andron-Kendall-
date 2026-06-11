# Ejercicio 10: comprimir_repetidos
# Tipo de recursividad: COLA
# Estudiante: Kendall Vargas Palma

def comprimir_repetidos(lista, acumulador=None):
    
    if acumulador is None:
        acumulador = []
    
    if len(lista) == 0:
        return acumulador
    
    if len(acumulador) == 0 or acumulador[-1][0] != lista[0]:
        nuevo_acumulador = acumulador + [[lista[0], 1]]
        return comprimir_repetidos(lista[1:], nuevo_acumulador)
    
    else:
        ultimo_numero = acumulador[-1][0]
        nueva_cantidad = acumulador[-1][1] + 1
        nuevo_acumulador = acumulador[:-1] + [[ultimo_numero, nueva_cantidad]]
        
        return comprimir_repetidos(lista[1:], nuevo_acumulador)


# Casos de prueba
comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]) # esperado: [[1, 3], [2, 2], [3, 1], [1, 2]] 
comprimir_repetidos([5, 5, 5, 5]) # esperado: [[5, 4]] 
comprimir_repetidos([1, 2, 3, 4]) # esperado: [[1, 1], [2, 1], [3, 1], [4, 1]] 
comprimir_repetidos([]) # esperado: [] 







