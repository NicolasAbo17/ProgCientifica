# Librerias
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

fr_grafica = tk.Frame(master=window)
fr_grafica.place(x=25, y=125)
fr_grafica.config(width=475, height=250)

fr_funciones = tk.Frame(master=window)
fr_funciones.place(x=25, y=400)
fr_funciones.config(width=475, height=75)

fr_tiempo = tk.Frame(master=window)
fr_tiempo.place(x=25, y=500)
fr_tiempo.config(width=475, height=150)

fr_parametros = tk.Frame(master=window)
fr_parametros.place(x=550, y=25)
fr_parametros.config(bg="#F4D03F", width=325, height=300)

fr_solucion = tk.Frame(master=window)
fr_solucion.place(x=550, y=350)
fr_solucion.config(bg="#F4D03F", width=325, height=300)


# Implementacion de los frames
# fr_buttons
def exportar():
    print("Exportar")


def importar():
    print("Importar")


Style.configure('primary.TButton', font=('Agency FB', 17, 'bold'), foreground='#102c59', background='#1b1052',
                padding=0)
Style.map("primary.TButton",
          foreground=[('pressed', '#0e0926'), ('active', '#1A5276')],
          background=[('pressed', '!disabled', '#2809ba'), ('active', '#157bbd')])
btn_exportar = ttk.Button(master=fr_buttons, text="Exportar", style="primary.TButton", command=exportar).place(relx=0.3,
                                                                                                               rely=0.5,
                                                                                                               anchor=CENTER)
btn_importar = ttk.Button(master=fr_buttons, text="Importar", style="primary.TButton", command=importar).place(relx=0.7,
                                                                                                               rely=0.5,
                                                                                                               anchor=CENTER)


# fr_grafica
def fun_s(t):
    return t


def fun_e(t):
    return 2 * t


def fun_i(t):
    return 3 * t


def fun_l(t):
    return 0.5 * t


def grafica():
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
    Plot = FigureCanvasTkAgg(fig, master=fr_grafica)
    Plot.draw()
    Plot.get_tk_widget().place(relx=0.5, rely=0.5, width=475, height=250, anchor=CENTER)


grafica()

# fr_funciones
Style.configure('Fun.TCheckbutton', font=('Agency FB', 17, 'bold'), foreground='#102c59', padding=0)
Style.map("Fun.TCheckbutton",
          foreground=[('active', '#1A5276')])

check_sfun = tk.BooleanVar()
cbx_s = ttk.Checkbutton(master=fr_funciones, text="S(t)", style="Fun.TCheckbutton", variable=check_sfun)
cbx_s.place(relx=0.2, rely=0.5, anchor=CENTER)
check_sfun.set(True)

check_efun = tk.BooleanVar()
cbx_e = ttk.Checkbutton(master=fr_funciones, text="E(t)", style="Fun.TCheckbutton", variable=check_efun)
cbx_e.place(relx=0.4, rely=0.5, anchor=CENTER)
check_efun.set(True)

check_ifun = tk.BooleanVar()
cbx_i = ttk.Checkbutton(master=fr_funciones, text="I(t)", style="Fun.TCheckbutton", variable=check_ifun)
cbx_i.place(relx=0.6, rely=0.5, anchor=CENTER)
check_ifun.set(True)

check_lfun = tk.BooleanVar()
cbx_l = ttk.Checkbutton(master=fr_funciones, text="L(t)", style="Fun.TCheckbutton", variable=check_lfun)
cbx_l.place(relx=0.8, rely=0.5, anchor=CENTER)
check_lfun.set(True)

# fr_tiempo
Style.configure('Title.TLabel', font=('Agency FB', 25, 'bold'), foreground='#102c59', padding=0)
Style.configure('Time.TLabel', font=('Agency FB', 25, 'bold'), foreground='#c9bc06', padding=0)

label_time = ttk.Label(master=fr_tiempo, text="Tiempo de simulación", style="Title.TLabel").place(relx=0.5, rely=0.3,
                                                                                                  anchor=CENTER)


def validate_year(P):
    return P.isdigit()


num_initalYear = tk.StringVar()
entry_initial = ttk.Entry(master=fr_tiempo, textvariable=num_initalYear, font=('Agency FB', 25, 'bold'), width=11,
                          validate="key",
                          validatecommand=(fr_tiempo.register(validate_year), "%P"))
entry_initial.place(relx=0.2, rely=0.7, anchor=CENTER)

num_finalYear = tk.StringVar()
entry_final = ttk.Entry(master=fr_tiempo, textvariable=num_finalYear, font=('Agency FB', 25, 'bold'), width=11,
                        validate="key",
                        validatecommand=(fr_tiempo.register(validate_year), "%P"))
entry_final.place(relx=0.6, rely=0.7, anchor=CENTER)

label_total = ttk.Label(master=fr_tiempo, text="134 años", style="Time.TLabel").place(relx=0.9, rely=0.7, anchor=CENTER)

# MELISSA RINCON
# fr_parametros
# fr_solucion

window.mainloop()
