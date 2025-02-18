from gurobipy import *
import numpy as np

try:
    # Defining the model
    model = Model("Aceites")

    # Defining the dimensions of sets of indices
    aceites = 5
    vegetal = 2
    novegetal = 3

    # Defining the parameters:
    coste = [110,120,130,110,115]
    dureza =[8.8,6.1,2.0,4.2,5.0]
    dureza_minima = 3
    dureza_maxima = 6
    precio_venta = 150
    refino_vegetal = 200
    refino_novegetal =250

    # Defining the decision variables
    x = {}
    for i in range(0,aceites):
            x[i] = model.addVar(lb=0, name='x_%s' % i, vtype='C')

    # Defining the objective function
    model.setObjective(quicksum( (precio_venta-coste[i]) * x[i] for i in range(0,aceites)), GRB.MAXIMIZE)

    # Defining the constraints
    model.addConstr(quicksum(x[i] for i in range(0,vegetal)) <= refino_vegetal, 'refino vegetal')
    model.addConstr(quicksum(x[i] for i in range(vegetal,vegetal+novegetal)) <= refino_novegetal, 'refino no vegetal')
    model.addConstr(quicksum(dureza[i]*x[i] for i in range(0,aceites)) -  dureza_minima * quicksum(x[i] for i in range(0,aceites)) >= 0, 'dureza minima')
    model.addConstr(quicksum(dureza[i]*x[i] for i in range(0,aceites)) -  dureza_maxima * quicksum(x[i] for i in range(0,aceites)) <= 0, 'dureza maxima')

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
    print("Beneficio: %g" % model.ObjVal)

    # Printing variables x different from 0
    print("SOLUTION:")
    for i in range(0,aceites):
       if x[i].X > 0: print("x[%s] = %g" % (i+1, x[i].X))

except GurobiError as e:
    print(e)