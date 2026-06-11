# Ejercicio 3: mayor_lista
# Tipo de recursividad: COLA
# Estudiante: Kendall Vargas Palma

def mayor_lista(lista, mayor_actual=None):
    
    if len(lista) == 0:
        return mayor_actual
    
    
    if mayor_actual is None:
        return mayor_lista(lista[1:], lista[0])
    
    
    if lista[0] > mayor_actual:
        return mayor_lista(lista[1:], lista[0])
    else:
        return mayor_lista(lista[1:], mayor_actual)


# Casos de prueba: 
mayor_lista([4, 8, 1, 9, 3])   # esperado: 9 
mayor_lista([10, 2, 5, 7])     # esperado: 10 
mayor_lista([-3, -8, -1, -10]) # esperado: -1 
mayor_lista([6])               # esperado: 6 


    #   git commit -m "Se resuelve ejercicio 3 (mayor_lista) con recursividad de cola"