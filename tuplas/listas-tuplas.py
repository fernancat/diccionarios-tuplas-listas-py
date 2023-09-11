fechatupla1 = (25,12,2016)

print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista = list(fechatupla1)
print("imprimimos la lista que se le copio a la tupla anterior")
print(fechalista)
#modificamos la lista
fechalista[0]=31
print(f"imprimimos la lista ya modificada: {fechalista}")
#copiamos la lista modificada a una tupla
fechatupla2= tuple(fechalista)
print(f"Imprimamos la segund tupla que se le copio a la lista {fechatupla2}")
