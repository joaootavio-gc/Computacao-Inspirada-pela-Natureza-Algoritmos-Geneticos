import random

def Problema1(probabilidadeCrossOver, probabilidadeMutacao):
    alvo = [1,1,1,1,0,1,1,0,1,1,1,1]
    populacao = inicializar()
    aptidao = avaliar(populacao)
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
    return 1

def reproduzir(populacao, aptidao, probabilidadeCrossOver):
    return 1

def variar(populacao, probabilidadeMutacao):
    return 1

def avaliar(populacao):
    aptidao = []
    for individuo in populacao:
        aptidao.append(sum(individuo))
    return aptidao

if __name__ == '__main__':
    probabilidadeCrossOver = 1
    probabilidadeMutacao = 1
    Problema1(probabilidadeCrossOver, probabilidadeMutacao)