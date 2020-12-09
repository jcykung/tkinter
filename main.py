import tkinter as tk

def pprint():
    print("Hello")

root = tk.Tk()

lab = tk.Label(root, text="Hello World")
lab.grid(row=0, column=1)

button = tk.Button(root, text="Click")
button.grid(row=0, column=0)
button["command"] = pprint

root.mainloop()