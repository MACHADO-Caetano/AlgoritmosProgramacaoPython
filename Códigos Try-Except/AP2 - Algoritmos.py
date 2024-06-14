'Código com utilização de listas, um pouco mais lapidado que o anterior'
lista=[]
option=""
try:
    while option != 0:
        print("Opção 01 - Digite 1 para adicionar um produto à sua lista: ")
        print("Opção 02 - Digite 2 para adicionar um produto na posição à sua escolha: ")
        print("Opção 03 - Digite 3 para remover um produto da sua lista: ")
        print("Opção 04 - Digite 4 para listar seus produtos na lista: ")
        print("Opção 0 - Digite 0 para encerrar o programa.")
        option=(int(input("Insira a opção: ")))
        if option == 1:
            existe=False
            ad1=str(input("Digite o item que você vai adicionar: "))
            for i in range (0, len(lista)):
                if (lista[i] == ad1):
                    existe=True
            if existe == False:
                lista.append(ad1)
                print("Adicionado com sucesso!")
            elif existe == True:
                print("Não foi possível adicionar o produto, pois o mesmo já está em sua lista, tente novamente.")       
        elif option == 2:
            existe1=False
            pos=int(input("Digite a posição que você vai adicionar: "))
            add=input("Digite o item que você vai adicionar: ")
            for ia in range (0, len(lista)):
                if (lista[ia] == add):
                    existe1=True
            if pos <= len(lista) and existe1 == False:
                lista.insert(pos,add)
                print(f"Seu item {add} foi adicionado na posição {pos}!")
            else: 
                print("Esta opção não pode ser concluída, tente novamente.")
        elif option == 3:
            lista.remove(input("Digite o item que queiras remover: "))
            print("Item removido.")
        elif option == 4:
            print(f"Sua lista atual está: {lista}")
        elif option == 0:
            print("Programa encerrado.")
except:
    print("Inválido, tentar novamente")