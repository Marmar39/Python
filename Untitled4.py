from __future__ import division
from pyomo.environ import *
model = AbstractModel()
model.F = Param(within=NonNegativeIntegers)
model.N = Param(within = NonNegativeIntegers)

model.I = RangeSet(1,model.F)
model.J = RangeSet(1,model.N)

model.a = Param(model.I, model.J)
model.c = Param(model.I)
model.Nmin = Param(model.J)
model.Nmax = Param(model.J)
model.v = Param(model.I)
model.vMax = Param()

model.x = Var(model.I, domain= NonNegativeReals)
def objjj(model):
    return summation(model.c,model.x)
model.OBJ = Objective(rule = objjj)

def exp_constraint(model,j):
    return sum(model.a[i,j]*model.x[i] for i in model.I)<=model.Nmax[j]
model.ax1const = Constraint(model.J, rule = exp_constraint)

def exp2_constraint(model,j):
    return sum(model.a[i,j]*model.x[i] for i in model.I)>=model.Nmin[j]
model.ax2const = Constraint(model.J, rule = exp2_constraint)

def exp3_constraint(model):
    return summation(model.v,model.x)<=model.vMax
model.ax3const = Constraint(rule=exp3_constraint)
#pyomo solve Untitled3.ipynb Exp1.dat --solver=glpk
#instance = model.create("Exp1.dat")
#instance.pprint()
#opt = SolverFactory('glpk')
#results = opt.solve(model)