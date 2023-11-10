import matplotlib.pyplot as plt


# graficando un dataframe con MATPLOTLIB
def graficar(dataFrame,imgGrafica,xColumn, yColumn,xLabel,yLabel,title,xTicks,tamX=20,tamY=15):
    dataFrame[xColumn] = dataFrame[xColumn].astype(str)
    colores = ['blue', 'green', '#EFEC1B', 'orange', 'purple' ]
    plt.figure(figsize=(tamX,tamY))
    plt.bar(dataFrame[xColumn],dataFrame[yColumn], color=colores)
    
    #Personalizando la gráfica
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.xticks(rotation = xTicks)
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig(imgGrafica)
    #plt.show()
    
""" def personalizarGrafico(xLabel, yLabel, title, xTicks,imgGrafica):
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.xticks(rotation=xTicks)     """