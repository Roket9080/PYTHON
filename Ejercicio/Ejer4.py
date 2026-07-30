#listas

listaVacia = []
print(type(listaVacia))

print(listaVacia)
listaVacia.append("dato")
print(listaVacia)

paises=["Colombia","Peru","Venezuela","Ecuador","Bolivia","Kazajistan","Reino Unido de Gran Bretaña e Irlanda del Norte","Yugoslavia"]

print(paises)
print(f"longitud de la lista es {len(paises)}")

print(paises[:4])
paises[7] = "Nicaragua"

print(paises)

paises.insert(1,"Portugal")

print(paises)

paises.pop(6)
print(paises)

frutas=("manzana","pera","Banano","manzana")

print(frutas.count("manzana"))

