#COLA

'''  
Ejercicio 7 
Dificultad: Media 
Desarrolle una función recursiva llamada separar_por_paridad(numero) que reciba un número entero positivo y 
retorne una lista con dos números: 
El primer número debe estar formado por los dígitos pares del número original. 
El segundo número debe estar formado por los dígitos impares del número original. 
Se debe respetar el orden original de aparición de los dígitos. 
No puede convertir el número a string ni a lista. 
Casos de prueba: 
• separar_por_paridad(123456) debe retornar [246, 135] 
• separar_por_paridad(80231) debe retornar [802, 31] 
• separar_por_paridad(97531) debe retornar [0, 97531] 
• separar_por_paridad(2468) debe retornar [2468, 0]
'''
#formar numeros de manera independiente, sumarlos en forma de lista
def separar_por_paridad(numero, resPAR=0, resIMPAR=0, expPAR=0, expIMPAR=0):
    if numero == 0:
        return [resPAR] + [resIMPAR]
    if (numero % 10) % 2 == 0: #PAR
        return separar_por_paridad(numero // 10, resPAR + (numero % 10) * (10**expPAR), resIMPAR, expPAR + 1, expIMPAR)
    if (numero % 10) % 2 != 0: #IMPAR
        return separar_por_paridad(numero // 10, resPAR, resIMPAR + (numero % 10) * (10**expIMPAR), expPAR, expIMPAR + 1)  

print(separar_por_paridad(123456))
print(separar_por_paridad(80231))
print(separar_por_paridad(97531))
print(separar_por_paridad(2468))
