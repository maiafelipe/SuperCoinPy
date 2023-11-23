import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rd
import tkinter as tk

caixa = {
        "Jogador1": 50,
        "Jogador2": 50,
        "Jogador3": 50,
        "Banca": 100}

def plot(currJogada, caixa):
    if currJogada == 1:
        caixa["Jogador1"] = float(varInputCaixaP1.get())
        caixa["Jogador2"] = float(varInputCaixaP2.get())
        caixa["Jogador3"] = float(varInputCaixaP3.get())
        caixa["Banca"] = float(varInputCaixaBanca.get())

    nJogadas = int(varInputEras.get())

    strategies = {
        "Aleatório": 0,
        "Apenas Cara": 1,
        "Apenas Coroa": 2}

    rewardsCara = float(varInputCara.get())
    rewardsCoroa = float(varInputCara.get())


    p1Strategie = strategies[p1Option.get()]
    p1MaxValue = float(varP1Max.get())
    p1MinValue = float(varP1Min.get())

    p2Strategie = strategies[p2Option.get()]
    p2MaxValue = float(varP2Max.get())
    p2MinValue = float(varP2Min.get())

    p3Strategie = strategies[p3Option.get()]
    p3MaxValue = float(varP3Max.get())
    p3MinValue = float(varP3Min.get())

    keys = list(caixa.keys())
    values = list(caixa.values())

    if(currJogada <= nJogadas):

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




        plt.clf()

        plt.title(f"Jogada {currJogada}: ")
        plt.xlabel("Jogadores")
        plt.ylabel("Carteira")
        plt.ylim((0, 500))

        keys = (f"Jogador1 ${caixa['Jogador1']:.2f}",
            f"Jogador2 ${caixa['Jogador2']:.2f}",
            f"Jogador3 ${caixa['Jogador3']:.2f}",
            f"Banca ${caixa['Banca']:.2f}")
        
        values = list(caixa.values())
        plt.bar(keys, values, color ='blue', width = 0.5)


        plt.draw()
        frameInput.after(int(varInputTimeIntervalo.get()), plot, currJogada+1, caixa)
    else:
       caixa["Jogador1"] = float(varInputCaixaP1.get())
       caixa["Jogador2"] = float(varInputCaixaP2.get())
       caixa["Jogador3"] = float(varInputCaixaP3.get())
       caixa["Banca"] = float(varInputCaixaBanca.get())



#Iniciando Tkinter
root = tk.Tk()

fig, ax = plt.subplots()



#Aplicação do Tkinter
frameInput = tk.Frame(root)
framePlot = tk.Frame(root)
label = tk.Label(text="Super Coin House")
label.config(font=("Courier", 32))
label.pack()


labelEras = tk.Label(text="Quantidade de Jogadas:",master=frameInput)
labelEras.grid(column=0, row=0)
varInputEras = tk.Entry(master=frameInput)
varInputEras.insert(tk.END,"100")
varInputEras.grid(column=1, row=0)

labelRCara = tk.Label(text="Premio Cara:",master=frameInput)
labelRCara.grid(column=0, row=1)
varInputCara = tk.Entry(master=frameInput)
varInputCara.insert(tk.END,"1.7")
varInputCara.grid(column=1, row=1)

labelRCoroa = tk.Label(text="Premio Coroa:",master=frameInput)
labelRCoroa.grid(column=0, row=2)
varInputCoroa = tk.Entry(master=frameInput)
varInputCoroa.insert(tk.END,"1.7")
varInputCoroa.grid(column=1, row=2)

labelTimeIntervalo = tk.Label(text="Intervalo (ms):",master=frameInput)
labelTimeIntervalo.grid(column=0, row=3)
varInputTimeIntervalo = tk.Entry(master=frameInput)
varInputTimeIntervalo.insert(tk.END,"20")
varInputTimeIntervalo.grid(column=1, row=3)

labelCaixaBanca = tk.Label(text="Carteira Banca:",master=frameInput)
labelCaixaBanca.grid(column=0, row=4)
varInputCaixaBanca = tk.Entry(master=frameInput)
varInputCaixaBanca.insert(tk.END,"100.0")
varInputCaixaBanca.grid(column=1, row=4)

OPTIONS = [
"Aleatório",
"Apenas Cara",
"Apenas Coroa"
]
p1Option = tk.StringVar(root)
p1Option.set(OPTIONS[0])
p2Option = tk.StringVar(root)
p2Option.set(OPTIONS[0])
p3Option = tk.StringVar(root)
p3Option.set(OPTIONS[0])

