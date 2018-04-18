def algoritmoEvolutivoPadrao(probabilidadeCrossOver, probabilidadeMutacao):
    populacao = inicializar()
    aptidao = avaliar(populacao)
    t = 1
    while True:
        populacao = selecionar(populacao, aptidao)
        populacao = reproduzir(populacao, aptidao, probabilidadeCrossOver)
        populacao = variar(populacao, probabilidadeMutacao)
        aptidao   = avaliar(populacao)
        t += 1


def inicializar(populacao):
    return 1

def selecionar(populacao, aptidao):
    return 1

def reproduzir(populacao, aptidao, probabilidadeCrossOver):
    return 1

def variar(populacao, probabilidadeMutacao):
    return 1

def avaliar(populacao):
    return 1
