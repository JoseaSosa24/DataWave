import random
empleados = []

for _ in range(50):
    id = _+1
    nombre = random.choice(['Andrés', 'Jose', 'Manuela', 'Jhohan'])
    cargo = random.choice(['Gerente', 'Desarrollador', 'Diseñador', 'Analista'])
    edad = random.randint(22,60)
    salario = random.randint(1160000, 20000000)
    retefuente = 0
    
    if salario >= 6000000: 
        retefuente = 0.1
    else:
        retefuente = 0.0
    empleado = {"id": id, "nombre":nombre,"cargo":cargo,"edad":edad,"retefuente":retefuente,"salario":salario}
    empleados.append(empleado)
    
    
print(empleados)
    
           
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
