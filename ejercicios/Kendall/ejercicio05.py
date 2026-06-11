# Ejercicio 5: eliminar_impares
# Tipo de recursividad: PILA
# Estudiante: Kendall Vargas Palma

def eliminar_impares(numero):
    
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    resto = numero // 10
    
    if ultimo_digito % 2 == 0:
        
        return eliminar_impares(resto) * 10 + ultimo_digito
    
    else:
        
        return eliminar_impares(resto)


# Casos de prueba
eliminar_impares(123456) # esperado: 246 
eliminar_impares(97531) # esperado: 0 
eliminar_impares(80246) # esperado: 80246 
eliminar_impares(1007) # esperado: 0 