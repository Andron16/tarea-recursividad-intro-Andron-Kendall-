# Ejercicio 6: contar_bloques_iguales
# Tipo de recursividad: PILA
# Estudiante: Kendall Vargas Palma

def contar_bloques_iguales(lista):
    
    if len(lista) == 0:
        return 0
    
    if len(lista) == 1:
        return 1
    
    if lista[0] == lista[1]:
        return contar_bloques_iguales(lista[1:])
    
    else:
        return 1 + contar_bloques_iguales(lista[1:])




# Casos de prueba: 
contar_bloques_iguales([1, 1, 2, 2, 2, 3, 1, 1]) # esperado: 4 
contar_bloques_iguales([5, 5, 5, 5]) # esperado: 1 
contar_bloques_iguales([1, 2, 3, 4]) # esperado: 4 
contar_bloques_iguales([]) # esperado: 0 