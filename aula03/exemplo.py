print('vamos votar em um time (1-branco), (2-verde), (3-vermelho)')
nome = input("digite seu nome:")
voto = int(input("digite para qual time vai o seu voto:"))
if(voto--1):
    print(f'{nome} votou no time branco')
elif(voto==2):
    print(f'{nome} votou no time verde')
elif(voto==3):
    print(f'{nome} votou no time vermelho')
else:
    print("voto errado")
print("obrigado pelo seu voto!")