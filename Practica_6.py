import pandas as pd
import matplotlib.pyplot as plt

def notes_alumnes(Notes_alumnes_practica6):
    try:
        alumnes = pd.read_excel(Notes_alumnes_practica6)
        notes = [col for col in alumnes.columns if col.startswith('Nota')]
        alumnes['Mitjana'] = alumnes[notes].mean(axis=1).round(2)
        return alumnes
    except Exception as e:
        print("Error en llegir l'arxiu Excel:", e)
        return pd.DataFrame()

def qual_quant(m):
    m = float(m)

    if m < 5.00: return "No assoliment"
    elif m < 7.00: return "Assoliment Satisfactori"
    elif m < 9.00: return "Assoliment Notable"
    else: return "Assoliment Excel·lent"

def histograma(alumnes):
    contar = alumnes['Qualificació'].value_counts().reindex(
        ["No assoliment", "Assoliment Satisfactori", "Assoliment Notable", "Assoliment Excel·lent"],
        fill_value=0
    )
    colors = ["#f03629", "#f0da16", "#a7f016", "#41f011"]

    plt.bar(contar.index, contar.values, color=colors, width=0.6)
    plt.title ("Qualificacions de la classe")
    plt.xlabel("Qualificació")
    plt.ylabel("Nombre d'alumnes")
    plt.xticks(rotation=10)
    plt.savefig('histograma_qualificacions.png')
    plt.close()

def mill_pitj(alumnes):
    notes_cols = [col for col in alumnes.columns if col.startswith('Nota')]

    millor = alumnes.loc[alumnes['Mitjana'].idxmax()]
    pitjor = alumnes.loc[alumnes['Mitjana'].idxmin()]

    plt.plot(range(1, 7), millor[notes_cols], label=f"Millor: {millor['Alumnes']}", marker='o', color='green')
    plt.plot(range(1, 7), pitjor[notes_cols], label=f"Pitjor: {pitjor['Alumnes']}", marker='o', color='red')

    plt.title("Evolució de les notes del millor i pitjor alumne")
    plt.xlabel("Avaluació")
    plt.ylabel("Nº nota")
    plt.xticks(range(1, 7), notes_cols)
    plt.ylim(0, 11)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('evolucio_millor_pitjor.png')
    plt.close()

arxiu = "Notes_alumnes_practica6.xlsx"
alumnes = notes_alumnes(arxiu)

if not alumnes.empty:
    alumnes['Qualificació'] = alumnes['Mitjana'].apply(qual_quant)
    histograma(alumnes)
    print("El grafic 'Qualificacions de la classe' s'ha desat com 'histograma_qualificacions.png'")
    mill_pitj(alumnes)
    print("El grafic 'Evolució de les notes del millor i pitjor alumne' s'ha desat com 'evolucio_millor_pitjor.png'")
else:
    print("No s'han pogut carregar les dades.")