#modules
import random
import math
import time
import os
from math import tan, cos, sin, radians, degrees, pi, pow
#Numbers
num1 = 0.0
num2 = 0.0

#Functions for the calculator (operations)
def addition(pNum1, pNum2):
    print("The answer of your addition is ", round(pNum1 + pNum2, 2))

def multiply(pNum1, pNum2):
    print("The answer of your multiplication is ", round(pNum1 * pNum2, 2))

def divide(pNum1, pNum2):
    if pNum2 == 0:
        print("undefined")
    else:
        fTotal = print("The answer of your division is ", round(pNum1 / pNum2, 2))
    return(fTotal)

def subtract(pNum1, pNum2):
    print("The answer of your subtract is ", round(pNum1 - pNum2, 2))

def square(pNum1, pNum2):
    print("The answer of your squaring is ", round(pNum1 ** pNum2, 2))

def squareRoot(pNum1):
    print("The answer is ", round(math.sqrt(pNum1), 2))

def sine(pNum1):
    print("The answer is ", round(math.sin(pNum1*(180/pi)), 2))
def cosine(pNum1):
    print("The answer is ", round(math.cos(pNum1), 5))

def tangent(pNum1):
    print("The answer is ", round(math.tan(pNum1), 5))

def hypotenuse(pNum1, pNum2):
    hyp = math.sqrt(pNum1**2 + pNum2**2)
    print("The hypotenuse is ", round(hyp, 2))

def adjacent(pNum1, pNum2):
    adj = math.sqrt(pNum1**2 - pNum2**2)
    print("The adjacent is ", round(adj, 2))

def opposite(pNum1, pNum2):
    opp = math.sqrt(pNum1**2 - pNum2**2)
    print("The opposite is ", round(opp, 2))

def sphere(pNum1):
    print("The volume of the sphere is ", round(4.0/3.0*pi*pNum1**3, 2))

def circle(pNum1):
    print("The surface area of the circle is ", round(pi*pNum1**2, 2))

def circumference(pNum1):
    print("The circumference of the circle is ", round(pi*pNum1*2), 2)

def Asquare(pNum1):
  print("The area of the square is: ", round(pNum1 * pNum1))
#Function for starrt  
def start():
  print("|||WELCOME TO THE ULTIMATE CALCULATOR|||")
  print("Instructions: ")
  print("For addition use + operator")
  print("For subtraction use - operator")
  print("For division use / ")
  print("For multiplication use * OR the letter 'x'")
  print("For exponents use ** OR ^")
  print("To square root, use 'sqrt'")
  print("To find the hypotenuse, use 'hypo'")
  print("To find the adjacent, use 'adj'")
  print("To find the opposite, use 'opp'")
  print("To use sin use 'sin' (calculated in radians)")
  print("To use cos use 'cos' (calculated in radians)")
  print("To use tan use 'tan' (calculated in radians)")
  print("To calculate the volume of a sphere, use 'sph'")
  print("To calculate the surface area of a circle, use 'circ'")
  print("To calculate the area of a square, use 'sqr' ")
  print("- - - - - - - - - - - - - - - -") 
  time.sleep(0.1)
  operation = str(input("Enter the operation: "))
  if operation == "sqrt" or operation == "sin" or operation == "cos" or operation == "tan" or operation == "sph" or operation == "circ" or operation == "sqr":
    num1 = float(input("Enter the number: "))
    if num1 == 69 or num1 == 420:
      print("Ok, that has to be a joke. ")
    if operation == "sqrt":
     squareRoot(num1)
    if operation == "sin":
      sine(num1)
    if operation == "cos":
      cosine(num1)
    if operation == "tan":
      tangent(num1)
    if operation == "sph":
      sphere(num1)
    if operation == "circ":
      circle(num1)
  elif operation == "hyp":
    num1 = float(input("Enter the adjacent: "))
    num2 = float(input("Enter the opposite: "))
    adjacent(num1,num2)
  elif operation == "adj":
    num1 = float(input("Enter the hypotenuse: "))
    num2 = float(input("Enter the opposite: "))
    hypotenuse(num1, num2)
  elif operation == "opp":
    num1 = float(input("Enter the hypotenuse: "))
    num2 = float(input("Enter the adjacent: "))
    opposite(num1, num2)
  elif operation == "sqr":
    num1 = float(input("Enter the length of one side: "))
    Asquare(num1)
  else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    circumference(num1)
    #operations
    if operation == "+":
      addition(num1, num2)
    elif operation == "*" or operation == "x" :
      multiply(num1, num2)
    elif operation == "/":
      divide(num1, num2)
    elif operation == "-":
      subtract(num1, num2)
    elif operation == "**" or operation == "^":
      square(num1, num2)
    else:
      print("How am I suppose to know that? ")
  sel = input("Do you want to restart? (yes/no) ")
  if sel == "yes":
    os.system("clear")
    start()
  if sel == "no":
    print("Then off you go")

start()