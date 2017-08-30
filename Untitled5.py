
# coding: utf-8

# In[21]:

#http://nbviewer.jupyter.org/github/Pyomo/PyomoGallery/blob/master/maxflow/maxflow.ipynb

from __future__ import division
from pyomo.environ import *

model = AbstractModel()
model.N = Set()
model.A = Set(within=model.N*model.N)

model.s = Param(within=model.N)
model.t = Param(within=model.N)
model.c = Param(model.A)

model.f = Var(model.A, domain= NonNegativeReals)

def objc1(model):
    return sum(model.c[i,j]*model.f[i,j] for (i,j) in model.A if j==value(model.t))
model.OBJ = Objective(rule = objc1)
# Enforce an upper limit on the flow across each arc
def constraint1(model,i,j):
    return model.f[i,j]<=model.c[i,j]
model.axconst= Constraint(model.A, rule = constraint1)

def constraint2(model, k):
    if k != value(model.t) and k !=value(model.s):
        return sum(model.f[i,k]for (i,k) in model.A )== sum(model.f[k,i]for (k,i) in model.A )
model.axconst2= Constraint(model.A, rule = constraint2)
#instance = model.create("Exp1.dat")
#instance.pprint()
get_ipython().system(' jupyter nbconvert --to script Untitled5.ipynb')
#instance = model.create("Exp2.dat")
#instance.pprint()
get_ipython().system('cat Exp2.dat')
get_ipython().system('pyomo solve --solver=glpk Untitled5.py Exp2.dat')
get_ipython().system('cat results.yml')




