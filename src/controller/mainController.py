from model.jogo import Jogo
import matplotlib.pyplot as plt
import random as rd

class MainController:

    def __init__(self, context) -> None:
        self.jogo:Jogo = Jogo()
        self.context = context
        self.graphKeys = []
        self.graphValues = []
        self.timeIntervalo = 1
    #} __init__

    def loadEntries(self) -> None:
        self.jogo.caixa["Jogador1"] = self.context.varCaixaP1.get()
        self.jogo.caixa["Jogador2"] = self.context.varCaixaP2.get()
        self.jogo.caixa["Jogador3"] = self.context.varCaixaP3.get()
        self.jogo.caixa["Banca"] = self.context.varCaixaBanca.get()

        self.jogo.nJogadas = self.context.varQntJogadas.get() 

        self.timeIntervalo = self.context.varTimeIntervalo.get()

        self.jogo.rewardsCara = self.context.varRewardCara.get()
        self.jogo.rewardsCoroa = self.context.varRewardCara.get()


        self.jogo.p1Strategie = Jogo.strategies[self.context.varP1StrategeOption.get()]
        self.jogo.p1MaxValue = self.context.varP1Max.get()
        self.jogo.p1MinValue = self.context.varP1Min.get()

        self.jogo.p2Strategie = Jogo.strategies[self.context.varP2StrategeOption.get()]
        self.jogo.p2MaxValue = self.context.varP2Max.get()
        self.jogo.p2MinValue = self.context.varP2Min.get()

        self.jogo.p3Strategie = Jogo.strategies[self.context.varP2StrategeOption.get()]
        self.jogo.p3MaxValue = self.context.varP2Max.get()
        self.jogo.p3MinValue = self.context.varP2Min.get()

        self.graphKeys = list(self.jogo.caixa.keys())
        self.graphValues = list(self.jogo.caixa.values())

    def justPlot(self) -> None:
        plt.clf()

        plt.title(f"Jogada X: --")
        plt.xlabel("Jogadores")
        plt.ylabel("Carteira")
        plt.ylim((0, 500))

        keys = (f"Jogador1: -- \n R${self.jogo.caixa['Jogador1']:.2f}\n ",
                f"Jogador2: -- \n R${self.jogo.caixa['Jogador2']:.2f} \n ",
                f"Jogador3: -- \n R${self.jogo.caixa['Jogador3']:.2f} \n ",
                f"Banca R${self.jogo.caixa['Banca']:.2f}")
            
        values = list(self.jogo.caixa.values())
        plt.bar(keys, values, color ='blue', width = 0.5)


        plt.draw()
    # }justPlot

    def runTurnoAndPlot(self, currTurno:int) -> None:
        if(currTurno <= self.jogo.nJogadas):

            self.jogo.runTurno()

            saidaText = "Cara" if self.jogo.currSaida == 0 else "Coroa"
            aposta1Text = "Cara" if self.jogo.currAposta1 == 0 else "Coroa"
            aposta2Text = "Cara" if self.jogo.currAposta2 == 0 else "Coroa"
            aposta3Text = "Cara" if self.jogo.currAposta3 == 0 else "Coroa"

            plt.clf()

            plt.title(f"Jogada {currTurno}: {saidaText}")
            plt.xlabel("Jogadores")
            plt.ylabel("Carteira")
            plt.ylim((0, 500))

            keys = (f"Jogador1: {aposta1Text} \n R${self.jogo.caixa['Jogador1']:.2f}\n ",
                f"Jogador2: {aposta2Text} \n R${self.jogo.caixa['Jogador2']:.2f} \n ",
                f"Jogador3: {aposta3Text} \n R${self.jogo.caixa['Jogador3']:.2f} \n ",
                f"Banca R${self.jogo.caixa['Banca']:.2f}")
            
            values = list(self.jogo.caixa.values())
            plt.bar(keys, values, color ='blue', width = 0.5)


            plt.draw()
            self.context.root.after(self.timeIntervalo, self.runTurnoAndPlot, currTurno+1)
    
    #} runTurno

#}MainController