ana = 0 
bruno = 0
carlos = 0

votos = []

while True:
    voto = input("Digite o nome do candidato (fim para encerrar): ")
    
    if voto.lower() == "fim":
        break  

    voto = voto.capitalize()

    if voto in ["Ana", "Bruno", "Carlos"]:
        votos.append(voto)  
    else:
        print("Voto inválido. Tente novamente.")

for voto in votos:
    if voto == "Ana":
        ana = ana + 1
    elif voto == "Bruno":
        bruno = bruno + 1
    elif voto == "Carlos":
        carlos = carlos + 1

maior = ana
if bruno > maior:
    maior = bruno
if carlos > maior:
    maior = carlos

print('\nResultado da votação: ')
print(f"Ana: {ana} votos")
print(f"Bruno: {bruno} votos")
print(f"Carlos: {carlos} votos")

vencedores = []

if ana == maior:
    vencedores.append("Ana")
if bruno == maior:
    vencedores.append("Bruno")
if carlos == maior:
    vencedores.append("Carlos")


if len(vencedores) > 1:
    print("Houve um empate entre os candidatos.")
else:
    print(f"O vencedor é: {vencedores[0]}")