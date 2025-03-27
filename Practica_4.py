num1 = int(input("Introdueix un valor: "))
num2 = int(input("Introdueix un segon valor: "))
num3 = int(input("Introdueix un tercer valor: "))

if num1 > num2 and num3:
    print(f"{num1} és el valor més gran")
elif num2 > num1 and num3:
    print(f"{num2} és el valor més gran")
elif num3 > num1 and num3:
    print(f"{num3} és el valor més gran")