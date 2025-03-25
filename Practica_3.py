def hores_segons(hores, minuts, segons):
    return hores*3600 + minuts*60 + segons

hores = int(input("Introdueix l'hora actual: "))
minuts = int(input("Intrdueix els minuts actuals: "))
segons = int(input("Introdueix les segons acruals: "))

total = hores_segons(hores, minuts, segons)
print("l'hora actual en segons és", total)