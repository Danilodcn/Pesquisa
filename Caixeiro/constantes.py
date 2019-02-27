try:
    from Caixeiro import funcoes
except:
    import funcoes

N_CIDADES = 10
COORDENADAS = funcoes.geraCoordenadas(N_CIDADES)
CIDADE_PARTIDA = 0
TAM_POPULACAO = 100

#AG
N_CROSSOVER = int(TAM_POPULACAO * 1)
N_MUTACAO = int(TAM_POPULACAO * 0.15)
MAX_GERACOES = 100
MUDANCA_MENOR = 5
