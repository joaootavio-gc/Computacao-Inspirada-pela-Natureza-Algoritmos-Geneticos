import random, numpy

def Problema1(probabilidadeCrossOver, probabilidadeMutacao):
    populacao = inicializar()
    aptidao = avaliar(populacao)
    if 12 in aptidao:
        print('Um indivíduo alcançou o alvo!\n')

    t = 1
    while not(atingiuAlvo(aptidao)):
        populacao = selecionar(populacao, aptidao)
        populacao = reproduzir(populacao, aptidao, probabilidadeCrossOver)
        populacao = variar(populacao, probabilidadeMutacao)
        aptidao   = avaliar(populacao)
        t += 1
    print("Numero de iterações: %d" %t)
    for individuo in populacao:
        print(individuo)

def inicializar():
    populacao = []
    individuo = []
    for i in range(0, 8):
        individuo = []
        for j in range(0, 12):
             individuo.append(random.randint(0,1))
        populacao.append(individuo)
    return populacao


def selecionar(populacao, aptidao):
    somaAptidoes = sum(aptidao)
    porcaoRoleta = []
    selecionados = []
    porcaoRoleta.append(360*aptidao[0]/somaAptidoes)
    for i in range(1,8):
        porcaoRoleta.append((360*aptidao[i]/somaAptidoes) + porcaoRoleta[i-1])
    for i in range(0, 8):
        sorteado = random.randint(0, 360)
        i = 0 #para guardar o indice do individuo escolhido
        while porcaoRoleta[i] < sorteado:
            i += 1
            if i <= 7:
                break
        selecionados.append(populacao[i])
    return selecionados

def reproduzir(populacao, aptidao, probabilidadeCrossOver):
    i = 0
    novaPopulacao = []
    while i < len(populacao):
        if random.random() <= probabilidadeCrossOver: #fazer o cruzamento entre dois indivíduos
            pontoCrossOver = random.randint(1, 11) #pois a posição 0 e a 12 degeneram o cross over
            filho1 = [0] * 12
            filho2 = [0] * 12
            for j in range(0, pontoCrossOver):
                filho1[j] = populacao[i][j]
                filho2[j] = populacao[i+1][j]
            while j < 12:
                filho1[j] = populacao[i+1][j]
                filho2[j] = populacao[i][j]
                j += 1
            novaPopulacao.append(filho1)
            novaPopulacao.append(filho2)
        else: #os pais originais são repetidos na próxima geração
            novaPopulacao.append(populacao[i])
            novaPopulacao.append(populacao[i+1])
        i += 2
    return novaPopulacao

def variar(populacao, probabilidadeMutacao):
    for individuo in populacao:
        for gene in range(0, len(individuo)):
            if random.random() <= probabilidadeMutacao:
                individuo[gene] = 1 if individuo[gene] == 0 else 0 # expressão condicional para inverter o bit
    return populacao

def avaliar(populacao):
    alvo = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    aptidao = []
    for individuo in populacao:
        #contar o numero de elementos diferentes e subtrair 12 é o mesmo que contar os iguais
        #usando um vetor numpy, cada elemento de aptidão conterá os elementos iguais
        aptidao.append(numpy.sum(numpy.array(individuo) == numpy.array(alvo)))
    return aptidao

def atingiuAlvo(aptidao):
    return True if 12 in aptidao else False


if __name__ == '__main__':
    probabilidadeCrossOver = 0.7
    probabilidadeMutacao = 0.00
    Problema1(probabilidadeCrossOver, probabilidadeMutacao)