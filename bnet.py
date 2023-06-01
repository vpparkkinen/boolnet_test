import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import itertools


allcombs = list(itertools.product([True, False], repeat=5))
allcdf = DataFrame(allcombs, columns=["M", "E", "L", "LE", "G"])

# Updating rules. Not good.
# To do: make it so that the rules can be given in a dict
# of string keys/values `"C": "not A and B"` etc. that are then
# # parse+eval'd appropriately in a context of a df describing  the init # state.
def upstate(state):
    upstate = {}
    upstate["M"] = not state["G"].iloc[0] and state["L"].iloc[0] or not state["G"].iloc[0] and state["LE"].iloc[0]

    upstate["E"] = state["M"].iloc[0]

    #upstate["E"] = False

    upstate["L"] = not state["G"].iloc[0] and state["LE"].iloc[0] and not state["E"].iloc[0] or not state["G"].iloc[0] and not state["E"].iloc[0] and state["L"].iloc[0]

    upstate["LE"] = state["LE"].iloc[0]

    upstate["G"] = state["G"].iloc[0]

    return(DataFrame(upstate, index=[0]))


def simu_single(state, times):
    if times < 1:
        return(state)
    else:
        times = times - 1
        state = pd.concat([state, upstate(state.iloc[[-1]])])
        return(simu_single(state = state, times = times))

# simu_single(allcdf.iloc[[30],], 1)


def simulate(init_states, times):
     res = [0] * len(init_states)
     for i in range(len(init_states)):
          res[i] = simu_single(init_states.iloc[[i], ], times)
     return(res)




# allcombs = list(itertools.product([True, False], repeat=3))
# allcdf = DataFrame(allcombs, columns=["A", "B", "C"])
# def upstate2(state):
#     upstate = {}
#     upstate["A"] = state["C"].iloc[0]
#     upstate["B"] = state["A"].iloc[0] or state["A"].iloc[0]
#     upstate["C"] = state["B"].iloc[0]
#     return(DataFrame(upstate, index=[0]))
