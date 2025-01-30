def obtener_datos():
    cantidad_valores, cantidad_consultas = map(int, input().split())
    arreglo = list(map(int, input().split()))
    for i in range(cantidad_consultas):
        consultas.append(list(map(int, input().split())))

def calcular_respuesta(arreglo, consultas : list):
    for consulta in consultas:
        sum(arreglo[consulta[0], consulta[1]])

cantidad_valores = 0
cantidad_consultas = 0
arreglo = []
consultas = []

obtener_datos()
calcular_respuesta()