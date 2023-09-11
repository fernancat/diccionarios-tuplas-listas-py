lista = []


for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)



menor = lista[0]
posicion = 0

for x in range (1,5):
    if lista[x] < menor:
        menor = lista[x]
        posicion=x


print(f"Lista {lista}")
print(f"Menor de la lista {menor}")
print(f"posicion  del menor de la lista {posicion}")