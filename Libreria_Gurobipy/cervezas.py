import gurobipy as gp

# Create a new model
m = gp.Model()

# Create variables
x = m.addVar(vtype='C', name="x")
y = m.addVar(vtype='C', name="y")

# Set objective function
m.setObjective(100 * x + 125 * y, gp.GRB.MAXIMIZE)

# Add constraints
m.addConstr(3 * x + 5 * y <= 15)
m.addConstr(90 * x + 85 * y <= 350)

# Solve it!
m.optimize()

print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: x={x.X}, y={y.X}")