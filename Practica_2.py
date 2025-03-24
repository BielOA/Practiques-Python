print("Pots seure davant?")
edat = int(input("Indica la teva edat: "))
altura = int(input("Indica la teva estatura (en cm): "))
if edat < 10 or altura < 120:
    print("NO POTS SEURE AL DAVANT")
else:
    print("SÍ POTS SEURE AL DAVANT")