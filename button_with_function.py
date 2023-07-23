import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("400x150") # width and height of the window 
def change():
    b4.config(state="ABLE")
def change1():
    b4.config(state="disabled")
var1=ttk.StringVar()
var2=ttk.StringVar()
b4= ttk.Button(my_w, text="Button Primary", bootstyle=DARK,state="disabled")
b4.grid(row=0, column=0, padx=30, pady=30)

b5= ttk.Button(my_w, text="Button Primary",bootstyle=DARK,command=change)
b5.grid(row=0, column=1, padx=30, pady=30)

b6= ttk.Button(my_w, text="Button Primary", bootstyle=DARK,command=change1)
b6.grid(row=0, column=2, padx=30, pady=30)

my_w.mainloop()