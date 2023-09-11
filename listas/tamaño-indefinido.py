lista = []


valor = int(input("Ingresa valor 0 para finalizar: "))


while valor != 0:
    lista.append(valor)
    valor = int(input("Ingresa valor 0 para finalizar: "))



print(f"Tamaño de la lista: {len(lista)}" )