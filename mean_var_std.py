import numpy as np

def calculate(list):
    if len(list) > 9 or len(list) < 9:
        raise(ValueError('List must contain nine numbers.'))

    rlist = [list[x:x+3] for x in range (0, 7, 3)]
    clist = [[list[x], list[x+3], list[x+6]] for x in range(0,3)]
    funcs = {"mean": np.mean, "variance": np.var, "standard deviation": np.std, "max": np.max, "min": np.min, "sum": np.sum}
    calculations = {}

    for func_key in funcs.keys():
        axis1 = [funcs[func_key](x) for x in clist]
        axis2 = [funcs[func_key](x) for x in rlist]
        full = funcs[func_key](list)
        calculations[func_key] = [axis1, axis2, full]
    return calculations