# Librerias
import tkinter as tk
from tkinter import ttk, CENTER
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np
import re

from functions import *

matplotlib.use("TkAgg")

# Configuración de la ventana
window = tk.Tk()
window.geometry('900x675')
window.title('Proyecto final - Programación Científica')
Style = ttk.Style()

fr_buttons = tk.Frame(master=window)
fr_buttons.place(x=25, y=25)
fr_buttons.config(width=475, height=75)

fr_graph = tk.Frame(master=window)
fr_graph.place(x=25, y=125)
fr_graph.config(width=475, height=250)

fr_functions = tk.Frame(master=window)
fr_functions.place(x=25, y=400)
fr_functions.config(width=475, height=75)

fr_time = tk.Frame(master=window)
fr_time.place(x=25, y=500)
fr_time.config(width=475, height=150)

fr_parameters = tk.Frame(master=window)
fr_parameters.place(x=550, y=25)
fr_parameters.config(width=325, height=300)

fr_solutions = tk.Frame(master=window)
fr_solutions.place(x=550, y=350)
fr_solutions.config(width=325, height=300)


# Implementacion de los frames
# fr_buttons
def exportar():
    return


def importar():
    return


Style.configure('primary.TButton', font=('Agency FB', 17, 'bold'), foreground='#102c59', background='#1b1052',
                padding=0)
Style.map("primary.TButton",
          foreground=[('pressed', '#0e0926'), ('active', '#1A5276')],
          background=[('pressed', '!disabled', '#2809ba'), ('active', '#157bbd')])

btn_exportar = ttk.Button(master=fr_buttons, text="Exportar", style="primary.TButton", command=exportar)
btn_exportar.place(relx=0.3, rely=0.5, anchor=CENTER)
btn_importar = ttk.Button(master=fr_buttons, text="Importar", style="primary.TButton", command=importar)
btn_importar.place(relx=0.7, rely=0.5, anchor=CENTER)

# fr_graph
check_sfun = tk.BooleanVar()
check_efun = tk.BooleanVar()
check_ifun = tk.BooleanVar()
check_lfun = tk.BooleanVar()


def graficar():
    fig = plt.Figure(figsize=(4, 2), dpi=100)
    t = np.arange(0, variable_years.get(), 0.01)
    sub = fig.add_subplot(111)

    var_bools = {
            "S":check_sfun.get(),
            "I":check_ifun.get(),
            "L":check_lfun.get(),
            "E":check_efun.get()
        }

    functions = get_functions(var_bools, t)

    for key in functions:
        sub.plot(t, functions[key], label=key)

    fig.suptitle(variable_method.get())

    sub.legend()
    plt.close()
    plt.style.use('seaborn-darkgrid')
    Plot = FigureCanvasTkAgg(fig, master=fr_graph)
    Plot.draw()
    Plot.get_tk_widget().place(relx=0.5, rely=0.5, width=475, height=250, anchor=CENTER)


# fr_functions
Style.configure('Fun.TCheckbutton', font=('Agency FB', 17, 'bold'), foreground='#102c59', padding=0)
Style.map("Fun.TCheckbutton",
          foreground=[('active', '#1A5276')])

cbx_s = ttk.Checkbutton(master=fr_functions, text="S(t)", style="Fun.TCheckbutton", variable=check_sfun,
                        command=graficar)
cbx_s.place(relx=0.2, rely=0.5, anchor=CENTER)
check_sfun.set(True)

cbx_e = ttk.Checkbutton(master=fr_functions, text="E(t)", style="Fun.TCheckbutton", variable=check_efun,
                        command=graficar)
cbx_e.place(relx=0.4, rely=0.5, anchor=CENTER)
check_efun.set(True)

cbx_i = ttk.Checkbutton(master=fr_functions, text="I(t)", style="Fun.TCheckbutton", variable=check_ifun,
                        command=graficar)
cbx_i.place(relx=0.6, rely=0.5, anchor=CENTER)
check_ifun.set(True)

cbx_l = ttk.Checkbutton(master=fr_functions, text="L(t)", style="Fun.TCheckbutton", variable=check_lfun,
                        command=graficar)
cbx_l.place(relx=0.8, rely=0.5, anchor=CENTER)
check_lfun.set(True)

# fr_time
Style.configure('Title.TLabel', font=('Agency FB', 25, 'bold'), foreground='#102c59', padding=0)
Style.configure('Time.TLabel', font=('Agency FB', 25, 'bold'), foreground='#c9bc06', padding=0)

num_initalYear = tk.StringVar()
num_finalYear = tk.StringVar()

label_time = ttk.Label(master=fr_time, text="Tiempo de simulación", style="Title.TLabel")
label_time.place(relx=0.5, rely=0.3, anchor=CENTER)


def validate_integer(string):
    regex = re.compile(r"[0-9]*$")
    result = regex.match(string)
    return (string == ""
            or (result is not None
                and result.group(0) != ""))


