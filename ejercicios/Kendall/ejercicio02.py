# Ejercicio 2: contar_pares
# Tipo de recursividad: COLA
# Estudiante: Kendall Vargas Palma


def contar_pares(numero, acumulador=0):
    
    if numero == 0:
        return acumulador
    
    
    ultimo_digito = numero % 10
    
    
    if ultimo_digito % 2 == 0:
        return contar_pares(numero // 10, acumulador + 1)
    else:
        return contar_pares(numero // 10, acumulador)