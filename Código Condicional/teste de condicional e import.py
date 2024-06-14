'''Pequeno Jogo de Adivinhar Números, com importação de biblioteca, fiz este durante um curso paralelo com a faculdade'''
import random
jogo='S'
while jogo == 'S':
    print("Vou pensar em um número, quero que tentes adivinhar em que número estou pensando... \n Este número está entre 0 e 5.")
    nums = [0, 1, 2, 3, 4, 5]
    num = random.choice(nums)
    escolha = int(input("Em que número estou pensando? \n"))
    from time import sleep
    print("Processando...")
    sleep(3)
    if escolha == num:
        print(f"Você acertou o número em que pensei: {num}. Você venceu!!!")
        jogo=str(input("Você deseja jogar novamente (S/N)"))
    else:
        print(f"Você errou o número {num}, em que pensei... eu venci!")
        jogo=str(input("Você deseja jogar novamente (S/N)"))
