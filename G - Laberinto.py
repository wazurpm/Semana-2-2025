def obtener_datos():
    alto, ancho = map(int, input().split())
    for i in range(alto):
        laberinto.append(input())

def calcular_resultado(laberinto: list):
    for i in range(alto):
        print(laberinto[i].index("A"))

alto, ancho = 0
laberinto = []

obtener_datos()
calcular_resultado(laberinto)