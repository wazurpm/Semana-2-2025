def recibir_datos():
    cantidad_problemas = int(input())
    if cantidad_problemas < 1 or cantidad_problemas > 1000:
        print("***Error: Cantidad de problemas fuera de rango***")
        exit()

    for i in range(cantidad_problemas):
        problemas.append(list(map(int,input().replace(" ", ""))))

def obtener_respuesta():
  suma = 0

  for problema in problemas:
    if len(problema) == 3:
      for i in range(len(problema)):
          if problema[i] < 0 or problema[i] > 1:
              print("***Error: Verifique los datos de entrada***")
              exit()
    else:
      print("***Error: Verifique los datos de entrada***")
      exit()

    if sum(problema) >= 2:
                suma += 1

  print(suma)

problemas = []
recibir_datos()
obtener_respuesta()