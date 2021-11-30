## Librerias
import tkinter as tk
from tkinter import ttk, CENTER
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np

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
def fun_s(t):
    return t


def fun_e(t):
    return 2 * t


def fun_i(t):
    return 3 * t


def fun_l(t):
    return 0.5 * t


def graficar():
    fig = plt.Figure(figsize=(4, 2), dpi=100)
    t = np.arange(0, 10, 0.01)
    sub = fig.add_subplot(111)

    sub.plot(t, fun_s(t))
    sub.plot(t, fun_i(t))
    sub.plot(t, fun_l(t))
    sub.plot(t, fun_e(t))

    fig.suptitle("Funciones")

    plt.close()
    plt.style.use('seaborn-darkgrid')
    Plot = FigureCanvasTkAgg(fig, master=fr_graph)
    Plot.draw()
    Plot.get_tk_widget().place(relx=0.5, rely=0.5, width=475, height=250, anchor=CENTER)


graficar()

# fr_functions
Style.configure('Fun.TCheckbutton', font=('Agency FB', 17, 'bold'), foreground='#102c59', padding=0)
Style.map("Fun.TCheckbutton",
          foreground=[('active', '#1A5276')])

check_sfun = tk.BooleanVar()
cbx_s = ttk.Checkbutton(master=fr_functions, text="S(t)", style="Fun.TCheckbutton", variable=check_sfun)
cbx_s.place(relx=0.2, rely=0.5, anchor=CENTER)
check_sfun.set(True)

check_efun = tk.BooleanVar()
cbx_e = ttk.Checkbutton(master=fr_functions, text="E(t)", style="Fun.TCheckbutton", variable=check_efun)
cbx_e.place(relx=0.4, rely=0.5, anchor=CENTER)
check_efun.set(True)

check_ifun = tk.BooleanVar()
cbx_i = ttk.Checkbutton(master=fr_functions, text="I(t)", style="Fun.TCheckbutton", variable=check_ifun)
cbx_i.place(relx=0.6, rely=0.5, anchor=CENTER)
check_ifun.set(True)

check_lfun = tk.BooleanVar()
cbx_l = ttk.Checkbutton(master=fr_functions, text="L(t)", style="Fun.TCheckbutton", variable=check_lfun)
cbx_l.place(relx=0.8, rely=0.5, anchor=CENTER)
check_lfun.set(True)

# fr_time
Style.configure('Title.TLabel', font=('Agency FB', 25, 'bold'), foreground='#102c59', padding=0)
Style.configure('Time.TLabel', font=('Agency FB', 25, 'bold'), foreground='#c9bc06', padding=0)

label_time = ttk.Label(master=fr_time, text="Tiempo de simulación", style="Title.TLabel")
label_time.place(relx=0.5, rely=0.3, anchor=CENTER)


def validate_year(P):
    return P.isdigit()


num_initalYear = tk.StringVar()
entry_initial = ttk.Entry(master=fr_time, textvariable=num_initalYear, font=('Agency FB', 25, 'bold'), width=11,
                          validate="key",
                          validatecommand=(fr_time.register(validate_year), "%P"))
entry_initial.place(relx=0.2, rely=0.7, anchor=CENTER)

num_finalYear = tk.StringVar()
entry_final = ttk.Entry(master=fr_time, textvariable=num_finalYear, font=('Agency FB', 25, 'bold'), width=11,
                        validate="key",
                        validatecommand=(fr_time.register(validate_year), "%P"))
entry_final.place(relx=0.6, rely=0.7, anchor=CENTER)

label_total = ttk.Label(master=fr_time, text="134 años", style="Time.TLabel").place(relx=0.9, rely=0.7, anchor=CENTER)

# fr_parameters
label_parameters = ttk.Label(master=fr_parameters, text="Parámetros", style="Title.TLabel")
label_parameters.place(relx=0.5, rely=0.1, anchor=CENTER)

parameters = ['Λ', '𝛽', 'δ', 'p', '𝜇', 'k', 'r1', 'r2', 'ϕ', '𝛾', 'd1', 'd2']
entry_parameters = []

Style.configure('Parameter.TLabel', font=('Agency FB', 15, 'bold'), foreground='#ffffff', background='#dbd821', width=4,
                padding=0, anchor=CENTER)

xPos_parameters = 0.2
yPos_parameters = 0.3


def validate_number(P):
    return P.isdigit() or P.contains('.')


for parameter in parameters:
    label_parameter = ttk.Label(master=fr_parameters, text=parameter, style="Parameter.TLabel")
    label_parameter.place(relx=xPos_parameters, rely=yPos_parameters, anchor=CENTER)

    xPos_parameters += 0.2

    entry_parameter = ttk.Entry(master=fr_parameters, font=('Agency FB', 10, 'bold'), width=5,
                                validate="key",
                                validatecommand=(fr_parameters.register(validate_number), "%P"))
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
                padding=0, width = 20)
Style.map("secondary.TButton",
          foreground=[('pressed', '#0e0926'), ('active', '#1A5276')],
          background=[('pressed', '!disabled', '#2809ba'), ('active', '#157bbd')])

methods = ["Euler adelante", "Euler atrás", "Euler modificado", "Runge–Kutta 2", "Runge–Kutta 4", "solve_ivp"]
button_methods = []
yPos_methods = 0.3

for method in methods:
    button_method = ttk.Button(master=fr_solutions, text=method, style="secondary.TButton")
    button_method.place(relx=0.5, rely=yPos_methods, anchor=CENTER)

    button_methods.append(button_method)
    yPos_methods += 0.1

window.mainloop()
