from gurobipy import *

try:
    # Defining the model
    model = Model('Mina')

    # Defining the sets of indices
    productos = ['lignito', 'antracita']
    recursos = ['corte', 'tamizado', 'lavado']

    # Defining the parameters:
    beneficio = {'lignito': 24,'antracita': 18}

    limite_recursos = {
        'corte': 12,
        'tamizado': 10,
        'lavado': 8
    }

    consumo = {
        ('lignito', 'corte'): 3,
        ('lignito', 'tamizado'): 3,
        ('lignito', 'lavado'): 4,
        ('antracita', 'corte'): 4,
        ('antracita', 'tamizado'): 3,
        ('antracita', 'lavado'): 2,
    }

    # Defining the decision variables
    x = {}
    for i in productos:
            x[i] = model.addVar(lb=0, name='x_%s' % i, vtype='C')

    # Defining the objective function
    model.setObjective(
         quicksum(beneficio[i]*x[i] for i in productos),
           -1)

    # Defining the constraints

    for j in recursos:
        model.addConstr(
             quicksum(consumo[i,j] * x[i] for i in productos) <= limite_recursos[j], 'limites_%s' % j)

    # Defining the time limit (in seconds)
    model.setParam('TimeLimit', 100)

    # Calling the optimizer
    model.optimize()

    # Obtaining the status of the incumbent solution
    status = model.getAttr('Status')
    if status == GRB.OPTIMAL:
        print('Solución óptima')
    else:
        print('Status: '+str(status))

    # Printing the value of the objective function
    print('Beneficio: %g' % model.ObjVal)

    # Printing variables x different from 0
    print('SOLUTION:')
    for i in productos:
            if x[i].X > 0:
                print('x[%s] = %g' % (i, x[i].X))

except GurobiError as e:
    print(e)