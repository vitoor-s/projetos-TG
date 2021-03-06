def imprimir(matriz):
    for i in range(len(matriz)):
        print('linha ',i+1,':', end='')
        print(matriz[i],end='')
        print("soma:",sum(matriz[i]))

def imprimirLista(l):
    print('[')
    for i in range(len(l)):
        print('casa ', i + 1,', probabilidade :', l[i] * 100,'%,', sep='')
    print(']')

def addA(origem, destino):
    matrizP[origem-1][destino-1] += 0.5

def multiplicaVetorMatriz(matriz1, matriz2):

    result = [0] * len(matriz2[0])

    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            result[j] += matriz1[k] * matriz2[k][j]

    return result

def multiplicaMatrizConstante(matriz, constante):
    m = [0] * len(matriz)
    for i in range(len(matriz[0])):
        m[i] = [0] * len(matriz[0])

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            m[i][j] = constante * matriz[i][j]
    return m

def somaMatriz(matrizA, matrizB):
    if len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0]):
        m = [0] * len(matrizA)
        for i in range(len(matrizA[0])):
            m[i] = [0] * len(matrizA[0])

        for linha in range(len(matrizA)):
            for coluna in range(len(matrizA[0])):
                m[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
    return m

def adaptaP(matriz):
    m = [0] * 36
    for i in range(36):
        m[i] = [0] * 36

    for linha in range(36):
            if sum(matriz[linha]) == 0.0:
                for coluna in range(36):
                    m[linha][coluna] = 1/36
            else:
                m[linha] = matriz[linha]
    return m

def indicaLinha0(matriz):
    flag = True
    for linha in range(len(matriz)):
        if sum(matriz[linha]) == 0:
            flag = False
            print('linha nula:',linha+1)

    if flag:
        print("Sem linhas nulas")
#definindo constante alpha
ALPHA = 0.1

#criando matriz P
matrizP = [0]*36
for i in range(len(matrizP)):
    matrizP[i] = [0]*36


#definindo P
addA(1,15)
addA(1,3)

addA(3,4)
addA(3,7)

addA(4,7)
addA(4,6)

addA(6,7)
addA(6,8)

addA(7,8)
addA(7,27)

addA(8,27)
addA(8,10)

addA(10,11)
addA(10,12)

addA(11,12)
addA(11,13)

addA(12,13)
addA(12,14)

addA(13,14)
addA(13,15)

addA(14,15)
addA(14,16)

addA(15,16)
addA(15,4)

addA(16,4)
addA(16,29)

addA(19,6)
addA(19,21)

addA(21,22)
addA(21,23)

addA(22,23)
addA(22,16)

addA(23,16)
addA(23,35)

addA(26,27)
addA(26,28)

addA(27,28)
addA(27,29)

addA(28,29)
addA(28,30)

addA(29,30)
addA(29,31)

addA(30,31)
addA(30,30)

addA(31,30)
addA(31,33)

addA(33,12)
addA(33,35)

addA(35,36)
addA(35,36)

addA(36,36)
addA(36,36)

#criando vetor w
w = [0]*36

#definindo posição inicial como 0, correspondente a posição 1 do tabuleiro
w[0] = 1

#executando power method 100 vezes
for i in range(100):
    w = multiplicaVetorMatriz(w, matrizP)

#distribuição estacionaria com nº de interações igual a 100
#print(w)
imprimirLista(w)
print("soma w:", sum(w))

#PAGE RANK
matrizP_PR = adaptaP(matrizP)

#criando matriz unitaria
U = [1] * 36
for i in range(len(U)):
    U[i] = [1] * 36

#criando matriz P barra
matrizP_ = somaMatriz(multiplicaMatrizConstante(matrizP_PR, (1 - ALPHA)), multiplicaMatrizConstante(U, (ALPHA * 1 / 36)))

#criando vetor wP para distribuição estacionária no modelo page-rank
wP = [0] * 36

#definindo posição inicial como 0, correspondente a posição inicial do tabuleiro
wP[0] = 1

#executando power method 100 vezes
for i in range(100):
    wP = multiplicaVetorMatriz(wP, matrizP_)

imprimirLista(wP)
print("soma wP:", sum(wP))
print("max wP:", max(wP))
