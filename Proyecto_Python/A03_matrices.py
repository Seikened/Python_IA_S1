
def matriz(cA, rA, cB, rB):
     
     import random
     
     def numeroMatriz():
          numero = random.randint(-10,10)
          return numero

     while True:
          # Matríz a
          columnasA =  cA
          renglonesA =  rA
          # Matríz b
          columnasB = cB
          renglonesB = rB
          if columnasA == renglonesB:
               break

     matrizA = [[numeroMatriz() for _ in range(columnasA)] for _ in range(renglonesA)]

     matrizB = [[numeroMatriz() for _ in range(columnasB)] for _ in range(renglonesB)]

     lista = [[] ]

     # Tamaño de la matríz c
     matrizC = [[0 for _ in range(len(matrizB[0]))] for _ in range(len(matrizA))]

     for i in range(len(matrizA)):
          for j in range(len(matrizB[0])):
               for k in range(len(matrizA[0])):
                    posicionA = matrizA[i][k]
                    posisionB = matrizB[k][j]
                    matrizC[i][j] += posicionA * posisionB

     
     return matrizA, matrizB, matrizC
