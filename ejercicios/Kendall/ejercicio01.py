# Ejercicio 1: sumar_digitos
# Tipo de recursividad: COLA
# Estudiante: Kendall Vargas Palma

def sumar_digitos(num):
    return sumar_digitos_aux(num, 0)

def sumar_digitos_aux(num, acumulador):
    if num == 0:
        return acumulador
    return sumar_digitos_aux(num // 10, acumulador + num % 10)


# Casos de prueba
print(sumar_digitos(1234))   # esperado: 10
print(sumar_digitos(9001))   # esperado: 10
print(sumar_digitos(7))      # esperado: 7
print(sumar_digitos(0))      # esperado: 0