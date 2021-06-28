original=["ananá","manzana", "uva", "pera", "limón", "frutilla", "banana", "perejil"]
aEliminar=["perejil", "limón"]

def filtrar(original, aEliminar):
    resultante=[i for i in original if not i in aEliminar]
    return(original, aEliminar, resultante)

print(filtrar(original, aEliminar))