import requests
 
URL = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
resultado = requests.get(URL).json()
tabela = sorted([
    (candidate['nm'], candidate['vap'], candidate['pvap'])
    for candidate in resultado['cand']
    ], key=lambda linha: linha[1], reverse=True) # Ordena por votos
 

for linha in tabela:
    print('\t'.join(linha)+"% \n")