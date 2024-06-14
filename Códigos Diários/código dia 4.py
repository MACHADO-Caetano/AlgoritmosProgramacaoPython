print("Vamos ver quanto de gasto em sacos de ração o Sky consome!\n")
gramas = float(input("Primeiro, quantas gramas que são colocadas para ele comer, por vez? "))
vezes_dia = int(input("Segundo, quantas vezes ao dia é colocado para ele comer? "))
saco = float(input("E agora, de quantos quilos é o saco que é/vai ser comprado para ele? "))
valor_saco = float(input("Para finalizar, quantos reais são gastos em um saco de ração? "))
resultado_um=gramas*vezes_dia
quant_dias=resultado_um*365
quilos=quant_dias / 1000
quant_saco=quilos / saco
valor=quant_saco *valor_saco
print(f"O valor total, no ano, gasto com ração é: R$ {valor}")

