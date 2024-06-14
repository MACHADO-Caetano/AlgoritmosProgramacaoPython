print("Vamos organizar um Happy Hour! Para isso, vamos precisar saber quantas pessoas irão participar conosco, e ainda, quantos litros deveremos compras.\n")
man=int(input("Informe, quantos homens participarão do evento:\n"))
woman=int(input("Informe, quantas mulheres participaraão do evento:\n"))
chopp_man = man * 2
chopp_woman = woman * 1.5
total = chopp_man + chopp_woman
print(f"A quantidade de chopp que vamos precisar para o evento será: {total}")