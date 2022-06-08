from matplotlib import pyplot as plt
import pandas as pd
import os
print(os.getcwd())
def getDicEnvelope(f):
    dic = {}
    dic["Nome"] = "envelope"

    for tipo in f.readline().replace('\n', '').split(' '):
        dic[tipo] = []
    linhas = []
    for linha in f.readlines():
        linha = linha.replace('\n', '').replace('  ', ' ').split(" ")
        linhas.append(linha)
    for l in linhas:
        dic["Temp"].append(l[0])
        dic["P_Vapor"].append(float(l[1]))
        dic["Z_Liq"].append(float(l[2]))
        dic["Fug_Liq"].append(float(l[3]))
        dic["Vol_Liq"].append(float(l[4]))
        dic["H_Liq"].append(float(l[5]))
        dic["S_Liq"].append(float(l[6]))
        dic["Z_Vap"].append(float(l[7]))
        dic["Fug_Vap"].append(float(l[8]))
        dic["Vol_Vap"].append(float(l[9]))
        dic["H_Vap"].append(float(l[10]))
        dic["S_Vap"].append(float(l[11]))

    return dic

def getDict(f, nome):
    dic = {}
    for tipo in f.readline().replace('\n', '').split(' '):
        dic[tipo] = []

    linhas = []
    for linha in f.readlines():
        linha = linha.replace('\n', '').replace('  ', ' ').split(" ")
        linhas.append(linha)

    for l in linhas:
        dic["Fase"].append(l[0])
        dic["Temp"].append(float(l[1]))
        dic["Pres"].append(float(l[2]))
        dic["Z"].append(float(l[3]))
        dic["Fug"].append(float(l[4]))
        dic["Vol"].append(float(l[5]))
        dic["Ental"].append(float(l[6]))
        dic["Entro"].append(float(l[7]))
    
    dic["Nome"] = "Isoterma " + str(dic["Temp"][0]) + "K"

    return dic

p = os.getcwd()

envelope = getDicEnvelope(open('./envelope/envelope.dat', "r"))

files = os.listdir('./isotermas/')
dicts = []
for file in files:
    nome = file
    nome = nome[:8].capitalize() + " " + nome[8:].capitalize() + "K"
    dicts.append(getDict(open('./isotermas/'+file, "r"), nome.replace('.dat', '')))


n = input("Qual o nome da substância?\n")

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(envelope["Vol_Liq"], envelope["P_Vapor"], label="Envelope liquido")
ax.plot(envelope["Vol_Vap"], envelope["P_Vapor"], label="Envelope vapor")
for dic in dicts:
    ax.plot(dic["Vol"], dic["Pres"], label=dic["Nome"])
ax.legend()
plt.xscale("log")
plt.title(f"Diagrama P x V ({n.capitalize()})")
plt.xlabel("Volume molar (m³/mol)")
plt.ylabel("Pressão (bar)")
fig.savefig("Gráfico Gerado")