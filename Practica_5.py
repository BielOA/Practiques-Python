import matplotlib.pyplot as plt

print("Introdueix una sèrie de valors amb les vendes mensuals d'un determinat tipus de producte")
def obtenir_vendes():
    vendes = []
    mes = 1
    while True:
        valor = int(input(f"Introdueix les vendes del mes {mes} (0 si ja has acabat): "))
        if valor == 0:
            break
        vendes.append(valor)
        mes += 1
    return vendes

def grafic(vendes):
    plt.plot(range(1, len(vendes) + 1), vendes, marker='o', linestyle='-', color='b')
    plt.xlabel("Mes")
    plt.ylabel("Vendes")
    plt.title("Evolució de les vendes mensuals")
    plt.grid()
    plt.savefig("vendes_graf.png")
    print("El gràfic s'ha desat com 'vendes_graf.png'.")

vendes = obtenir_vendes()
if vendes:
    grafic(vendes)
else:
    print("No s'han introduït dades de vendes.")