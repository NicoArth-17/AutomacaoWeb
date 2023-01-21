# Passo 1: Pegar cotação do dólar
# Passo 2: Pegar cotação do euro
# Passo 3: Pegar cotação do ouro
# Passo 4: Importar a base de dados e atualizar
# Passo 5: Recalcular os preços
# Passo 6: Exportar a base atualizada


from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Comando para habilitar o teclado para pressionar teclas

navegador = webdriver.Chrome() # Criando um navegador chrome

# PASSO 1 - Pegar cotação do dólar

# 1.1 - Entrar no google
navegador.get('https://www.google.com/')

# 1.2 - Pesquisar cotaçao
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotaçao dolar')
# xpath -> Identificador de cada elemento
# .find_element() -> Encontrar elemento
# .send_keys() -> Escrever
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) 
# .send_keys(Keys.ENTER) -> Pressionar enter

# 1.3 - Selecionar o valor
cotDolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
# get_attribute() -> Pegar informações

print(cotDolar)



# PASSO 2 - Pegar cotação do euro

# 2.1 - Entrar no google
navegador.get('https://www.google.com/')

# 2.2 - Pesquisar cotaçao
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotaçao euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) 

# 2.3 - Selecionar o valor
cotEuro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotEuro)



# PASSO 3 - Pegar cotação do ouro

# 3.1 - Entrar no site de cotaçao do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')

# 3.3 - Selecionar o valor
cotaçaoOuro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')

cotOuro = cotaçaoOuro.replace(',','.')
# .replace -> Formata fazendo uma substituição, no caso a VÍRGULA pelo PONTO

print(cotOuro)

navegador.quit() # Fechar navegador

# PASSO 4 - Importar a base de dados e atualizar

# 4.1 - Importar
import pandas as pd
tabela = pd.read_excel(r'C:\Users\mobishopgamer\Documents\Estudo\CursoEmVideo\Python\IntensivãoPython\ProjetoAutomaçaoWeb\Produtos.xlsx')

# 4.2 - Atualizar cotação dolar
tabela.loc[tabela['Moeda']=='Dólar', 'Cotação'] = float(cotDolar)
# .loc[lin, col] -> Localizar na tabela
# tabela['Moeda']=='Dólar' -> Linha delecionada onde todo lugar na coluna 'Moeda' for igual a 'Dolar'

# 4.2 - Atualizar cotação euro
tabela.loc[tabela['Moeda']=='Euro', 'Cotação'] = float(cotEuro)

# 4.3 - Atualizar cotação ouro
tabela.loc[tabela['Moeda']=='Ouro', 'Cotação'] = float(cotOuro)

# PASSO 5 - Recalcular os preços

# 5.1 - Preço de compra
tabela['Preço de Compra'] = tabela['Cotação'] * tabela['Preço Original']

# 5.2 - Preço de venda
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

# PASSO 6 - Exportar a base atualizada

tabela.to_excel(r'C:\Users\mobishopgamer\Documents\Estudo\CursoEmVideo\Python\IntensivãoPython\ProjetoAutomaçaoWeb\ProdutosAtualizados.xlsx', index=False)
# index=False -> Exporta a tabela sem o índice da linha 