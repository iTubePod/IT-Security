
def cifrarBloque(bloque, llave):
    cifrado = ""
    for i in range(0,4):
        cifrado+=chr(ord(bloque[i])^llave[i])
    return cifrado


def ECB(mensaje, llaveTexto):
    if len(mensaje)%4!=0:
        for i in range(0, 4-int(len(mensaje)%4)):
            mensaje+="!"
        print(mensaje)
    llave = []
    for c in llaveTexto:
        llave.append(ord(c))
    cifrado =""
    for i in range(0, int(len(mensaje)/4)):
        cifrado += cifrarBloque(mensaje[(i*4):(i*4)+4], llave)
    return cifrado

mensajeCifrado = ECB("HolaTMP", "1234")
print(mensajeCifrado)
mensajeCifrado = ECB(mensajeCifrado, "1234")
print(mensajeCifrado)