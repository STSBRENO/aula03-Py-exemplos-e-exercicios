# calcular IMC
peso = float(input("digite seu peso Kg:"))
altura = float(input("digite a sua altura:"))
imc = peso/ (altura**2)
if(imc<18):
    print("voce esta abaixo do peso")
elif(imc>18.5 and imc ==24.9):
    print("voce esta no peso ideal")
elif(imc>=25):
    print("sobrepeso")
else:
    print("obesidade")