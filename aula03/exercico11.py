#pode dirigir 
podeDirigir = (input("voce pode dirigir (sim) ou (não):"))
idade = int(input("digite a sua idade:"))
if(idade>=18 & podeDirigir == "sim"):
    print("liberado")
else:
    print("volte ano que vem")