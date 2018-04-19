import random, numpy

def Problema1(probabilidadeCrossOver, probabilidadeMutacao):
    populacao = inicializar()
    aptidao = avaliar(populacao)
    if 12 in aptidao:
        print('Um indivíduo alcançou o alvo!\n')

    t = 1
    while True:
        populacao = selecionar(populacao, aptidao)
        populacao = reproduzir(populacao, aptidao, probabilidadeCrossOver)
        populacao = variar(populacao, probabilidadeMutacao)
        aptidao   = avaliar(populacao)
        t += 1


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
        somaAuxiliar = 0 #para percorrer as porções da roleta buscando o elemento correto
        i = 0 #para guardar o indice do individuo escolhido
        while porcaoRoleta[i] < sorteado:
            i += 1
        selecionados.append(populacao[i])
    return selecionados

def reproduzir(populacao, aptidao, probabilidadeCrossOver):
    return 1

def variar(populacao, probabilidadeMutacao):
    return 1

def avaliar(populacao):
    alvo = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    aptidao = []
    for individuo in populacao:
        #contar o numero de elementos diferentes e subtrair 12 é o mesmo que contar os iguais
        #usando um vetor numpy, cada elemento de aptidão conterá os elementos iguais
        aptidao.append(numpy.sum(numpy.array(individuo) == numpy.array(alvo)))
    return aptidao

if __name__ == '__main__':
    probabilidadeCrossOver = 1
    probabilidadeMutacao = 1
    Problema1(probabilidadeCrossOver, probabilidadeMutacao)