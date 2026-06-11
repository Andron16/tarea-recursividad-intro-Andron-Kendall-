#COLA

'''  
Ejercicio 4 
Dificultad: Fácil 
Desarrolle una función recursiva llamada invertir_numero(numero) que reciba un número entero positivo y 
retorne el número invertido. 
No puede convertir el número a string ni a lista. 
Casos de prueba: 
• invertir_numero(1234) debe retornar 4321 
• invertir_numero(900) debe retornar 9 
• invertir_numero(5071) debe retornar 1705 
• invertir_numero(8) debe retornar 8
'''
def len_num(num):
    if num == 0:
        return 1
    contador = 0
    while num != 0:
        contador += 1
        num //= 10
    return contador

def invertir_numero(numero, res=0):
    numero = abs(numero)
    exp = len_num(numero) - 1
    if numero == 0:
        return res
    else:
        return invertir_numero(numero // 10, res + ((numero % 10) * (10**exp)))
    
print(invertir_numero(1234))
print(invertir_numero(900))
print(invertir_numero(5071))
print(invertir_numero(8))
