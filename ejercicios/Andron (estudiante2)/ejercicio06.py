#COLA

'''  
Ejercicio 6 
Dificultad: Media 
Desarrolle una función recursiva llamada contar_bloques_iguales(lista) que reciba una lista de números enteros 
y retorne la cantidad de bloques de números consecutivos iguales. 
Un bloque es una secuencia continua donde el mismo número aparece una o más veces seguidas. 
Casos de prueba: 
• contar_bloques_iguales([1, 1, 2, 2, 2, 3, 1, 1]) debe retornar 4 
• Explicación: [1,1], [2,2,2], [3], [1,1] 
• contar_bloques_iguales([5, 5, 5, 5]) debe retornar 1 
• contar_bloques_iguales([1, 2, 3, 4]) debe retornar 4 
• contar_bloques_iguales([]) debe retornar 0
'''

def contar_bloques_iguales(lista, res=0):
    if lista == []:
        return 0
    if len(lista) == 1:
        return res + 1
    if lista[0] == lista[1]:
        return contar_bloques_iguales(lista[1:], res)
    return contar_bloques_iguales(lista[1:], res + 1)

print(contar_bloques_iguales([1,1,2,2,2,3,1,1]))
print(contar_bloques_iguales([5,5,5,5]))
print(contar_bloques_iguales([1,2,3,4]))
print(contar_bloques_iguales([]))