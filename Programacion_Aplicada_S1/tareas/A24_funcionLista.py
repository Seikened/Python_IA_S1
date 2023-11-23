def NumeroEntero(n):
    tamLista = n
    lista = [0 for _ in range(tamLista)]
    for posicion in range(tamLista):
        numeroUser = float(input(f"Dame tu numero en la posición ({posicion+1}): "))
        lista[posicion] = numeroUser #type: ignore
    return lista


numero = int(input("¿De que tamaño quieres tu lista?: "))
print(NumeroEntero(numero))