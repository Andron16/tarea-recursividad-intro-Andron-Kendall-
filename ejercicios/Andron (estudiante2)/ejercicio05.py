#COLA

'''  
Ejercicio 5 
Dificultad: Fácil 
Desarrolle una función recursiva llamada eliminar_impares(numero) que reciba un número entero positivo y 
retorne un nuevo número formado únicamente por los dígitos pares del número original. 
Si el número no contiene dígitos pares, debe retornar 0. 
No puede convertir el número a string ni a lista. 
Casos de prueba: 
• eliminar_impares(123456) debe retornar 246 
• eliminar_impares(97531) debe retornar 0 
• eliminar_impares(80246) debe retornar 80246 
• eliminar_impares(1007) debe retornar 0
'''

def eliminar_impares(numero, res=0, exp=0):
    if numero == 0:
        return res
    else:
        if (numero % 10) % 2 == 0:
            return eliminar_impares(numero // 10, res + (numero % 10) * (10**exp), exp + 1)
        else:
            return eliminar_impares(numero // 10, res, exp)

print(eliminar_impares(123456))
print(eliminar_impares(97531))
print(eliminar_impares(80246))
print(eliminar_impares(1007))