

# # num_4 = 6
# # num_5 = 4

# def trans_soma (num: float, num1: float ):  
    
#     ''' Soma dois numeros float'''


#     adicao = num + num1
#     return( adicao )
    

# print("*********************")
# print("**Soma de numeros**")
# print("*********************")

# valor_1: float = float(input("Digite um numero: "))
# valor_2: float = float(input("Digite outro numero: "))


# resultado = trans_soma(num = valor_1, num1 = valor_2 )

# print(f'{resultado:.2f}')


# Calcular Média de Valores em uma Lista:

# def calcular_media(elementos):
#     soma = sum(elementos)
#     qtd_elementos = len(elementos)
#     media = soma / qtd_elementos
#     return media

# lista = [3, 4, 5, 6, 70]

# media_elementos = calcular_media(lista)

# print(media_elementos)

#Filtrar Dados Acima de um Limite


# def filtro_acima_limite(valores, limite):
#     lista = []
#     for valor in valores:
#         if valor > limite:
#             lista.append(valor)
#     return(lista)

# print(filtro_acima_limite(valores = [10.5, 3.2, 7.8, 15.0, 2.0, 12.3],
# limite = 7.0))

#Contar Valores Únicos em uma Lista


# from typing import List

# def valor_unico(valores: List[int]) -> int:
#     lista= []
#     for item in valores:
#         if item not in lista:
#             lista.append(item)

#     return(lista)

# print(valor_unico(valores = [1, 5, 5, 4, 7, 2, 1, 7]))

#Converter Celsius para Fahrenheit em uma Lista
# Entradas de teste


# from typing import Dict, List

# def celsius_to_fahrenheit(temperaturas_celsius:List[float]) -> List[float]:
#     return [ (temp * 9/5) + 32 for temp in temperaturas_celsius]

# temperaturas: Dict[str, List[float]] = {
# "temperaturas1": [0, 20, 30, 40],
# "temperaturas2": [-10, 0, 10, 25],
# "temperaturas3": [36.6, 100, -40],
# "temperaturas4": [],
# "temperaturas5": [15.5, 22.8, 37.2] 
# }

# convertidos: List[float]  = []
# for lista in temperaturas.values():
#     convertidos.extend(celsius_to_fahrenheit(lista))

# print(convertidos)

# #Calcular Desvio Padrão de uma Lista



# def desvio_padrao(valores):
#     media = sum(valores) / len(valores)

#     soma_dos_quadrados = 0
#     for valor in valores:
#         diferenca = valor - media
#         soma_dos_quadrados += diferenca ** 2

#     variancia = soma_dos_quadrados / len(valores)

#     import math 
#     desvio_padrao = math.sqrt(variancia)


# #Encontrar Valores Ausentes em uma Sequência

# def valor_ausente(sequencia):
#     lista = set(range(min(sequencia), max(sequencia)+ 1))

#     return(list(lista - set(sequencia)))
    