labelPlayer1 = tk.Label(text="Jogador 1:",master=frameInput)
labelPlayer1.grid(column=0, row=5)
labelPlayer1.config(font=("Courier", 20))
labelP1Estra = tk.Label(text="Estratégia:",master=frameInput)
labelP1Estra.grid(column=0, row=6)
varP1Estra = tk.OptionMenu(frameInput, p1Option, *OPTIONS)
varP1Estra.grid(column=1, row=6)

labelCaixaP1 = tk.Label(text="Carteira:",master=frameInput)
labelCaixaP1.grid(column=0, row=7)
varInputCaixaP1 = tk.Entry(master=frameInput)
varInputCaixaP1.insert(tk.END,"50.0")
varInputCaixaP1.grid(column=1, row=7)

labelP1Min = tk.Label(text="Jogada Mínima:",master=frameInput)
labelP1Min.grid(column=0, row=8)
varP1Min = tk.Entry(master=frameInput)
varP1Min.insert(tk.END,"1.0")
varP1Min.grid(column=1, row=8)

labelP1Max = tk.Label(text="Jogada Máxima:",master=frameInput)
labelP1Max.grid(column=0, row=9)
varP1Max = tk.Entry(master=frameInput)
varP1Max.insert(tk.END,"5.0")
varP1Max.grid(column=1, row=9)



labelPlayer2 = tk.Label(text="Jogador 2:",master=frameInput)
labelPlayer2.grid(column=0, row=10)
labelPlayer2.config(font=("Courier", 20))
labelP2Estra = tk.Label(text="Estratégia:",master=frameInput)
labelP2Estra.grid(column=0, row=11)
varP2Estra = tk.OptionMenu(frameInput, p2Option, *OPTIONS)
varP2Estra.grid(column=1, row=11)

labelCaixaP2 = tk.Label(text="Carteira:",master=frameInput)
labelCaixaP2.grid(column=0, row=12)
varInputCaixaP2 = tk.Entry(master=frameInput)
varInputCaixaP2.insert(tk.END,"50.0")
varInputCaixaP2.grid(column=1, row=12)

labelP2Min = tk.Label(text="Jogada Mínima:",master=frameInput)
labelP2Min.grid(column=0, row=13)
varP2Min = tk.Entry(master=frameInput)
varP2Min.insert(tk.END,"1.0")
varP2Min.grid(column=1, row=13)

labelP2Max = tk.Label(text="Jogada Máxima:",master=frameInput)
labelP2Max.grid(column=0, row=14)
varP2Max = tk.Entry(master=frameInput)
varP2Max.insert(tk.END,"5.0")
varP2Max.grid(column=1, row=14)


labelPlayer3 = tk.Label(text="Jogador 3:",master=frameInput)
labelPlayer3.grid(column=0, row=15)
labelPlayer3.config(font=("Courier", 20))
labelP3Estra = tk.Label(text="Estratégia:",master=frameInput)
labelP3Estra.grid(column=0, row=16)
varP3Estra = tk.OptionMenu(frameInput, p3Option, *OPTIONS)
varP3Estra.grid(column=1, row=16)

labelCaixaP3 = tk.Label(text="Carteira:",master=frameInput)
labelCaixaP3.grid(column=0, row=17)
varInputCaixaP3 = tk.Entry(master=frameInput)
varInputCaixaP3.insert(tk.END,"50.0")
varInputCaixaP3.grid(column=1, row=17)

labelP3Min = tk.Label(text="Jogada Mínima:",master=frameInput)
labelP3Min.grid(column=0, row=18)
varP3Min = tk.Entry(master=frameInput)
varP3Min.insert(tk.END,"1.0")
varP3Min.grid(column=1, row=18)

labelP3Max = tk.Label(text="Jogada Máxima:",master=frameInput)
labelP3Max.grid(column=0, row=19)
varP3Max = tk.Entry(master=frameInput)
varP3Max.insert(tk.END,"5.0")
varP3Max.grid(column=1, row=19)





tk.Button(frameInput, text="Iniciar", command=lambda: plot(1, caixa)).grid(column=0, row=20, pady=10, padx=10)

plot(99, caixa)

canvas = FigureCanvasTkAgg(fig, master=framePlot)
canvas.get_tk_widget().pack()






frameInput.pack(side=tk.LEFT)
framePlot.pack(side=tk.LEFT)

root.title("SuperCoinHouse")

root.mainloop()