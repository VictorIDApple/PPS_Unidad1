# Función para comprobar que el numero esta en el rango
def estaEnRango(valor, minimo, maximo):
    try:
        return minimo <= int(valor) <= maximo
    except ValueError:
        return False
# Funcion que comprueba que el numero esta en la lista
def estaEnLista(valor, lista):
    try:
        return int(valor) in lista
    except ValueError:
        return False

try:
    # Pedimos el numero al usuario
    numuser = int(input("Introduce un número del 1 al 20: "))
    # Llamamos a la funcion estaEnRango para comprobar 
    if estaEnRango(numuser, 1, 20):
        listnum = [6, 14, 11, 3, 2, 1, 15, 19]
        # LLamamos a la funcion estaEnLista para comprobar
        if estaEnLista(numuser, listnum):
            print(f"{numuser} está en la lista.")
        else:
            print(f"{numuser} no está en la lista.")
    else:
        print("Error: El número debe estar entre el 1 y el 20.")
except ValueError:
    print("Error: Ingresa un valor numérico válido.")