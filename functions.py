def fun_s(t):
    return 0.5 * t


def fun_e(t):
    return t


def fun_i(t):
    return 2 * t


def fun_l(t):
    return 3 * t


def get_functions(var_bools, pLambda, pBeta, pDelta, pP, pMiu, pK, pR1, pR2, pFi, pGamma, pD1, pD2, t):
    funs = {}

    if var_bools["S"] == 1:
        funs["S"] = fun_s(t)
    if var_bools["E"] == 1:
        funs["E"] = fun_e(t)
    if var_bools["I"] == 1:
        funs["I"] = fun_i(t)
    if var_bools["L"] == 1:
        funs["L"] = fun_l(t)
    return funs
