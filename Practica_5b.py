import pandas as pd
import matplotlib.pyplot as plt

def vendes_excel(Valors_Practica_5b):
    try:
        dades = pd.read_excel(Valors_Practica_5b)
        vendes = dades['Vendes'].tolist()
        return vendes
    except Exception as e:
        print("Error en llegir l'arxiu Excel:", e)
        return []

def grafic(vendes):
    plt.plot(range(1, len(vendes) + 1), vendes, marker='o', linestyle='-', color='b')
    plt.xlabel("Mes")
    plt.ylabel("Vendes")
    plt.title("Evolució de les vendes mensuals")
    plt.grid()
    plt.savefig("vendes_graf.png")
    print("El gràfic s'ha desat com 'vendes_graf.png'.")

def mitjana(vendes):
    mitjana_calc = sum(vendes) / len(vendes)
    return mitjana_calc

Valors_Practica_5b = "Valors_Practica_5b.xlsx"
vendes = vendes_excel(Valors_Practica_5b)

if vendes:
    grafic(vendes)
    mitjana_calc = mitjana(vendes)
    print(f"La mitjana de vendes és: {mitjana_calc: .2f}")
else:
    print("No s'han pogut obtenir les dades.")