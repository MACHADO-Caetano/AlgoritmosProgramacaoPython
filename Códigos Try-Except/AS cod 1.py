'Código de listagem e contagem de aparição de números em uma lista, com utilização de função; Este foi a primeira parte da avaliação final do semestre, onde já apresenta um avanço em relação aos primeiros códigos, no quesito, tratamento de entrada de dados.'
def ocorrencias(lista_de_numbers, numeroparaverificar):
    cont = 0
    for num in lista_de_numbers:
        if num == numeroparaverificar:
            cont += 1
    return cont

def codigo():
    while len(lista_de_numbers) <= 9:
        numero = int(input('Insira um número para a lista: \n'))
        lista_de_numbers.append(numero)
    numeroparaverificar = int(input('Selecione o número para ver quantas vezes ele aparece: \n'))
    contagem = ocorrencias(lista_de_numbers, numeroparaverificar)
    print(f'O número {numeroparaverificar} apareceu {contagem} vezes na lista')
lista_de_numbers = []
try:
    codigo()
except ValueError:
    print("Erro")
    try:
        codigo()
    except:
        print('Insira um valor válido!')
except:
    print('Erro2')
    try:
        codigo()
    except:
        print('Insira um valor válido!')

