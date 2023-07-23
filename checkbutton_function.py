import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("400x150")
def play():
    if(var1.get()==1) and(var2.get()==0):
        b1.config(state="abled")
    elif(var1.get()==0) and(var2.get()==1):
        b1.config(state="abled")
    elif(var1.get()==0) and(var2.get()==0):
        b1.config(state="disabled")
    else:
        b1.config(state="disabled")
var1=ttk.IntVar()
var2=ttk.IntVar()

c1=ttk.Checkbutton(my_w,text="yes",variable=var1,onvalue=1,offvalue=0, bootstyle=INFO,command=play)
c1.pack(side="top")

b1 = ttk.Button(my_w, text="Button Success", bootstyle="info-link",state="disable")
b1.pack(side="bottom")

c2=ttk.Checkbutton(my_w,text="no",variable=var2,onvalue=1,offvalue=0, bootstyle="danger",command=play)
c2.pack(side="top",pady=20)
my_w.mainloop()


