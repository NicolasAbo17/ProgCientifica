import numpy as np
import scipy.integrate as inte

def fun_s(pLambda, pBeta, pDelta, pMiu):
    return lambda s, e, i, l: pLambda - pBeta * s * (i + pDelta * l) - pMiu * s


def fun_e(pBeta, pP, pDelta, pR2, pMiu, pK,  pR1):
    return lambda s, e, i, l: pBeta * (1 - pP) * s * (i + (pDelta * l)) + pR2 * i - (pMiu + pK * (1 - pR1)) * e


def fun_i(pBeta, pP, pDelta, pK, pR1, pGamma, pMiu, pD1, pFi, pR2):
    return lambda s, e, i, l: pBeta * pP * s * (i + pDelta * l) + pK * (1 - pR1) * e + pGamma * l - (pMiu + pD1 + pFi * (1  - pR2) + pR2) * i


def fun_l(pFi, pR2, pMiu, pD2, pGamma):
    return lambda s, e, i, l: pFi * (1 - pR2)*i - (pMiu + pD2+ pGamma)*l


def get_functions(var_bools, tipo, To, Tf, pLambda, pBeta, pDelta, pP, pMiu, pK, pR1, pR2, pFi, pGamma, pD1, pD2, t, h):
    funs = {"S": fun_s(pLambda, pBeta, pDelta, pMiu),
            "E": fun_e(pBeta, pP, pDelta, pR2, pMiu, pK, pR1),
            "I": fun_i(pBeta, pP, pDelta, pK, pR1, pGamma, pMiu, pD1, pFi, pR2),
            "L": fun_l(pFi, pR2, pMiu, pD2, pGamma)}

    ans = solve_function(tipo, funs, t, h, To, Tf)

    for key in var_bools:
        if  var_bools[key] == 0:
            del funs[key]

    return ans

def solve_function(tipo, funs, t, h, To, Tf):
    initial = {
        "S": 0,
        "E": 0,
        "I": 0,
        "L": 0
    }
    if tipo == "Euler adelante":
        return sol_kutta2(funs, initial, t, h)
    if tipo == "Euler atrás":
        return sol_kutta2(funs, initial, t, h)
    if tipo == "Euler modificado":
        return sol_kutta2(funs, initial, t, h)
    if tipo == "Runge–Kutta 2":
        return sol_kutta2(funs, initial, t, h)
    if tipo == "Runge–Kutta 4":
        return sol_kutta4(funs, initial, t, h)
    if tipo == "solve_ivp":
        return solve_ip(funs, initial, t, h, To, Tf)


def sol_kutta2(funs, initial, t, h):
    RK2 = {
        "S": np.zeros(len(t)),
        "E": np.zeros(len(t)),
        "I": np.zeros(len(t)),
        "L": np.zeros(len(t))
    }

    for key in RK2:
        RK2[key][0] = initial[key]

    k_val1 = {}
    k_val2 = {}
    for i in range(1, len(t)):
        for key in RK2:
            k_val1[key] = funs[key](RK2["S"][i-1],
                                    RK2["E"][i-1],
                                    RK2["I"][i-1],
                                    RK2["L"][i-1])

        for key in RK2:
            k_val2[key] = funs[key](RK2["S"][i-1] + k_val1["S"]*h,
                                    RK2["E"][i-1] + k_val1["E"]*h,
                                    RK2["I"][i-1] + k_val1["I"]*h,
                                    RK2["L"][i-1] + k_val1["L"]*h)

        for key in RK2:
            RK2[key][i] = RK2[key][i - 1] + (h / 2) * (k_val1[key] + k_val2[key])

    return RK2

def sol_kutta4(funs, initial, t, h):
    RK4 = {
        "S": np.zeros(len(t)),
        "E": np.zeros(len(t)),
        "I": np.zeros(len(t)),
        "L": np.zeros(len(t))
    }

    for key in RK4:
        RK4[key][0] = initial[key]

    k_val1 = {}
    k_val2 = {}
    k_val3 = {}
    k_val4 = {}
    for i in range(1, len(t)):
        for key in RK4:
            k_val1[key] = funs[key](RK4["S"][i-1],
                                    RK4["E"][i-1],
                                    RK4["I"][i-1],
                                    RK4["L"][i-1])

        for key in RK4:
            k_val2[key] = funs[key](RK4["S"][i-1] + 0.5 * k_val1["S"] * h,
                                    RK4["E"][i-1] + 0.5 * k_val1["E"] * h,
                                    RK4["I"][i-1] + 0.5 * k_val1["I"] * h,
                                    RK4["L"][i-1] + 0.5 * k_val1["L"] * h)

        for key in RK4:
            k_val3[key] = funs[key](RK4["S"][i - 1] + 0.5 * k_val2["S"] * h,
                                    RK4["E"][i - 1] + 0.5 * k_val2["E"] * h,
                                    RK4["I"][i - 1] + 0.5 * k_val2["I"] * h,
                                    RK4["L"][i - 1] + 0.5 * k_val2["L"] * h)

        for key in RK4:
            k_val4[key] = funs[key](RK4["S"][i-1] + k_val3["S"] * h,
                                    RK4["E"][i-1] + k_val3["E"] * h,
                                    RK4["I"][i-1] + k_val3["I"] * h,
                                    RK4["L"][i-1] + k_val3["L"] * h)

        for key in RK4:
            RK4[key][i] = RK4[key][i - 1] + (h / 6) * (k_val1[key] + 2 * k_val2[key] + 2 * k_val3[key] + k_val4)

    return RK4

def solve_ip(funs, initial, t, To, Tf):
    FSystem = lambda t, y: [funs["S"], funs["E"], funs["I"], funs["L"]]
    return  inte.solve_ivp(FSystem, [To, Tf], [initial["S"], initial["E"], initial["I"], initial["L"]],t_eval=t, method='RK45')