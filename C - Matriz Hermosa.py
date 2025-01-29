def obtener_datos():
    entrada = []
    for i in range(5):
        entrada.append(list(input().split(" ")))
    return entrada

def calcular_respuesta(matrix : list):
    ubicacion = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "1":
                ubicacion = [abs((i+1)-3),abs((j+1)-3)]
                print(ubicacion)
                break
    return max(ubicacion) + min(ubicacion)

matriz = obtener_datos()
print(calcular_respuesta(matriz))