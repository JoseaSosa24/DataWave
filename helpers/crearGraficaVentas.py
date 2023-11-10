import pandas as pd
import matplotlib.pyplot as plt


# graficando un dataframe con MATPLOTLIB
def graficar(dataFrame,imgGrafica,xLabel,yLabel,title,xTicks,tamX=5,tamY=10):
    dataFrame["NumeroOrden"] = dataFrame["NumeroOrden"].astype(str)
    colores = ['blue', 'green', '#EFEC1B', 'orange', 'purple' ]
    plt.figure(figsize=(tamX,tamY))
    plt.bar(dataFrame["NumeroOrden"],dataFrame["Costo"], color=colores)
    
    plt.savefig(imgGrafica)
    
    #Personalizando la gráfica
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.xticks(rotation = xTicks)
    

   