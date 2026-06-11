# Ejercicio 8: detectar_valles
# Tipo de recursividad: COLA
# Estudiante: Kendall Vargas Palma

def detectar_valles(lista, acumulador=None):

    if acumulador is None:
        acumulador = []
    
    if len(lista) < 3:
        return acumulador
    

    if lista[1] < lista[0] and lista[1] < lista[2]:
        nuevo_valle = [lista[0], lista[1], lista[2]]
        return detectar_valles(lista[1:], acumulador + [nuevo_valle])
    
    else:
        return detectar_valles(lista[1:], acumulador)


# Casos de prueba
detectar_valles([5, 1, 6, 3, 8, 2, 7]) # esperado: [[5, 1, 6], [6, 3, 8], [8, 2, 7]] 
detectar_valles([1, 2, 3, 4, 5]) # esperado: [] 
detectar_valles([9, 4, 8, 2, 6]) # esperado: [[9, 4, 8], [8, 2, 6]] 
detectar_valles([3, 1]) # esperado: [] 