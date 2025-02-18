

# https://pypi.org/project/PuLP/
# https://github.com/coin-or/pulp?tab=readme-ov-file




from pulp import *

# Inicializamos el modelo
model = LpProblem("Profitmaximisingproblem", LpMaximize)

# Variables
A = LpVariable('A', lowBound=0, cat='Integer')
B = LpVariable('B', lowBound=0, cat='Integer')

# Función objetivo
model += 30000 * A + 45000 * B, "Profit"

# Restricciones
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21

# Resolvemos
model.solve()
LpStatus[model.status]

# Mostramos por pantalla los resultados
print("Production of Car A = {}".format(A.varValue))
print("Production of Car B = {}".format(B.varValue))
print(value(model.objective))



