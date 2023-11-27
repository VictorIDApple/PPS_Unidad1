# Creamos la funcion que comprueba si es binario el numero
def esBinario(strbinario):
    for caracter in strbinario:
        if caracter != '0' and caracter != '1':
            return False
    return True

# Funcion para pasar de binario a deciman
def binario_a_decimal(strbinario):

    # Si esBinario es False salta este error
    if not esBinario(strbinario):
        raise ValueError("Error: La entrada no es un número binario válido.")
    
    # Si es True el codigo sigue por aqui y pasa de binario a decimal
    numdecimal = 0
    for x, byt in enumerate(reversed(strbinario)):
        numdecimal += int(byt) * (2 ** x)

    return numdecimal

try:
    numeroBin = input("Introduce un número binario: ")
    resultado = binario_a_decimal(numeroBin)
    print(f"En formato decimal es: {resultado}")
except ValueError as f:
    print(f)