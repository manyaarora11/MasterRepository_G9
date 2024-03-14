#THIS IS A LIBRABRY WHICH CONTAIN BUTTONS IN IT FOR USING THAT BUTTONS WE USED THAT LIBRARY 
from tkinter import * 
import math

#FOR ADDITION 
def add():
    numbers = [float(entry.get()) for entry in entry_list]
    result.set(sum(numbers))

#FOR SUBTRACTION
def subtract():
    numbers = [float(entry.get()) for entry in entry_list]
    result.set(numbers[0] - sum(numbers[1:]))

#FOR MULTIPLICATION
def multiply():
    numbers = [float(entry.get()) for entry in entry_list]
    result.set(math.prod(numbers))

#FOR DIVISION
def divide():
    numbers = [float(entry.get()) for entry in entry_list]
    result.set(numbers[0] / math.prod(numbers[1:]))

#FOR SQUARE ROOT
def square_root():
    number = float(entry_list[0].get())
    result.set(math.sqrt(number))

#DIFFERENT FUNCTIONS FOR TRIGNOMETRY 
def sine():
    number = float(entry_list[0].get())
    result.set(math.sin(math.radians(number)))

def cosine():
    number = float(entry_list[0].get())
    result.set(math.cos(math.radians(number)))

def tangent():
    number = float(entry_list[0].get())
    result.set(math.tan(math.radians(number)))

#HERE WE GAVE NAME TO OUR APPLICATION
root = Tk()
root.title('Calculator By Coder manya')

entry_list = []

for _ in range(3):  
    entry = Entry(root)
    entry.pack()
    entry_list.append(entry)

result = StringVar()
result_label = Label(root, textvariable=result)
result_label.pack()

add_button = Button(root, text='+', command=add)
subtract_button = Button(root, text='-', command=subtract)
multiply_button = Button(root, text='*', command=multiply)
divide_button = Button(root, text='/', command=divide)
sqrt_button = Button(root, text='√', command=square_root)
sin_button = Button(root, text='sin', command=sine)
cos_button = Button(root, text='cos', command=cosine)
tan_button = Button(root, text='tan', command=tangent)

add_button.pack(side=LEFT)
subtract_button.pack(side=LEFT)
multiply_button.pack(side=LEFT)
divide_button.pack(side=LEFT)
sqrt_button.pack(side=LEFT)
sin_button.pack(side=LEFT)
cos_button.pack(side=LEFT)
tan_button.pack(side=LEFT)

root.mainloop()
