# Ejercicio 7: separar_por_paridad
# Tipo de recursividad: PILA
# Estudiante: Kendall Vargas Palma

def separar_por_paridad(numero):
    
    if numero == 0:
        return [0, 0]
    
    ultimo_digito = numero % 10
    resto = numero // 10
    
    
    resultado = separar_por_paridad(resto)
    
    if ultimo_digito % 2 == 0:
        return [resultado[0] * 10 + ultimo_digito, resultado[1]]
    
    else:
        return [resultado[0], resultado[1] * 10 + ultimo_digito]

# Casos de prueba
separar_por_paridad(123456) # esperado: [246, 135] 
separar_por_paridad(80231) # esperado: [802, 31] 
separar_por_paridad(97531) # esperado: [0, 97531] 
separar_por_paridad(2468) # esperado: [2468, 0] 