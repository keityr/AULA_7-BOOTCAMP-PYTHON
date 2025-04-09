import csv 

path_arquivo = 'products_with_seller.csv'

def abrir_arquivo(nome_do_arquivo:str) -> list[dict]:
    '''
    Funcao que abre e le o arquivo csv e retorna  uma lista de dicionarios '''

    lista_csv = []
    with open(nome_do_arquivo, mode = 'r', encoding='utf-8') as arquivo:
        lista = csv.DictReader(arquivo)
        for linha in lista:
            lista_csv.append(linha)

    return list(lista_csv)


def faturamento_total(arquivo: list):
    ''' Funcao que calcula o faturamento total das vendas (preco * quantidade vendida)'''
    faturamento = 0 
    for linha in arquivo:
        preco = float(linha['price'])
        qtd_vendida = int(linha['quantity_sold'])
        faturamento +=  preco * qtd_vendida

    return faturamento
       

def soma_dos_precos(arquivo: list[dict]) -> float:
    
    '''Funcao que soma todos os precos'''
    valor_total = 0

    for produto in arquivo:
        valor_total += float(produto.get("price"))
    return valor_total

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    '''
    Funcao que filtra produtos onde entrega = True '''

    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get('shipment') == "True":
            lista_produtos_filtrados.append(produto)

    return lista_produtos_filtrados


lista_de_produtos = abrir_arquivo(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
soma_total = soma_dos_precos(lista_de_produtos)
faturamento = faturamento_total(lista_de_produtos) 
print(soma_total)
print(f'{faturamento:.2f}')
print(produtos_entregues)