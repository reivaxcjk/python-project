import tkinter as tk
window = tk.Tk()
window.title("Simple Caculator")
input = tk.Entry(window, width=20, borderwidth=5, font=("Arial",20))
input.grid(row=0, column=0, columnspan=3)
pos = 0
number1 = []
number2 = []

#Creating the function for the buttons 1,2,3,4,5,6,7,8,9,0
def button_click(number):
    global pos
    input.insert(pos, str(number))
    pos += 1
    if "+" in number1:
        number2.append(str(number))
    elif "-" in number1:
        number2.append(str(number))
    elif "*" in number1:
        number2.append(str(number))
    elif "/" in number1:
        number2.append(str(number))
    else:
        number1.append(str(number))

#buttons 7,8,9
for x in range(7,10):
    button_x = tk.Button(window, text=x, padx=50, pady=15, command=lambda x=x: button_click(x))
    button_x.grid(row=1, column=x-7)

#buttons 4,5,6
for y in range(4,7):
    button_y = tk.Button(window, text=y, padx=50, pady=15, command=lambda y=y: button_click(y))
    button_y.grid(row=2, column=y-4)

#buttons 1,2,3
for z in range(1,4):
    button_z = tk.Button(window, text=z, padx=50, pady=15, command=lambda z=z: button_click(z))
    button_z.grid(row=3, column=z-1)

#button 0 
button_0 = tk.Button(window, text=0, padx=50, pady=15, command=lambda: button_click(0))
button_0.grid(row=4, column=0)

#Creating the function for the button +,-,*,/
def button_op_click(operator):
     global pos
     input.insert(pos, operator)
     pos += 1
     number1.append(operator)

#button +
button_plus = tk.Button(window, text="+", padx=50, pady=15, command=lambda: button_op_click("+"))
button_plus.grid(row=5, column=0)

#button -,*,/
operator_list = ["-","*","/"]
for place, i in enumerate(operator_list):
    button_i = tk.Button(window, text=i, padx=50, pady=15, command=lambda i=i: button_op_click(i))
    button_i.grid(row=6, column=place) 

#Creating the "=" button
def button_equal_click():
    if "+" in number1:
        number1.remove("+")
        number1_1 = int(''.join(number1))
        number2_2 = int(''.join(number2))
        result = number1_1 + number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    elif "-" in number1:
        number1.remove("-")
        number1_1 = int(''.join(number1))
        number2_2 = int(''.join(number2))
        result = number1_1 - number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    elif "*" in number1:
        number1.remove("*")
        number1_1 = int(''.join(number1))
        number2_2 = int(''.join(number2))
        result = number1_1 * number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    elif "/" in number1:
        number1.remove("/")
        number1_1 = int(''.join(number1))
        number2_2 = int(''.join(number2))
        result = number1_1 / number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    def button_clear_click():
        label.destroy()
        number1.clear()
        number2.clear()
    button_clear = tk.Button(window, text="Clear", padx=97, pady=15, command=button_clear_click)
    button_clear.grid(row=4, column=1, columnspan=2)
button_equal = tk.Button(window, text="=", padx=107, pady=15, command=button_equal_click)
button_equal.grid(row=5, column=1, columnspan=2)

#Creating the "Clear" button
def button_clear_click():
    input.delete(0,pos)
button_clear = tk.Button(window, text="Clear", padx=97, pady=15, command=button_clear_click)
button_clear.grid(row=4, column=1, columnspan=2)

window.mainloop()