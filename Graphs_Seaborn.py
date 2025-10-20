import seaborn as sns
import matplotlib.pyplot as plt
from Graphs import df

traducao = {"India" : "Índia",
            "United Kingdom of Great Britain and Northern Ireland" : "Reino Unido\n da Grã-Bretanha\n e Irlanda do Norte",
            "Philippines" : "Filipinas",
            "Pakistan" : "Paquistão",
            "United States of America" : "Estados Unidos\n da América",
            "Iran (Islamic Republic of)" : "Irã",
            "Republic of Korea" : "Coreia do Sul",
            "Poland" : "Polônia"}

sns.set_theme(style = "ticks")

top10 = df.sort_values("Total", ascending = False).head(10)
top10 = top10.rename(index = traducao)

def gerar_paleta(palette):
    fig, ax = plt.subplots(figsize = (12,5))
    ax = sns.barplot(data = top10, x = "Total", y = top10.index, orient = "h", hue = top10.index, palette = palette)
    ax.set_title("Países com maior taxa de imigração para o Canadá \n 1980 a 2013", fontsize = 15)  
    ax.set_xlabel("Número de imigrantes")
    ax.set_ylabel("")
    sns.despine()
    plt.show()
       
gerar_paleta("tab10")

