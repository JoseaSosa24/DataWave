import random

import random


class Ventas:

    def __init__(self):
        ## contructor vacío
        pass

    def generar_ventas(self, cantidad):
        
        ventas = []
        for _ in range(cantidad):

            numeroOrden=random.randint(0,500000)
            cliente=random.choice(['Andres', 'Ana', 'Isabel', 'Pablo','Juan','kelly','Mauricio','Manuela','Veronica','Raul'])
            costo = random.randint(150000, 600000)
            orden = [numeroOrden, cliente, costo]
            ventas.append(orden)
        return ventas      
# Armar lista de empleados
# llevar la lista a análisis
#Cnvertir los la lita de empleados en dataframe
# Crear un página que me lleve la dashboard
# solo si se gana más de 6 millons se aplicar retención en la fuente





# desarrollador junior 
# desarrollador intermedio 
# desarrollador avanzado  
# arquitecto

#SOLO si se ganan mas de 6 millones se aplica retencion en la fuente del 10%
