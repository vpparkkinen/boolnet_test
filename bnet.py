import numpy as np
import matplotlib as plt
import pandas as pd
from pandas import DataFrame
import itertools

#
init = {
    "M": False,
    "E": False,
    "L": False,
    "LE": True,
    "G": False
}

np.array(np.meshgrid([True, False]*2)).T.reshape(-1,2)

allcombs = list(itertools.product([True,False], repeat=5))
allcdf = DataFrame(allcombs, columns=["M", "E", "L", "LE", "G"])
[[True, False]]*2
[True, False]*5

init = DataFrame()

def upstate(state):
    upstate = {}
    upstate["M"] = not state["G"] and state["L"] or not state["G"] and state["LE"]
    upstate["E"] = state["M"]
    upstate["L"] = not state["G"] and state["L"] or not state["G"]
    upstate["LE"] = state["LE"]
    upstate["G"] = state["G"]
    return(upstate)

upstate(allcdf.iloc[0,:])

def simu_single(state, times):
    initstate = state
    newstate = [0] * times
    for i in range(times):
        newstate[i] = upstate(state)
        state = newstate[i]
    out = DataFrame([initstate] + newstate)
    return(out)

simu(init, 5)

for x in range(6):
  print(x)
