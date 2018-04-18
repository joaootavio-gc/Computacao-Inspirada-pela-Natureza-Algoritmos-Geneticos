import random
from math import sin, pi, exp


def subinaColina(maximoIteracoes):
    x = inicializar()
    t = 1
    ultimasSolucoes = []
    while t < maximoIteracoes and not(convergiu(ultimasSolucoes)):
        xl = perturbar(x)
        # restringir intervalo de xl
        if xl > 1:
            xl = 1
        if xl < 0:
            xl = 0
        if avaliar(xl) > avaliar(x): # pois é um problema de maximização
            x = xl
            ultimasSolucoes.append(x)
        t += 1
    return x


def subinaColinaIterativo(numeroInicializacoes, maximoIteracoes):
    melhor = inicializar() #inicializar melhor
    t = 1
    ultimasSolucoes = []
    while t < numeroInicializacoes and not(convergiu(ultimasSolucoes)):
        x = inicializar()
        x = subinaColina(maximoIteracoes)
        t += 1
        if avaliar(x) > avaliar(melhor): # pois é um problema de maximização
            melhor = x
            ultimasSolucoes.append(x)

    return x


def subinaColinaEstocastico(maximoIteracoes, T):
    x = inicializar()
    t = 1
    ultimasSolucoes = []
    while t < maximoIteracoes and not(convergiu(ultimasSolucoes)):
        xl = perturbar(x)
        # restringir intervalo de xl
        if xl > 1:
            xl = 1
        if xl < 0:
            xl = 0
        if random.random() < (1/(1+exp((avaliar(xl) > avaliar(x))/T))): # pois é um problema de maximização
            x = xl
            ultimasSolucoes.append(x)
        t += 1
    return x






def inicializar():
    return random.random() #gera um aleatório entre 0 e 1

def avaliar(x):
    return 2**(-2*((x-0.1)/0.9)**2)*((sin(5*pi*x))**6)

def perturbar(x):
    return x + random.gauss(0, 0.1)

def convergiu(ultimasSolucoes):
    if len(ultimasSolucoes) < 10: #tamanh minimo de k(=10) elementos
        return 0; #pois temos poucos elementos para concluir se ouve convergência
    ultimos = len(ultimasSolucoes) - 10 # olhar no proxímo laço as últimas k(=10) avaliações
    pontos = 0#para contar as avaliações que convergiram
    for i in range(ultimos, len(ultimasSolucoes)):
        if ultimasSolucoes[ultimos] - ultimasSolucoes[i] >= abs(0.001):
            pontos += 1
    if pontos >= 10: #k(=10)
        return 1
    return 0