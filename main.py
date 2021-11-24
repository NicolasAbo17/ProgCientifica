##
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

matplotlib.use("TkAgg")

import tkinter as tk
from tkinter import ttk

# Configuración de la ventana
window = tk.Tk()
window.geometry('900x675')
window.title('Proyecto final - Programación Científica')

# Frames izquierda
fr_buttons = tk.Frame(master=window)
fr_buttons.place(x=25, y=25)
fr_buttons.config(bg="#F4D03F", width=475, height=75)

fr_grafica = tk.Frame(master=window)
fr_grafica.place(x=25, y=125)
fr_grafica.config(bg="#F4D03F", width=475, height=250)

fr_funciones = tk.Frame(master=window)
fr_funciones.place(x=25, y=400)
fr_funciones.config(bg="#F4D03F", width=475, height=75)

fr_tiempo = tk.Frame(master=window)
fr_tiempo.place(x=25, y=500)
fr_tiempo.config(bg="#F4D03F", width=475, height=150)

# Frames derecha
fr_parametros = tk.Frame(master=window)
fr_parametros.place(x=550, y=25)
fr_parametros.config(bg="#F4D03F", width=325, height=300)

fr_solucion = tk.Frame(master=window)
fr_solucion.place(x=550, y=350)
fr_solucion.config(bg="#F4D03F", width=325, height=300)

# Implementacion de los frames

#fr_buttons
#fr_grafica
#fr_funciones
#fr_tiempo
#fr_parametros
#fr_solucion

window.mainloop()
