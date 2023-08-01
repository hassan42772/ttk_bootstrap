import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("400x100")  # width and height
c=0 # column value 
fg1 = ttk.Floodgauge(
    bootstyle=INFO,
    mask='INFO ' + '{}%',
    value=40,
    maximum=100,
    length=350    
    )
fg1.grid(row=1, column=1,padx=15,pady=10)

my_w.mainloop()