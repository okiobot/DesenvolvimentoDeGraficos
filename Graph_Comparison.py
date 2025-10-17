import matplotlib.pyplot as plt
from Graphs import dados_brasil

# Criação de subplots para gráficos diferentes
fig, axs = plt.subplots(1, 2, figsize = (15,5))

# Nomes dos eixos X e Y, respectivamente
axs[0].plot(dados_brasil["Ano"], dados_brasil["Imigrantes"])

# Definição das características do primeiro gráfico (linhas)
axs[0].set_title("Imigração do Brasil para o Canadá\n1980 a 2013")
axs[0].set_xlabel("Ano")
axs[0].set_ylabel("Número de imigrantes")
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid()

# Definição das características do segundo gráfico (caixas)
axs[1].boxplot(dados_brasil["Imigrantes"])
axs[1].set_title("Gráfico de caixas da imigração do Brasil para o Canadá\n 1980 a 2013")
axs[1].set_xlabel("Brasil")
axs[1].set_ylabel("Número de imigrantes")
axs[1].grid()

# Informações dos dados adquiridos
print(dados_brasil.describe())

# Visualização dos gráficos
plt.show()