def validate_year(P):
    return validate_integer(P)


def set_years():
    if num_initalYear.get() == "":
        num_initalYear.set("0")
    if num_finalYear.get() == "":
        num_finalYear.set("0")

    temp_years = int(num_finalYear.get()) - int(num_initalYear.get())
    if temp_years < 0:
        variable_years.set(0)
    elif temp_years <= 100:
        variable_years.set(temp_years)
    else:
        variable_years.set(100)

    global label_total
    label_total.config(text="{} años".format(variable_years.get()))


label_total = ttk.Label(master=fr_time, text="21 años", style="Time.TLabel")
label_total.place(relx=0.9, rely=0.7, anchor=CENTER)

num_initalYear.trace("w", lambda name, index, mode, num_initalYear=num_initalYear: set_years())
entry_initial = ttk.Entry(master=fr_time, textvariable=num_initalYear, font=('Agency FB', 25, 'bold'), width=11)
entry_initial.config(validate="key", validatecommand=(entry_initial.register(validate_year), "%P"))
entry_initial.place(relx=0.2, rely=0.7, anchor=CENTER)

num_finalYear.trace("w", lambda name, index, mode, num_finalYear=num_finalYear: set_years())
entry_final = ttk.Entry(master=fr_time, textvariable=num_finalYear, font=('Agency FB', 25, 'bold'), width=11)
entry_final.config(validate="key", validatecommand=(entry_final.register(validate_year), "%P"))
entry_final.place(relx=0.6, rely=0.7, anchor=CENTER)

variable_years = tk.IntVar()

num_initalYear.set(2000)
num_finalYear.set(2021)
variable_years.set(21)

# fr_parameters
label_parameters = ttk.Label(master=fr_parameters, text="Parámetros", style="Title.TLabel")
label_parameters.place(relx=0.5, rely=0.1, anchor=CENTER)

parameters = ['Λ', '𝛽', 'δ', 'p', '𝜇', 'k', 'r1', 'r2', 'ϕ', '𝛾', 'd1', 'd2']
variables_parameters = []
entry_parameters = []

Style.configure('Parameter.TLabel', font=('Agency FB', 15, 'bold'), foreground='#ffffff', background='#dbd821', width=4,
                padding=0, anchor=CENTER)

xPos_parameters = 0.2
yPos_parameters = 0.3


def validate_float(string):
    regex = re.compile(r"(\+|\-)?[0-9,]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count('+') <= 1
                and string.count('-') <= 1
                and string.count(',') <= 1
                and result is not None
                and result.group(0) != ""))


def validate_parameter(P):
    return validate_float(P)


for parameter in parameters:
    label_parameter = ttk.Label(master=fr_parameters, text=parameter, style="Parameter.TLabel")
    label_parameter.place(relx=xPos_parameters, rely=yPos_parameters, anchor=CENTER)

    xPos_parameters += 0.2

    variable_parameter = tk.StringVar()
    variable_parameter.set("0,0")
    variables_parameters.append(variable_parameter)

    entry_parameter = ttk.Entry(master=fr_parameters, font=('Agency FB', 10, 'bold'), width=5,
                                textvariable=variable_parameter, validate="key")
    entry_parameter.config(validatecommand=(entry_parameter.register(validate_parameter), "%P"))
    entry_parameter.place(relx=xPos_parameters, rely=yPos_parameters, anchor=CENTER)
    entry_parameters.append(entry_parameter)

    if xPos_parameters >= 0.8:
        xPos_parameters = 0.2
        yPos_parameters += 0.1
    else:
        xPos_parameters += 0.2

# fr_solutions
label_parameters = ttk.Label(master=fr_solutions, text="Método de solución", style="Title.TLabel")
label_parameters.place(relx=0.5, rely=0.1, anchor=CENTER)

Style.configure('secondary.TButton', font=('Agency FB', 12, 'bold'), foreground='#102c59', background='#1b1052',
                padding=0, width=20)
Style.map("secondary.TButton",
          foreground=[('pressed', '#0e0926'), ('active', '#1A5276')],
          background=[('pressed', '!disabled', '#2809ba'), ('active', '#157bbd')])

methods = ["Euler adelante", "Euler atrás", "Euler modificado", "Runge–Kutta 2", "Runge–Kutta 4", "solve_ivp"]
button_methods = []

variable_method = tk.StringVar()
yPos_methods = 0.3


def set_method(name):
    variable_method.set(name)
    graficar()


for i in range(len(methods)):
    button_methods.append(ttk.Button(master=fr_solutions, text=methods[i], style="secondary.TButton"
                                     , command=lambda c=i: set_method(methods[c])))
    button_methods[i].place(relx=0.5, rely=yPos_methods, anchor=CENTER)
    yPos_methods += 0.1

variable_method.set(methods[0])

# Excecution
graficar()

window.mainloop()
