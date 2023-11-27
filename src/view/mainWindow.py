import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rd
import tkinter as tk
from controller.mainController import MainController

class MainWindow:
    OPTIONS = [
            "Aleatório",
            "Apenas Cara",
            "Apenas Coroa"
        ]

    def __init__(self):
        self.root = tk.Tk()

        self.controller = MainController(self)

        (self.fig, self.ax) = plt.subplots()

        self.varQntJogadas = tk.IntVar(value=100)
        self.varRewardCara = tk.DoubleVar(value=1.7)
        self.varRewardCoroa = tk.DoubleVar(value=1.7)
        self.varTimeIntervalo = tk.IntVar(value=20)
        self.varCaixaBanca = tk.DoubleVar(value=100.0)

        self.varP1StrategeOption = tk.StringVar()
        self.varP1StrategeOption.set(MainWindow.OPTIONS[0])
        self.varCaixaP1 = tk.DoubleVar(value=50.0)
        self.varP1Min = tk.DoubleVar(value=1.0)
        self.varP1Max = tk.DoubleVar(value=5.0)

        self.varP2StrategeOption = tk.StringVar() 
        self.varP2StrategeOption.set(MainWindow.OPTIONS[0])
        self.varCaixaP2 = tk.DoubleVar(value=50.0)
        self.varP2Min = tk.DoubleVar(value=1.0)
        self.varP2Max = tk.DoubleVar(value=5.0)

        self.varP3StrategeOption = tk.StringVar()
        self.varP3StrategeOption.set(MainWindow.OPTIONS[0])
        self.varCaixaP3 = tk.DoubleVar(value=50.0)
        self.varP3Min = tk.DoubleVar(value=1.0)
        self.varP3Max = tk.DoubleVar(value=5.0)
    #} __init__

    def start(self)->None:
        self.defineViewComponents()

        self.root.mainloop()
        
    #} start 

    def defineViewComponents(self) -> None:
        frameInput = tk.Frame(self.root)
        framePlot = tk.Frame(self.root)

        self.root.title("SuperCoinHouse")

        labelTitle = tk.Label(text="Super Coin House")
        labelTitle.config(font=("Courier", 32))
        labelTitle.pack()

        frameInput.pack(side=tk.LEFT)
        framePlot.pack(side=tk.RIGHT)

        validFloat = (self.root.register(self.validateFloat),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        validInt = (self.root.register(self.validateInt),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        rowComponent = 0

        labelQntJogadas = tk.Label(text="Quantidade de Jogadas:", master=frameInput)
        labelQntJogadas.grid(column=0, row=rowComponent)
        entryQntJogadas = tk.Entry(master=frameInput, textvariable=self.varQntJogadas, validate = 'key', validatecommand = validInt)
        entryQntJogadas.grid(column=1, row=rowComponent)
        rowComponent+=1
        
        labelRewardCara = tk.Label(text="Prêmio Cara:",master=frameInput)
        labelRewardCara.grid(column=0, row=rowComponent)
        entryRewardCara = tk.Entry(master=frameInput, textvariable=self.varRewardCara, validate = 'key', validatecommand = validFloat)
        entryRewardCara.grid(column=1, row=rowComponent)
        rowComponent+=1
        
        labelRewardCoroa = tk.Label(text="Prêmio Coroa:",master=frameInput)
        labelRewardCoroa.grid(column=0, row=rowComponent)
        entryRewardCoroa = tk.Entry(master=frameInput, textvariable=self.varRewardCoroa, validate = 'key', validatecommand = validFloat)
        entryRewardCoroa.grid(column=1, row=rowComponent)
        rowComponent+=1
        
        labelTimeIntervalo = tk.Label(text="Intervalo (ms):",master=frameInput)
        labelTimeIntervalo.grid(column=0, row=rowComponent)
        entryTimeIntervalo = tk.Entry(master=frameInput, textvariable=self.varTimeIntervalo, validate = 'key', validatecommand = validInt)
        entryTimeIntervalo.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelCaixaBanca = tk.Label(text="Carteira Banca:",master=frameInput)
        labelCaixaBanca.grid(column=0, row=rowComponent)
        entryCaixaBanca = tk.Entry(master=frameInput, textvariable=self.varCaixaBanca, validate = 'key', validatecommand = validFloat)
        entryCaixaBanca.grid(column=1, row=rowComponent)
        rowComponent+=1
        
        labelPlayer1 = tk.Label(text="Jogador 1:",master=frameInput)
        labelPlayer1.grid(column=0, row=rowComponent)
        labelPlayer1.config(font=("Courier", 20))
        rowComponent+=1
        labelP1Estra = tk.Label(text="Estratégia:",master=frameInput)
        labelP1Estra.grid(column=0, row=rowComponent)
        optionP1Estra = tk.OptionMenu(frameInput, self.varP1StrategeOption, *MainWindow.OPTIONS)
        optionP1Estra.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelCaixaP1 = tk.Label(text="Carteira:",master=frameInput)
        labelCaixaP1.grid(column=0, row=rowComponent)
        entryCaixaP1 = tk.Entry(master=frameInput, textvariable=self.varCaixaP1, validate = 'key', validatecommand = validFloat)
        entryCaixaP1.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelP1Min = tk.Label(text="Jogada Mínima:",master=frameInput)
        labelP1Min.grid(column=0, row=rowComponent)
        entryP1Min = tk.Entry(master=frameInput, textvariable=self.varP1Min, validate = 'key', validatecommand = validFloat)
        entryP1Min.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelP1Max = tk.Label(text="Jogada Máxima:",master=frameInput)
        labelP1Max.grid(column=0, row=rowComponent)
        entryP1Max = tk.Entry(master=frameInput, textvariable=self.varP1Max, validate = 'key', validatecommand = validFloat)
        entryP1Max.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelPlayer2 = tk.Label(text="Jogador 2:",master=frameInput)
        labelPlayer2.grid(column=0, row=rowComponent)
        labelPlayer2.config(font=("Courier", 20))
        rowComponent+=1
        labelP2Estra = tk.Label(text="Estratégia:",master=frameInput)
        labelP2Estra.grid(column=0, row=rowComponent)
        optionP2Estra = tk.OptionMenu(frameInput, self.varP2StrategeOption, *MainWindow.OPTIONS)
        optionP2Estra.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelCaixaP2 = tk.Label(text="Carteira:",master=frameInput)
        labelCaixaP2.grid(column=0, row=rowComponent)
        entryCaixaP2 = tk.Entry(master=frameInput, textvariable=self.varCaixaP2, validate = 'key', validatecommand = validFloat)
        entryCaixaP2.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelP2Min = tk.Label(text="Jogada Mínima:",master=frameInput)
        labelP2Min.grid(column=0, row=rowComponent)
        entryP2Min = tk.Entry(master=frameInput, textvariable=self.varP2Min, validate = 'key', validatecommand = validFloat)
        entryP2Min.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelP2Max = tk.Label(text="Jogada Máxima:",master=frameInput)
        labelP2Max.grid(column=0, row=rowComponent)
        entryP2Max = tk.Entry(master=frameInput, textvariable=self.varP2Max, validate = 'key', validatecommand = validFloat)
        entryP2Max.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelPlayer3 = tk.Label(text="Jogador 3:",master=frameInput)
        labelPlayer3.grid(column=0, row=rowComponent)
        labelPlayer3.config(font=("Courier", 20))
        rowComponent+=1
        labelP3Estra = tk.Label(text="Estratégia:",master=frameInput)
        labelP3Estra.grid(column=0, row=rowComponent)
        optionP3Estra = tk.OptionMenu(frameInput, self.varP3StrategeOption, *MainWindow.OPTIONS)
        optionP3Estra.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelCaixaP3 = tk.Label(text="Carteira:",master=frameInput)
        labelCaixaP3.grid(column=0, row=rowComponent)
        entryCaixaP3 = tk.Entry(master=frameInput, textvariable=self.varCaixaP3, validate = 'key', validatecommand = validFloat)
        entryCaixaP3.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelP3Min = tk.Label(text="Jogada Mínima:",master=frameInput)
        labelP3Min.grid(column=0, row=rowComponent)
        entryP3Min = tk.Entry(master=frameInput, textvariable=self.varP3Min, validate = 'key', validatecommand = validFloat)
        entryP3Min.grid(column=1, row=rowComponent)
        rowComponent+=1

        labelP3Max = tk.Label(text="Jogada Máxima:",master=frameInput)
        labelP3Max.grid(column=0, row=rowComponent)
        entryP3Max = tk.Entry(master=frameInput, textvariable=self.varP3Max, validate = 'key', validatecommand = validFloat)
        entryP3Max.grid(column=1, row=rowComponent)
        rowComponent+=1
        
        buttonStart = tk.Button(frameInput, text="Iniciar", command=lambda: self.clickStart())
        buttonStart.grid(column=0, columnspan=2, row=rowComponent, pady=10, padx=10)

        canvas = FigureCanvasTkAgg(self.fig, master=framePlot)
        canvas.get_tk_widget().pack()   
    #} defineViewComponents   

    def clickStart(self):
        self.controller.loadEntries()
        self.controller.runTurnoAndPlot(1)
    #} clickStart
    
    def validateFloat(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                self.controller.loadEntries()
                self.controller.justPlot()
                return True
            except ValueError:
                return False
        else:
            return False 
    #} validateFloat 

    def validateInt(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                self.controller.loadEntries() #Problema grave: novo plot antes do valor ser atribuido, necessário definir um trigger e plotar após valor ser aceito
                self.controller.justPlot()
                return True
            except ValueError:
                return False
        else:
            return False
        
    #} validateInt

#} MainWindow