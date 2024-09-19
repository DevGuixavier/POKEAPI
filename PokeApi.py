import requests

def get_request(numero_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon}"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def pegar_evolucao(url):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{url}"
    resposta = requests.get(url)
    dados = resposta.json()
    url_evolucoes = dados['evolution_chain']['url']
    resposta_evolucao = requests.get(url_evolucoes)
    dados_evolucao = resposta_evolucao.json()
    return dados_evolucao

def pegar_nome_evolucoes(dados_evolucao):
    nomes_evolucao = []
    evolucao_atual = dados_evolucao['chain']

    while evolucao_atual:
        nomes_evolucao.append(evolucao_atual['species']['name'])
        evolucao_atual = evolucao_atual['evolves_to'][0] if evolucao_atual['evolves_to'] else None

    return nomes_evolucao

puxar_num_pokemon = input("Digite o número do Pokémon: ")

dados_da_requisicao = get_request(puxar_num_pokemon)

nome_pokemon = dados_da_requisicao['name']
tipos = [tipo['type']['name'] for tipo in dados_da_requisicao['types']]
movimentos = [move['move']['name'] for move in dados_da_requisicao['moves']]

dados_evolucao = pegar_evolucao(puxar_num_pokemon)
nomes_evolucao = pegar_nome_evolucoes(dados_evolucao)

informacoes_pokemon = {
    "Nome": nome_pokemon.capitalize(),
    "Tipos": ", ".join(tipo.capitalize() for tipo in tipos),
    "Movimentos": ", ".join(move.capitalize() for move in movimentos),
}

print("Info Pokémon:")
for chave, valor in informacoes_pokemon.items():
    print(f"{chave}: {valor}")
