import gurobipy as gp

# Create a new model
m = gp.Model('Petroquimica')

# Create variables
x = m.addVar(vtype='C', name='Botella')
y = m.addVar(vtype='C', name='Fibra')

# Set objective function
m.setObjective(36 * x + 30 * y, sense=-1)

# Add constraints
m.addConstr(0.966 * x + 0.912 * y <= 260)
m.addConstr(0.365 * x + 0.344 * y <= 150)

# Solve it!
m.optimize()

print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: PET Botella={x.X}, PET Fibra={y.X}")