def obtener_datos():
    a = input()
    b = input()
    return a,b

def calcular_rerespuesta(a : str ,b : str):
    respuesta = ""
    for i in range(len(a)):
        respuesta += "0" if a[i] == b[i] else "1"
    return respuesta

primer_numero, segundo_numero = obtener_datos()
print(calcular_rerespuesta(primer_numero, segundo_numero))