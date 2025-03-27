def segons_hores(segons):
    hora = segons // 3600
    minuts = (segons % 3600) // 60
    segons_rest = segons % 60
    return hora, minuts, segons_rest
segons = int(input("Introdueix una hora en segons: "))

hora, minuts, segons_rest = segons_hores(segons)
print(f"L'hora actual és {hora} hores {minuts} minuts i {segons_rest} segons")