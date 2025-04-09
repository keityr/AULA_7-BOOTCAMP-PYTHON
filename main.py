from desafio import abrir_arquivo, filtrar_produtos_nao_entregues, soma_dos_precos, faturamento_total

path_arquivo = "products_with_seller.csv"


lista_de_produtos = abrir_arquivo(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
soma_total = soma_dos_precos(lista_de_produtos)
faturamento = faturamento_total(lista_de_produtos) 
print(soma_total)
print(f'{faturamento:.2f}')
print(produtos_entregues)