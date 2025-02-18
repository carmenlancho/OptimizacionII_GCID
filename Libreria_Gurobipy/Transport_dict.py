from gurobipy import *

try:
    # Defining the model
    model = Model("Transport")

    # Defining the sets of indices
    origins = ["F1", "F2"]
    destinations = ["D1", "D2", "D3"]

    # Defining the parameters:
    # Capacities
    capacities = {
        'F1': 350,
        'F2': 600
    }

    # Demands
    demands = {
        'D1': 325,
        'D2': 300,
        'D3': 275
    }

    # Distances
    d = {
        ('F1', 'D1'): 2.5,
        ('F1', 'D2'): 1.7,
        ('F1', 'D3'): 1.8,
        ('F2', 'D1'): 2.5,
        ('F2', 'D2'): 1.8,
        ('F2', 'D3'): 1.4,
    }

    # Transport cost per unit and 1000 miles
    c = 90

    # Defining the decision variables
    x = {}
    for i in origins:
        for j in destinations:
            x[i,j] = model.addVar(lb=0, name='x_%s_%s' % (i, j), vtype=GRB.CONTINUOUS)

    # Defining the objective function
    model.setObjective(quicksum(c*d[i,j]*x[i,j]/1000 for i in origins for j in destinations), GRB.MINIMIZE)

    # Defining the constraints
    for i in origins:
        model.addConstr(quicksum(x[i, j] for j in destinations) <= capacities[i], 'caps_%s' % i)

    for j in destinations:
        model.addConstr(quicksum(x[i, j] for i in origins) >= demands[j], 'dems_%s' % j)

    # Defining the time limit (in seconds)
    model.setParam("TimeLimit", 100)

    # Calling the optimizer
    model.optimize()

    # Obtaining the status of the incumbent solution
    status = model.getAttr("Status")
    if status == GRB.OPTIMAL:
        print("Optimal solution")
    else:
        print("Status: "+str(status))

    # Printing the value of the objective function
    print("Transport cost: %g" % model.ObjVal)

    # Printing variables x different from 0
    print("SOLUTION:")
    for i in origins:
        for j in destinations:
            if x[i, j].X > 0:
                print("x[%s,%s] = %g" % (i, j, x[i,j].X))

except GurobiError as e:
    print(e)