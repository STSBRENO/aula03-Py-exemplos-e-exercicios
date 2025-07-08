numero = int(input("digite um numero:"))
numero1 = int(input("digite outro numero:"))
if(numero > numero1):
    print(f"o maior numero é {numero}")
elif(numero == 0 and numero1 == 0):
    print("voce digitou dois numeros zeros")
else:
    print(f"o maior numero é {numero1}")