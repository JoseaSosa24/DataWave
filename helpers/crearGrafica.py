import matplotlib.pyplot as plt


# graficando un dataframe con MATPLOTLIB
def graficar(dataFrame,imgGrafica,xColumn, yColumn,xLabel,yLabel,title,xTicks,tamX=20,tamY=15):
    dataFrame[xColumn] = dataFrame[xColumn].astype(str)
    colores = ['#C0C0C0', '#808080', '#000000' ]
    plt.figure(figsize=(tamX,tamY))
    plt.bar(dataFrame[xColumn],dataFrame[yColumn], color=colores)
    
    #Personalizando la gráfic
    plt.xlabel(xLabel, fontsize=25)
    plt.ylabel(yLabel, fontsize=25)
    plt.title(title, fontsize=25)
    plt.xticks(rotation = xTicks, fontsize=25)
    plt.yticks(fontsize=25)
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig(imgGrafica)
    #plt.show()
    
""" def personalizarGrafico(xLabel, yLabel, title, xTicks,imgGrafica):
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.xticks(rotation=xTicks)     """