import matplotlib.pyplot as plt
from Graphs import anos, df

# Criação dos subplots (2 colunas e 2 fileiras)
fig, axs = plt.subplots(2,2, figsize = (10, 8))
fig.subplots_adjust(hspace = 0.4, wspace = 0.3)

# Título geral dos gráficos
fig.suptitle("Imigração dos quatro países da América do Sul para o Canadá\n1980 a 2013")

# Gráfico 1
axs[0,0].plot(df.loc["Brazil", anos])
axs[0,0].set_title("Brasil")

# Gráfico 2
axs[0,1].plot(df.loc["Colombia", anos])
axs[0,1].set_title("Colômbia")

# Gráfico 3
axs[1,0].plot(df.loc["Argentina", anos])
axs[1,0].set_title("Argentina")

# Gráfico 4
axs[1,1].plot(df.loc["Peru", anos])
axs[1,1].set_title("Peru")

# Para cada gráfico gerado, será definido um espaço de 5 entre seus valores no eixo X (anos)
for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))

# Para cado gráfico gerado, será definido um nome para seus eixos X e Y
for ax in axs.flat:
    ax.set_xlabel("Ano")
    ax.set_ylabel("Número de imigrantes")

# Para cada gráfico gerado, será definido 
for ax in axs.ravel():
    ax.set_ylim(0,7000)

plt.show()