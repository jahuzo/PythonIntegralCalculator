#PROJECT

from sympy import *
import numpy as np
from math import *
import tkinter as tk
from tkinter import ttk

x, y, z = symbols('x y z') #declare possibly used symbols as symbols   
n = 1  # order of derivative

def derivative(root, f, x0):
    try:
        def dxg(f, var, n):  # dxg - general form of derivative, gf - general formula, var - by which variable to find derivative
            gf = diff(f, var, n)
            return gf

        def dxn(f, x0):  # dxn - exact numeric value of derivative in point x0
            h = 0.00000000001  # true analytical derivative would parse into infinitely small segments, we have to choose a sufficiently small number
            res = (f.subs(x, x0 + h) - f.subs(x, x0)) / h  # substitution into the limit definition of derivative
            return float("%.3f" % res)

        
        app.general.delete(1.0, tk.END)  #Clear box
        app.general.insert(tk.END, f"General formula: \n \n {dxg(f, x, n)}")

        app.exact.delete(1.0, tk.END)  
        app.exact.insert(tk.END, f"Exact calculation: \n {dxn(f, x0)}")

    except:
        app.infobox.delete(0.0, tk.END)
        app.infobox.insert(tk.END, "Please input a valid function!") 

def integral(root, f, a, b):
    try:
        def intg(f, x):  # x is a symbolic input !!!
            gf = integrate(f, x)  # sympy integration function for the indefinite integral
            return gf

        def intn(f, a, b):
            res = integrate(f, (x, a, b))  # works the same as line 40, but when given bounds, computes the definite integral
            return float("%.3f" % res)

        app.general.delete(1.0, tk.END)  # Clear existing text
        app.general.insert(tk.END, f"General formula: \n {intg(f, x)}")

        app.exact.delete(1.0, tk.END)  # Clear existing text
        app.exact.insert(tk.END, f"Exact calculation: \n {intn(f, a, b)}")
    except:
        app.infobox.delete(0.0, tk.END)
        app.infobox.insert(tk.END, "Please input a valid function!")
def calc(app):
    try:              # exception handling for invalid bounds
        if "x" in app.fbox.get():
            f = sympify(app.fbox.get())
            if bv.get() == 1:
                x0 = int(app.boundbox.get())
                derivative(app, f, x0)
            else:
                a, b = app.boundbox.get().split()
                a, b = int(a), int(b)
                integral(app, f, a, b)
            app.infobox.delete(0.0, tk.END)
            app.infobox.insert(tk.END, f"Success!")
        else:
            raise ValueError
    except ValueError:
        app.infobox.delete(0.0, tk.END)
        app.infobox.insert(tk.END, "Please input a valid function! \n NOTE: Non-constant!")
    except:
        app.infobox.delete(0.0, tk.END)
        app.infobox.insert(tk.END, f"Please input valid bounds!")

def updB(app):
    app.fbox.delete(0, tk.END)
    app.bc["state"] = "normal"
    app.fbox["state"] = "normal"
    app.boundbox["state"] = "normal"
    app.fbox.insert(tk.END, "Input function")
    app.boundbox.delete(0, tk.END)
    if bv.get() == 1:
        app.infobox.delete(0.0, tk.END)
        app.infobox.insert(tk.END, "Input x0\nNOTE: x0 must be an integer!")
        app.boundbox.insert(tk.END, "x0")
    else:
        app.infobox.delete(0.0, tk.END)
        app.infobox.insert(tk.END, "Input a and b \nNOTE: a and b must be integers\nNOTE: separate by a space!")
        app.boundbox.insert(tk.END, "a b")

def clear(event):
    event.widget.delete(0, tk.END)

class ScaledWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        tk.Grid.rowconfigure(master, 0, weight=1)
        tk.Grid.columnconfigure(master, 0, weight=1)
        self.widgets()

    def widgets(self):
        for nr in range(3):
            tk.Grid.rowconfigure(self, nr, weight=1)
        for nc in range(4):
            tk.Grid.columnconfigure(self, nc, weight=1)

        self.infobox = tk.Text(self, width=10, height=5)
        self.infobox.grid(row=0, column=0, columnspan=4, sticky=tk.N+tk.S+tk.E+tk.W)
        self.infobox.insert(tk.END, "Welcome! Select operation mode!")
        
        self.fbox = tk.Entry(self, textvariable=f, state="disabled")
        self.fbox.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.fbox.insert(tk.END, "Input function!")
        self.fbox.bind("<FocusIn>", clear)
        
        self.boundbox = tk.Entry(self, width=5, textvariable=bounds, state="disabled")
        self.boundbox.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.boundbox.bind("<FocusIn>", clear)

        self.bd = tk.Radiobutton(self, text="Derivative", variable=bv, value=1, command=lambda: updB(self))
        self.bd.grid(row=1, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.bi = tk.Radiobutton(self, text="Integral", variable=bv, value=2, command=lambda: updB(self))
        self.bi.grid(row=1, column=3, sticky=tk.N + tk.S + tk.E + tk.W)

        self.general = tk.Text(self, width=10, height=5)
        self.general.grid(row=2, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.general.insert(tk.END, "General formula")

        self.exact = tk.Text(self, width=10, height=5)
        self.exact.grid(row=2, column=2, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.exact.insert(tk.END, "Exact calculation" )

        self.bc = tk.Button(self, text="Calculate", command=lambda: calc(self), state="disabled")
        self.bc.grid(row=0, column=4, rowspan = 3, sticky=tk.N + tk.S + tk.E + tk.W)
                           
win = tk.Tk()
win.title("Integral & derivative calculator by Marek Vacula")
bv = tk.IntVar()           # variable to track radio button states
f = tk.StringVar()                # fx - stores input string, test because of f name conflict
bounds = tk.StringVar()          # universal variable for bounds

app = ScaledWindow(win)

win.mainloop()