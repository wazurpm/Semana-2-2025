def obtener_datos():
    entrada = []
    for i in range(5):
        entrada.append(list(input().split(" ")))
    return entrada

def calcular_respuesta(matrix : list):
    ubicacion = []
    for i in range(len(matrix)):
        if matrix[i].index(1):
            ubicacion = [int(i), int(matrix[i].index("1"))]
    respuesta = max(ubicacion) - min(ubicacion)
    return respuesta

matriz = obtener_datos()
print(calcular_respuesta(matriz))