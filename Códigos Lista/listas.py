'Pequeno e simples algoritmo utilizando listas e menu de opções'
frutas=[]
opcao=""
while opcao !=0:
    print("1 - Para add frutas")
    print("2 - Para remover frutas")
    print("3 - Para quantificar frutas")
    print("4 - Para mostrar sua lista")
    print("0 - Para finalizar o programa")
    opcao=int(input("Digite aqui: "))
    if opcao ==1:
        frutas.append(input("Qual fruta você deseja adicionar?\n"))
        print("Fruta adicionada!")
    elif opcao==2:
        frutas.remove(input("Qual fruta desejas remover?\n"))
    elif opcao==3:
        print(f"Tamanho da lista: {len(frutas)}")
    elif opcao ==4:
        for fruta in frutas:
            print(f"Frutas: {fruta}")
    elif opcao==0:
        print("Processo encerrado")
    else:
        print("Comando inválido, insira novamente")
