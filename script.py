import numpy as np
import matplotlib.pyplot as plt
import random as rd

caixa = {
    "Jogador1": 50,
    "Jogador2": 50,
    "Jogador3": 50,
    "Banca": 100}

strategies = {
    "Aleatório": 0,
    "Apenas Cara": 1,
    "Apenas Coroa": 2}

rewardsCara = 1.7
rewardsCoroa = 1.7

rounds = 100 

p1Strategie = strategies["Aleatório"]
p1MaxValue = 10
p1MinValue = 5

p2Strategie = strategies["Aleatório"]
p2MaxValue = 10
p2MinValue = 5

p3Strategie = strategies["Aleatório"]
p3MaxValue = 5
p3MinValue = 1

keys = list(caixa.keys())
values = list(caixa.values())


fig = plt.figure(figsize=(20,10))


for i in range(1, rounds+1):
    aposta1 = 0
    if p1Strategie == strategies["Apenas Coroa"]:
        aposta1 = 1
    elif p1Strategie == strategies["Aleatório"]:
        aposta1 = rd.randint(0,1)
    valoraposta1 = rd.randint(p1MinValue, p1MaxValue)
    if caixa["Jogador1"] > valoraposta1:
        caixa["Banca"] += valoraposta1
        caixa["Jogador1"] -= valoraposta1
    else:
        valoraposta1 = 0

    aposta2 = 0
    if p2Strategie == strategies["Apenas Coroa"]:
        aposta2 = 1
    elif p2Strategie == strategies["Aleatório"]:
        aposta2 = rd.randint(0,1)
    valoraposta2 = rd.randint(p2MinValue, p2MaxValue)
    if caixa["Jogador2"] > valoraposta2:
        caixa["Banca"] += valoraposta2
        caixa["Jogador2"] -= valoraposta2
    else:
        valoraposta2 = 0

    aposta3 = 0
    if p3Strategie == strategies["Apenas Coroa"]:
        aposta3 = 1
    elif p3Strategie == strategies["Aleatório"]:
        aposta3 = rd.randint(0,1)
    valoraposta3 = rd.randint(p3MinValue, p3MaxValue)
    if caixa["Jogador3"] > valoraposta3:
        caixa["Banca"] += valoraposta3
        caixa["Jogador3"] -= valoraposta3
    else:
        valoraposta3 = 0

    saida = rd.randint(0,1)
    rewards = 1
    if saida == 0:
        rewards = rewardsCara
    else:
        rewards = rewardsCoroa

    if aposta1 == saida:
        caixa["Banca"] -= valoraposta1*rewards
        caixa["Jogador1"] += valoraposta1*rewards

    if aposta2 == saida:
        caixa["Banca"] -= valoraposta2*rewards
        caixa["Jogador2"] += valoraposta2*rewards

    if aposta3 == saida:
        caixa["Banca"] -= valoraposta3*rewards
        caixa["Jogador3"] += valoraposta3*rewards

    saidaText = "Cara" if saida == 0 else "Coroa"
    aposta1Text = "Cara" if aposta1 == 0 else "Coroa"
    aposta2Text = "Cara" if aposta2 == 0 else "Coroa"
    aposta2Text = "Cara" if aposta3 == 0 else "Coroa"

    keys = list(caixa.keys())
    values = list(caixa.values())
    plt.clf()
    plt.title(f"Era {i}: ")
    plt.xlabel("Jogadores")
    plt.ylabel("Carteira")
    plt.ylim((0, 500))

    keys = (f"Jogador1 ${caixa['Jogador1']:.2f}",
            f"Jogador2 ${caixa['Jogador2']:.2f}",
            f"Jogador3 ${caixa['Jogador3']:.2f}",
            f"Banca ${caixa['Banca']:.2f}")
    plt.bar(keys, values, color ='blue', 
        width = 0.5)

    plt.draw()
    plt.pause(0.01)

plt.show()