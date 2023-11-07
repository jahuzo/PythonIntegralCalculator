#PROJECT

from sympy import *
import numpy as np
from math import *
import tkinter as tk
from tkinter import ttk

x, y, z = symbols('x y z') #declare possibly used symbols as symbols

f = sympify(input("Input function as string: ")) #for subsequent functions, the variable must be symbolic and not string

operation = input("Input operation type (d for derivative OR i for integral) >> ") 
   
#f = x**2
n = 1
#x0 = 3
#a = 0  
#b = 1

print("The original function f =", f)

if operation == "d" :
  x0 = int(input("Find derivative in point x0 = "))  #for some reason the x0 input needs to be typed 
  def dxg(f, var, n):    # dxg - general form of derivative, gf - general formula, var - by which variable to find derivative
    gf = diff(f, var, n)

    return gf

  def dxn(f, x0): # dxn - exact numeric value of derivative in point x0
      h = 0.00000000001
      up = f.subs(x, x0 + h) - f.subs(x, x0) # substites exact values of x
      down = h
      m = up / down
      return float("%.3f" % m)

  print("General formula of its derivative of order",n, "is: f =", dxg(f, x, n))

  print("Exact numeric value of the derivative in x0 =", x0, "is", dxn(f, x0))

elif operation == "i" :
  a, b = input("Input integration bounds (2) with a space separator :").split() # splits the string with default sep
  def intg(f, x):
    gf = integrate(f,x)
    return gf

  def intn(f, a, b):

    res = integrate(f, (x, a, b))
    return float("%.3f" % res)

  print("General formula of its primitive function is: F =", intg(f, x))

  print("Exact numeric value when we integrate from", a, "to", b, "is", intn(f, a,b))

else:
  print("Invalid operation type")

