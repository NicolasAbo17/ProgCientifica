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
fr_funciones.config(bg="#F4D03F", width=475, height=75)

fr_tiempo = tk.Frame(master=window)
fr_tiempo.place(x=25, y=500)
fr_tiempo.config(bg="#F4D03F", width=475, height=150)

fr_parametros = tk.Frame(master=window)
fr_parametros.place(x=550, y=25)
fr_parametros.config(bg="#F4D03F", width=325, height=300)

fr_solucion = tk.Frame(master=window)
fr_solucion.place(x=550, y=350)
fr_solucion.config(bg="#F4D03F", width=325, height=300)


# Implementacion de los frames

# NICOLAS ABONDANO
# fr_buttons
def exportar():
    print("Exportar")


def importar():
    print("Importar")


Style.configure('1.TButton', font=('Agency FB', 17, 'bold'), foreground='#3618c9', background='#1b1052', padding=0)
Style.map("1.TButton",
          foreground=[('pressed', '#0e0926'), ('active', '#1A5276')],
          background=[('pressed', '!disabled', '#2809ba'), ('active', '#157bbd')])
btn_exportar = ttk.Button(master=fr_buttons, text="Exportar", style="1.TButton", command=exportar).grid(row=0, column=0,
                                                                                                        padx=60,
                                                                                                        pady=12.5)
btn_importar = ttk.Button(master=fr_buttons, text="Importar", style="1.TButton", command=importar).grid(row=0, column=1,
                                                                                                        padx=60,
                                                                                                        pady=12.5)


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

# NICOLAS ZUÑIGA
# fr_funciones
# fr_tiempo

# MELISSA RINCON
# fr_parametros
# fr_solucion

window.mainloop()
