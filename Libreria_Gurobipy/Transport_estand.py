from gurobipy import *
import numpy as np

try:
    # Defining the model
    model = Model("Transport")

    # Defining the dimensions of sets of indices
    origins = 2
    destinations = 3

    # Defining the parameters:
    # Capacities
    capacities = [350, 600]

    # Demands
    demands = [325, 300, 275]

    # Distances
    d = [[2.5,1.7,1.8],[2.5,1.8,1.4]]
    # If numpy is used:
    # d = np.array([[2.5,1.7,1.8],[2.5,1.8,1.4]])

    # Transport cost per unit and 1000 miles
    c = 90

    # Defining the decision variables
    x = {}
    for i in range(0,origins):
        for j in range(0,destinations):
            x[i,j] = model.addVar(lb=0, name='x_%s_%s' % (i, j), vtype=GRB.CONTINUOUS)

    # Defining the objective function
    model.setObjective(quicksum(c*d[i][j]*x[i,j]/1000 for i in range(0,origins) for j in range(0,destinations)), GRB.MINIMIZE)

    # Defining the constraints
    for i in range(0,origins):
        model.addConstr(quicksum(x[i, j] for j in range(0,destinations)) <= capacities[i], 'caps_%s' % i)

    for j in range(0,destinations):
        model.addConstr(quicksum(x[i, j] for i in range(0,origins)) >= demands[j], 'dems_%s' % j)

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
    for i in range(0,origins):
        for j in range(0,destinations):
            if x[i, j].X > 0:
                print("x[%s,%s] = %g" % (i+1, j+1, x[i,j].X))

except GurobiError as e:
    print(e)