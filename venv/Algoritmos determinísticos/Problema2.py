import random
from math import sin, pi, exp, pow

def Problema2(probabilidadeCrossOver, probabilidadeMutacao, maximoIteracoes):
    populacao = inicializar()
    aptidoes = avaliar(populacao)
    ultimasSolucoes = []
    ultimasSolucoes.append(max(aptidoes))#ultimas soluções guarda os melhores individuos de cada geração
    t = 1
    while t < maximoIteracoes and not(convergiu(ultimasSolucoes)):
        populacao = selecionar(populacao, aptidoes)
        populacao = reproduzir(populacao, probabilidadeCrossOver)
        populacao = variar(populacao, probabilidadeMutacao)
        aptidoes   = avaliar(populacao)
        t += 1
    print("Numero de iterações: %d" %t)
    for individuo in populacao:
        print(paraReal(individuo))

def inicializar():
    populacao = []
    individuo = []
    for i in range(0, 40):#população de 40 individuos
        individuo = []
        for j in range(0, 30):#30 casas decimais para representação
            individuo.append(random.randint(0,1))
        if individuo[0] == 1:
            for y in range(1, 30):
                individuo[y] = 0
        populacao.append(individuo)
    return populacao


def selecionar(populacao, aptidao):
    somaAptidoes = sum(aptidao)
    porcaoRoleta = []
    selecionados = []
    porcaoRoleta.append(360*aptidao[0]/somaAptidoes)
    for i in range(1,30):
        porcaoRoleta.append((360*aptidao[i]/somaAptidoes) + porcaoRoleta[i-1])
    for i in range(0, 30):
        sorteado = random.randint(0, 360)
        i = 0 #para guardar o indice do individuo escolhido
        while porcaoRoleta[i] < sorteado:
            i += 1
            if i == 29:
                break
        selecionados.append(populacao[i])
    return selecionados

def reproduzir(populacao, probabilidadeCrossOver):
    i = 0
    novaPopulacao = []
    while i < len(populacao):
        if random.random() <= probabilidadeCrossOver: #fazer o cruzamento entre dois indivíduos
            pontoCrossOver = random.randint(1, 11) #pois a posição 0 e a 30 degeneram o cross over
            filho1 = [0] * 30
            filho2 = [0] * 30
            for j in range(0, pontoCrossOver):
                filho1[j] = populacao[i][j]
                filho2[j] = populacao[i+1][j]
            while j < 30:
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
    aptidao = []
    for individuo in populacao:
        #avaliar cada individuo através g(x)
        real = paraReal(individuo)
        aptidao.append(2**(-2*((real-0.1)/0.9)**2)*((sin(5*pi*real))**6))
    return aptidao

def paraReal(individuo):
    real = 0
    for i in range(0, 30):
        real += (1/pow(2,i))*individuo[i]
    return real


def convergiu(ultimasSolucoes):
    if len(ultimasSolucoes) < 100: #tamanh minimo de k(=100) elementos
        return False; #pois temos poucos elementos para concluir se ouve convergência
    ultimos = len(ultimasSolucoes) - 100 # olhar no proxímo laço as últimas k(=100) avaliações
    pontos = 0 #para contar as avaliações que convergiram
    for i in range(ultimos, len(ultimasSolucoes)):
        # epsilon(0.0001) pode ser tão pequeno quanto necessário
        if abs(ultimasSolucoes[ultimos] - ultimasSolucoes[i]) <= 0.0001:
            pontos += 1
    if pontos >= 100: #k(=100)
        return True
    return False


if __name__ == '__main__':
    probabilidadeCrossOver = 0.7
    probabilidadeMutacao = 0.1
    Problema2(probabilidadeCrossOver, probabilidadeMutacao, 10000)