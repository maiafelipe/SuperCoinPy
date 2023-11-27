import random as rd
class Jogo:
    strategies = {
            "Aleatório": 0,
            "Apenas Cara": 1,
            "Apenas Coroa": 2}

    def __init__(self) -> None:
        self.caixa = {
            "Jogador1": 50,
            "Jogador2": 50,
            "Jogador3": 50,
            "Banca": 100
        }

        self.nJogadas = 0 

        self.rewardsCara = 0
        self.rewardsCoroa = 0

        self.p1Strategie = 0
        self.p1MaxValue = 0
        self.p1MinValue = 0

        self.p2Strategie = 0
        self.p2MaxValue = 0
        self.p2MinValue = 0

        self.p3Strategie = 0
        self.p3MaxValue = 0
        self.p3MinValue = 0

        self.currAposta1 = 0
        self.currAposta2 = 0
        self.currAposta3 = 0
        self.currSaida = 0
    #}__init__

    def runTurno(self) -> None:
        self.currAposta1 = 0
        if self.p1Strategie == Jogo.strategies["Apenas Coroa"]:
            self.currAposta1 = 1
        elif self.p1Strategie == Jogo.strategies["Aleatório"]:
            self.currAposta1 = rd.randint(0,1)
        valoraposta1 = rd.randint(self.p1MinValue, self.p1MaxValue)
        if self.caixa["Jogador1"] > valoraposta1:
            self.caixa["Banca"] += valoraposta1
            self.caixa["Jogador1"] -= valoraposta1
        else:
            valoraposta1 = 0

        self.currAposta2 = 0
        if self.p2Strategie == Jogo.strategies["Apenas Coroa"]:
            self.currAposta2 = 1
        elif self.p2Strategie == Jogo.strategies["Aleatório"]:
            self.currAposta2 = rd.randint(0,1)
        valoraposta2 = rd.randint(self.p2MinValue, self.p2MaxValue)
        if self.caixa["Jogador2"] > valoraposta2:
            self.caixa["Banca"] += valoraposta2
            self.caixa["Jogador2"] -= valoraposta2
        else:
            valoraposta2 = 0

        self.currAposta3 = 0
        if self.p3Strategie == Jogo.strategies["Apenas Coroa"]:
            self.currAposta3 = 1
        elif self.p3Strategie == Jogo.strategies["Aleatório"]:
            self.currAposta3 = rd.randint(0,1)
        valoraposta3 = rd.randint(self.p3MinValue, self.p3MaxValue)
        if self.caixa["Jogador3"] > valoraposta3:
            self.caixa["Banca"] += valoraposta3
            self.caixa["Jogador3"] -= valoraposta3
        else:
            valoraposta3 = 0

        self.currSaida = rd.randint(0,1)
        rewards = 1
        if self.currSaida == 0:
            rewards = self.rewardsCara
        else:
            rewards = self.rewardsCoroa

        if self.currAposta1 == self.currSaida:
            self.caixa["Banca"] -= valoraposta1*rewards
            self.caixa["Jogador1"] += valoraposta1*rewards

        if self.currAposta2 == self.currSaida:
            self.caixa["Banca"] -= valoraposta2*rewards
            self.caixa["Jogador2"] += valoraposta2*rewards

        if self.currAposta3 == self.currSaida:
            self.caixa["Banca"] -= valoraposta3*rewards
            self.caixa["Jogador3"] += valoraposta3*rewards
    #}runTurno  
#}Player