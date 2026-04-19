import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

# Entry box
entry = tk.Entry(root, width=18, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button style
btn_style = {
    "font": ("Arial", 12),
    "width": 5,
    "height": 2,
    "bd": 2
}

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, bg="#00c853", fg="white",
                        command=calculate, **btn_style)
    elif text in ['+', '-', '*', '/']:
        btn = tk.Button(root, text=text, bg="#ff9800", fg="white",
                        command=lambda t=text: click(t), **btn_style)
    else:
        btn = tk.Button(root, text=text, bg="#424242", fg="white",
                        command=lambda t=text: click(t), **btn_style)

    btn.grid(row=row, column=col, padx=5, pady=5)

# Extra buttons
tk.Button(root, text="C", bg="#d32f2f", fg="white",
          command=clear, **btn_style).grid(row=5, column=0, padx=5, pady=5)

tk.Button(root, text="⌫", bg="#1976d2", fg="white",
          command=delete, **btn_style).grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="√", bg="#9c27b0", fg="white",
          command=square_root, **btn_style).grid(row=5, column=2, padx=5, pady=5)

# Run app
root.mainloop()