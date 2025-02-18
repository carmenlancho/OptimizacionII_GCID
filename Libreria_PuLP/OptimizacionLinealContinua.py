
# https://pypi.org/project/PuLP/
# https://github.com/coin-or/pulp?tab=readme-ov-file



from pulp import *

###################################################################################
#############                          EJEMPLO 1                      #############
###################################################################################

# Comenzamos creando el modelo
model = LpProblem(name="EjemplitoClase", sense=LpMaximize) # LpMinimize

# Inicializamos las variables
x = LpVariable(name="x", lowBound=0, cat="Continuous")
y = LpVariable(name="y", lowBound=0)
# Algunos ejemplos:
#y = LpVariable("y", cat="Binary")
#x = LpVariable("x", lowBound=0, upBound = 3) 0<=x<=3

# Añadimos restricciones al modelo
model += (2 * x + y <= 20, "restriccion_1")
model += (-4 * x + 5 * y <= 10, "restriccion_2")
model += (-x + 2 * y >= -2, "restriccion_3")
model += (-x + 5 * y == 15, "restriccion_4")

# Añadimos la función objetivo
model += x + 2 * y
# model += lpSum([x, 2 * y]) # otra manera de escribirlo

# Resolvemos el problema
status = model.solve()

# Mostramos por pantalla los resultados
print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

# También podemos ver el valor de las variables así:
value(x)
value(y)

# Información sobre el solver
model.solver


###################################################################################
#############                          EJEMPLO 2                      #############
###################################################################################


# Creamos otro problema
Lp_prob = LpProblem('Problem', LpMinimize)

# Variables del problema
x = LpVariable("x", lowBound=0)  
y = LpVariable("y", lowBound=0)  

# Función objetivo
Lp_prob += 3 * x + 5 * y

# Constraints:
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3
# ¿Estas 2 últimas restricciones hacen falta? ¿O lo podríamos haber indicado de otro modo?

# Vemos las soluciones
print(Lp_prob)
status = Lp_prob.solve()  
print(LpStatus[status])  
print(value(x), value(y), value(Lp_prob.objective))

###########################################################
