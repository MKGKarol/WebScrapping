import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Recebe a url a ser analisada
url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022"

# Abre a url e puxa o html em string
html = urlopen(url)

# Realiza o parse do html 
bs = BeautifulSoup(html, 'html.parser')

# Pega todas as linhas cuja a tag seja "tr" e com a classe "expand-trigger"
linhas = bs.find_all('tr', {'class':'expand-trigger'})

# Vetores para armazenamendo dos dados
posicao, nome = [], []

for i in linhas:
    # Pega todos os dados dentro da tag "td"
    children = i.findChildren("td")
    # Difide as informações utilizando o \n
    output = children[0].text.split('\n')
    # adiciona os dados de acordo com a posição desejada
    posicao.append(output[2])
    # adiciona os dados de acordo com a posição desejada
    nome.append(output[4])

# Formata os dados em DataFrame utilizando o Panda
df = pd.DataFrame({'Posição': posicao, 'Time': nome})
df.head()

# Exibe os dados no Console
print(df)