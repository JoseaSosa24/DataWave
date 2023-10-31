import pandas as pd

from helpers.crearCSVProductos import crearCSVProductos
from helpers.crearTablaHTML import crearTabla

from data.producto import productos

#1. Crear un CSV con los datos de las ventas
crearCSVProductos(productos,'productos.csv')

"#2 Cargo la fuente de datos y con pandos PANDAS creo un DATAFRAME"
productosDataFrame=pd.read_csv('data/productos.csv')
crearTabla(productosDataFrame, 'tablaproductos')
#print(productosDataFrame)

#3.Explorar los datos
#examen1 = productosDataFrame.head()
#examen2 = productosDataFrame.tail()
#examen3 = productosDataFrame.head(20)
#examen4 = productosDataFrame.info()
#examen5 = productosDataFrame.describe()
#examen6 = productosDataFrame.tail(50)

#4.Filtrar y ordenar (limpiar)

filtroUno = productosDataFrame.query("(Precio_unitario>500000)")
filtroProducto = filtroUno[['Id_producto','Nombre','Precio_unitario']]
#print(filtroProducto)

filtroDos = productosDataFrame.query("(Precio_unitario>0) and (Precio_unitario<250000)")
filtroProductoDos = filtroDos[['Id_producto','Nombre','Precio_unitario']]
#print(filtroProductoDos)

#5. aplicar modelos estadísticos

#6. Presentar y explorar losd datos

