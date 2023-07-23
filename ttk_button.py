import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("400x150") # width and height of the window 

b1 = ttk.Button(my_w, text="Button Success", bootstyle="info-link",state="disable")
b1.grid(row=0, column=0, padx=30, pady=30)

b2 = ttk.Button(my_w, text="Button Primary", bootstyle=PRIMARY)
b2.grid(row=0, column=1, padx=30, pady=30)

b3= ttk.Button(my_w, text="Button Primary", bootstyle="danger-outline")
b3.grid(row=0, column=2, padx=30, pady=30)

b4= ttk.Button(my_w, text="Button Primary", bootstyle=DARK)
b4.grid(row=0, column=3, padx=30, pady=30)
my_w.mainloop()