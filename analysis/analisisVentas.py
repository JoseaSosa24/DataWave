import pandas as pd

from helpers.crearCSVVentas import crearCSVVentas
from helpers.crearTablaHTML import crearTabla

from data.ventas import ventas

#1. Crear un CSV con los datos de las ventas
crearCSVVentas(ventas,'ventas.csv')

"#2 Cargo la fuente de datos y con pandos PANDAS creo un DATAFRAME"
ventasDataFrame=pd.read_csv('data/ventas.csv')
crearTabla(ventasDataFrame, 'tablaventas')

#print(ventasDataFrame)

#3.Explorar los datos
# examen1 = ventasDataFrame.head()
# examen2 = ventasDataFrame.tail()
# examen3 = ventasDataFrame.head(20)
# examen4 = ventasDataFrame.info()
# examen5 = ventasDataFrame.describe()
# examen6 = ventasDataFrame.tail(50)

#4.Filtrar y ordenar (limpiar)

filtroUno = ventasDataFrame.query("(Costo>500000)")
totalVentas = filtroUno[['NumeroOrden','Costo']]
#print(totalVentas)

filtroDos = ventasDataFrame.query("(Costo>100000) and (Costo<250000)")
totalVentas2 = filtroDos[['NumeroOrden','Costo']]
#print(totalVentas2)


#5. aplicar modelos estadísticos

#6. Presentar y explorar los datos
#crearTabla(totalVentas,'ventasAltosCostos')
#crearTabla(totalVentas2,'ventasBajoCosto')