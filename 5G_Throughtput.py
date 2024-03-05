import math

# Constantes do problema:
mcsTableN = [2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8]
mcsTableN2 = [0.2344, 0.377, 0.6016, 0.877, 1.1758, 1.4766, 1.6953, 1.9141, 2.1602, 2.4063, 2.5703, 2.7305, 3.0293, 3.3223, 3.6094, 3.9023, 4.2129, 4.5234, 4.8164, 5.1152, 5.332, 5.5547, 5.8906, 6.2266, 6.5703, 6.9141, 7.1602, 7.4063]
OFDMSymbols = 11 # 14-3
symbolDuration = 0.0005 # 0.5ms
subcarriers = 12
guard = 4
totalDataResources = subcarriers * OFDMSymbols
rsrcFreq = 360 #kHz

def calcula_throughput(modOrder:int, bndWdth:int, DLUL:str, MIMOLayers:int) -> None:

    maxBitsPerSymbol = mcsTableN2[int(modOrder)]
    dataCarried = math.floor(totalDataResources * maxBitsPerSymbol)
    rsrcBlocks = math.floor(int(bndWdth) / int(rsrcFreq)) -4
    slots1Sec = 1 / symbolDuration

    if DLUL == "3:1":
        dwnlkSlots = 3 * slots1Sec / 4
    else:
        dwnlkSlots = 4 * slots1Sec/5


    throughput = int(dataCarried) * int(rsrcBlocks) * int(dwnlkSlots) * int(MIMOLayers) /1024 /1024

    text = ""
    text += f"{' Entradas ':-^20} | {' Valores ':-^20} | {f' throughput ':-^20}\n"
    text += f"{' MIMOLayers ':^20} | {MIMOLayers:^20} | {f' ':^20}\n"
    text += f"{' bndWdth ':^20} | {bndWdth:^20} | {throughput:^20}\n"
    text += f"{' modOrder ':^20} | {modOrder:^20} | {f' ':^20}\n"
    text += f"{' DLUL ':^20} | {DLUL:^20} | {f' ':^20}\n"

    print(text)
    salva_resultados(text)

def salva_resultados(texto:str) -> None:
    with open("C:/Users/mathe/OneDrive/Desktop/Codes/Redes/Resultados.txt", "a") as file:
        file.write(texto)
        file.write("\n")
        file.close()

def reset_resultados() -> None:
    with open("C:/Users/mathe/OneDrive/Desktop/Codes/Redes/Resultados.txt", "w") as file:
        file.write("")
        file.close()

def main():
    # Valores testados
    reset_resultados()
    modOrder = list(range(27)) # ordem da modulação: 0 a 27
    bndWdth = [20000, 50000, 100000, 400000] # largura de banda: 20, 50, 100 ou 400 MHz
    DLUL = ["3:1", "4:1"] # 3:1 ou 4:1
    MIMOLayers = [1, 2, 4] # 1, 2 ou 4 camadas MIMO

    for mod in modOrder:
        for bnd in bndWdth:
            for dlul in DLUL:
                for mimo in MIMOLayers:
                    calcula_throughput(mod, bnd, dlul, mimo)



if __name__ == "__main__":
    main()

