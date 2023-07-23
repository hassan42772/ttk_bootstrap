import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("400x150") # width and height of the window 


b4= ttk.Checkbutton(my_w, text="Button Primary", bootstyle=INFO)
b4.grid(row=0, column=0, padx=30, pady=30)

b5= ttk.Checkbutton(my_w, text="Button Primary", bootstyle="success-toolbutton")
b5.grid(row=0, column=1, padx=30, pady=30)

b6= ttk.Checkbutton(my_w, text="Button Primary", bootstyle="success-toolbutton-outline")
b6.grid(row=1, column=0, padx=30, pady=30)

b7= ttk.Checkbutton(my_w, text="Button Primary", bootstyle="success-round-toggle")
b7.grid(row=1, column=1, padx=30, pady=30)

b7= ttk.Checkbutton(my_w, text="Button Primary", bootstyle="success-square-toggle",state="disable")
b7.grid(row=2, column=0, padx=30, pady=30)



my_w.mainloop()
