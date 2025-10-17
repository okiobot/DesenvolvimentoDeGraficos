import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo csv/excel para 
df = pd.read_csv("C:\VSCode\GitHub\DesenvolvimentoDeGraficos\canadian_immegration_data.csv")

# Visualização pelo terminal do arquivo lido
print(df)

# Informações do arquivo (quantidade de fileiras e colunas, quantidade de entradas, etc.)
df.info()

# Define a coluna que será procurada pelo nome
df.set_index("Country", inplace = True)

# Produz uma lista do arquivo das entradas do período de tempo entre os calores específicados (1980 à 2014) 
anos = list(map(str, range(1980, 2014)))

# Encontra as entradas que possuem os valores da lista adquiridos anteriormente e busca pelo nome desejado
brasil = df.loc["Brazil", anos]
argentina = df.loc["Argentina", anos]

# Dicionário que cria listas para os valores desejados
brasil_dict = {"Ano" : brasil.index.tolist(), "Imigrantes" : brasil.values.tolist()}
argentina_dict = {"Ano" : argentina.index.tolist(), "Imigrantes" : argentina.values.tolist()}

# Transforma em um data frame os valores encontrados
dados_brasil = pd.DataFrame(brasil_dict)
dados_argentina = pd.DataFrame(argentina_dict)

# Apresenta no terminal
print("Brasil")
print(dados_brasil)

print("-"*100)

print("Argentina")
print(dados_argentina)

# Define o tamanho total do gráfico
plt.figure(figsize=(8,4))

# Adiciona as informações para a formulação do gráfico
plt.plot(dados_brasil["Ano"], dados_brasil["Imigrantes"])
plt.plot(dados_argentina["Ano"], dados_argentina["Imigrantes"])

plt.legend(["Brasil", "Argentina"])

# Título do gráfico
plt.title("Imigração do Brasil para o Canadá")

# Nome do eixo X e Y, respectivamente
plt.xlabel("Ano")
plt.ylabel("Número de imigrantes")

# Marcas dos valores X e Y, respectivamente
plt.xticks(["1980", "1985", "1990", "1995", "2000", "2005", "2010"])
plt.yticks([500, 1000, 1500, 2000, 2500, 3000])

# Adicionar grade para melhor visualização
plt.grid()

# Apresenta o gráfico pelo plomatlib 
plt.show()