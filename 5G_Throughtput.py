import math
import os

# Constants
mcsTableN = [2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8]
mcsTableN2 = [0.2344, 0.377, 0.6016, 0.877, 1.1758, 1.4766, 1.6953, 1.9141, 2.1602, 2.4063, 2.5703, 2.7305, 3.0293, 3.3223, 3.6094, 3.9023, 4.2129, 4.5234, 4.8164, 5.1152, 5.332, 5.5547, 5.8906, 6.2266, 6.5703, 6.9141, 7.1602, 7.4063]
OFDMSymbols = 11  # Number of OFDM symbols
symbolDuration = 0.0005  # Duration of each symbol in seconds
subcarriers = 12  # Number of subcarriers
guard = 4  # Guard interval
totalDataResources = subcarriers * OFDMSymbols  # Total number of data resources
rsrcFreq = 360  # Resource frequency in kHz

def throughput_calculation(modOrder: int, bndWdth: int, DLUL: str, MIMOLayers: int) -> float:
    maxBitsPerSymbol = mcsTableN2[modOrder]  # Maximum number of bits per symbol based on modulation order
    dataCarried = math.floor(totalDataResources * maxBitsPerSymbol)  # Total data carried in the given bandwidth
    rsrcBlocks = math.floor(bndWdth / rsrcFreq) - 4  # Number of resource blocks
    slots1Sec = 1 / symbolDuration  # Number of slots in one second

    if DLUL == "3:1":
        dwnlkSlots = 3 * slots1Sec / 4  # Downlink slots in one second for 3:1 DLUL ratio
    else:
        dwnlkSlots = 4 * slots1Sec / 5  # Downlink slots in one second for 4:1 DLUL ratio

    throughput = dataCarried * rsrcBlocks * dwnlkSlots * MIMOLayers / 1024 / 1024  # Calculating throughput in Mbps
    return throughput

def save_results(texto: str) -> None:
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "Results.txt")
    with open(file_path, "a") as file:
        file.write(texto + "\n")  # Saving the results to a file

def reset_results() -> None:
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "Results.txt")
    if os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass  # Resetting the results file
    else:
        print("File does not exist. No reset needed.")

def main():
    # Values to test
    reset_results()  # Resetting the results file
    modOrder = list(range(27))  # Modulation order: 0 to 27
    bndWdth = [20000, 50000, 100000, 400000]  # Bandwidth: 20, 50, 100, or 400 MHz
    DLUL = ["3:1", "4:1"]  # DLUL ratio: 3:1 or 4:1
    MIMOLayers = [1, 2, 4]  # Number of MIMO layers: 1, 2, or 4

    for mod in modOrder:
        for bnd in bndWdth:
            for dlul in DLUL:
                for mimo in MIMOLayers:
                    throughput = throughput_calculation(mod, bnd, dlul, mimo)  # Calculating throughput for each combination
                    text = f"{' Entradas ':-^20} | {' Valores ':-^20} | {f' throughput ':-^20}\n"
                    text += f"{' MIMOLayers ':^20} | {mimo:^20} | {f' ':^20}\n"
                    text += f"{' bndWdth ':^20} | {bnd:^20} | {throughput:^20}\n"
                    text += f"{' modOrder ':^20} | {mod:^20} | {f' ':^20}\n"
                    text += f"{' DLUL ':^20} | {dlul:^20} | {f' ':^20}\n"
                    print(text)  # Printing the results
                    save_results(text)  # Saving the results to a file

if __name__ == "__main__":
    main()  # Running the main function
