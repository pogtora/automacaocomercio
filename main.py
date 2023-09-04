# Automatização de Preços de Produtos Online
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://quotes.toscrape.com/' #site para teste

response = requests.get(url)

if response.status_code == 200:
    print('Página acessada com sucesso!')


    soup = BeautifulSoup(response.text, 'html.parser')


    elementos_precos = soup.find_all('span', class_='preco-produto')


    with open('dados_produtos.csv', 'w', newline='') as arquivo_csv:

        campo_nomes = ['Nome do Produto', 'Preço']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campo_nomes)
        escritor_csv.writeheader()


        for elemento_preco in elementos_precos:
            nome_produto = elemento_preco.find_previous('h2').text.strip()
            preco = elemento_preco.text.strip()
            print(f'Nome do Produto: {nome_produto}, Preço: {preco}')

            escritor_csv.writerow({'Nome do Produto': nome_produto, 'Preço': preco})

    print('Dados extraídos e salvos em dados_produtos.csv.')

else:
    print('Não foi possível acessar a página.')





