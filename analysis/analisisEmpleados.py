import pandas as pd

from helpers.crearCSVEmpleados import crearCSVEmpleados
from helpers.crearTablaHTML import crearTabla
from helpers.crearGrafica import graficar

from data.empleado import Empleado  

empleados = Empleado()
lista = empleados.generar_empleado(2000)
# 1. Crear un CSV con los datos de los empleados
crearCSVEmpleados(lista, 'empleados.csv')

# 2. Cargar la fuente de datos y crear un DataFrame con pandas
empleadosDataFrame = pd.read_csv('data/empleados.csv', encoding='latin-1')
crearTabla(empleadosDataFrame, 'tablaempleados')
#print(empleadosDataFrame)

# 3. Explorar los datos (puedes realizar operaciones de análisis y filtrado aquí)
#examen1 = empleadosDataFrame.head()
#examen2 = empleadosDataFrame.tail()
#examen3 = empleadosDataFrame.head(20)
#examen4 = empleadosDataFrame.info()
#examen5 = empleadosDataFrame.describe()
#examen6 = empleadosDataFrame.tail(50)

# 4. Filtrar y ordenar (limpiar) según tus necesidades

filtroUno = empleadosDataFrame.query("(Edad<24)")
filtroEmpleado = filtroUno[['Nombre','Cargo','Apellido']]
#print(filtroEmpleado)

filtroUno = empleadosDataFrame.query("(Edad>58)")
filtroEmpleadoDos = filtroUno[['Nombre','Cargo','Apellido']]
#print(filtroEmpleadoDos)

filtroUno = empleadosDataFrame.query("(Cargo == 'Desarrollador')")
filtroEmpleadoTres = filtroUno[['Nombre','Cargo','Apellido']]
#print(filtroEmpleadoTres)

filtroUno = empleadosDataFrame.query("(Salario>2500000)")
filtroEmpleadoCuatro = filtroUno[['Nombre','Cargo','Apellido']]
#print(filtroEmpleadoCuatro)

""" crearTabla(filtroEmpleado,'empleadosJovenes')
crearTabla(filtroEmpleadoDos,'empleadosMayores')
crearTabla(filtroEmpleadoTres,'empleadosDesarroladores')
crearTabla(filtroEmpleadoCuatro,'salariosAltos') """

# 6. Presentar y explorar los datos
EmpleadosMasGanan = empleadosDataFrame.nlargest(10, 'Salario')
print(EmpleadosMasGanan)

# graficando un dataframe con MATPLOTLIB
graficar(EmpleadosMasGanan, "figuras/barrasEmpleados.png","ID","Salario","Identificación",
"Salario",
"Los empleados que mas ganan",
45)