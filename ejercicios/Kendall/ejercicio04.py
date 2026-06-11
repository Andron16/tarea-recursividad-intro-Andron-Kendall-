# Ejercicio 4: invertir_numero
# Tipo de recursividad: PILA
# Estudiante: Kendall Vargas Palma

def invertir_numero(numero, multiplicador=1):

    if numero < 10:
        return numero * multiplicador
    
    
    ultimo_digito = numero % 10

    
    return ultimo_digito * (10 ** _contar_digitos(numero // 10)) + invertir_numero(numero // 10)


def _contar_digitos(numero):
    if numero < 10:
        return 1
    return 1 + _contar_digitos(numero // 10)


# Casos de prueba 
invertir_numero(1234) # esperado: 4321 
invertir_numero(900) # esperado: 9 
invertir_numero(5071) # esperado: 1705 
invertir_numero(8) # esperado: 8