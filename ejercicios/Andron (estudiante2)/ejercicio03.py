#PILA

'''  
Ejercicio 3  
Dificultad: Fácil 
Desarrolle una función recursiva llamada mayor_lista(lista) que reciba una lista de números enteros y retorne el 
número mayor de la lista. 
No puede utilizar la función max(). 
Casos de prueba: 
• mayor_lista([4, 8, 1, 9, 3]) debe retornar 9 
• mayor_lista([10, 2, 5, 7]) debe retornar 10 
• mayor_lista([-3, -8, -1, -10]) debe retornar -1 
• mayor_lista([6]) debe retornar 6
'''

def mayor_lista(lista):
    if len(lista) == 1:
        return lista[0]
    otros_mayores = mayor_lista(lista[1:])
    if lista[0] > otros_mayores:
        return lista[0]
    return otros_mayores
    

print(mayor_lista([4, 8, 1, 9, 3]))
print(mayor_lista([10, 2, 5, 7]))
print(mayor_lista([-3, -8, -1, -10]))
print(mayor_lista([6]))

