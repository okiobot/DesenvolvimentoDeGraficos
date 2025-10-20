from Graphs import *

# Tradução dos países 
traducao = {"Guyana" : "Guiana",
            "Colombia" : "Colômbia",
            "Brazil" : "Brasil",
            "Venezuela (Bolivarian Republic of)" : "Venezuela",
            "Ecuador" : "Equador",
            "Uruguay" : "Uruguai",
            "Bolivia (Plurinational State of)" : "Bolívia",
            "Paraguay" : "Paraguai"}

# Filtro que adquire apenas os países definidos (neste caso, apenas países da América do Sul)
america_sul = df.query('Region == "South America"')

# Esta parte organiza as informações adquiridas pelo seu total de forma ascendente e, depois, renomeia de acordo com as traduções fornecidas anteriormente
america_sul_sorted = america_sul.sort_values("Total", ascending = True)
america_sul_sorted = america_sul_sorted.rename(index = traducao)

# Cores utilizadas no gráfico
# Apenas uma das listas deve ser utilizada, a primeira é melhor para demonstrar todos os países, já a segunda, para destacar apenas o Brasil

#cores = ["royalblue", "orange", "forestgreen", "orchid", "purple", "brown", "slateblue", "gray", "olive", "navy", "teal", "tomato"]
cores = []

# Loop utilizado para destacar o Brasil com a cor verde
for pais in america_sul_sorted.index:
    if pais == "Brasil":
        cores.append("green")

    else:
        cores.append("silver")

fig, ax = plt.subplots(figsize = (12,5))

# Para gerar um código de barras vertical, basta remover o h de 'barh'
ax.barh(america_sul_sorted.index, america_sul_sorted["Total"], color = cores)

ax.set_title("Imigração dos países da América do Sul para o Canadá\n 1980 a 2013", fontsize = 18)

ax.set_xlabel("Número de imigrantes", fontsize = 14)
ax.set_ylabel("")

ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)

for i, v in enumerate(america_sul_sorted["Total"]):
    ax.text(v + 20, i, str(v), color = "black", fontsize = 10, va = "center")

# Remove a caixa externa
ax.set_frame_on(False)

# Remove o eixo X
ax.get_xaxis().set_visible(False)

# Remove os pequenos traços ao lado dos elementos no eixo Y
ax.tick_params(axis = "both", which = "both", length = 0)

plt.show()