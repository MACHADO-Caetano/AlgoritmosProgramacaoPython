'Código mais avançado, utilização de funções, cálculo de notas e média ponderada, com uso de listas; Segunda parta da avaliação final do semestre, com mais detalhes na elaboração do código.'
def ponderada(lista_de_notas,lista_de_pesos):
    if len(lista_de_notas) != len(lista_de_pesos) or len(lista_de_notas) == 0:
        print(f'Erro, a quantidade de notas não compactua com a quantidade de peso, reinicie o programa.')
        return None
    else:
        notas = sum([nota * peso for nota, peso in zip(lista_de_notas, lista_de_pesos)])
        pesos = sum(lista_de_pesos)
        final = notas / pesos
        print(f'A média ponderada das notas é {final}.')
        
lista_de_notas = []
lista_de_pesos = []
loop_Nota = True
loop_Peso = True
try:
    while loop_Nota == True:
        lista_de_notas.append(float(input('Insira a nota: \n')))
        again= input('Deseja adicionar mais uma nota? (S/N)\n')
        again= again.upper()
        if again == 'S':
            loop_Nota=True
        elif again == 'n' or again == 'N':
            loop_Nota=False
        else:
            print('Opção inválida, tente novamente')
            again= input('Deseja adicionar mais uma nota? (Sim/Não)\n')
    while loop_Peso == True:
        try: 
            lista_de_pesos.append(float(input('Insira o peso: \n')))
            again2 = input('Deseja adicionar mais alguma informação de peso? (S/N)\n')
            if again2 == 's' or again2 == 'S':
                loop_Peso=True
            elif again2 == 'n' or again2 == 'N':
                loop_Peso=False
            else:
                print('Opção inválida, tente novamente')
                again= input('Deseja adicionar mais uma nota? (Sim/Não)\n')
        except ValueError:
            print('Erro, tente novamente.')
        except:
            print('Erro, tente novamente.')
    ponderada(lista_de_notas,lista_de_pesos)
except ValueError:
    print('Erro, tente novamente.')
except:
    print('Erro, tente novamente.')
    

