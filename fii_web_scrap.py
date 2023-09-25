import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.fundsexplorer.com.br/ranking"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')

print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))

df = pd.DataFrame(columns=['Fundos', 'Setor', 'Preço Atual', 'Liquidez Diária', 'P/VP', 'Último Dividendo', 'Dividend Yield', 'DY (3M) Acumulado', 'DY (6M) Acumulado',''])