def valors_max(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("Introdueix un valor: "))
num2 = int(input("Introdueix un segon valor: "))
num3 = int(input("Introdueix un tercer valor: "))

max_valor = valors_max(num1, num2, num3)

print(f"El valor més alt és {max_valor}")