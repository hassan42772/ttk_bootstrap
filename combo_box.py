from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
from ttkbootstrap.constants import *
root=  Tk()
root.geometry("400x400")


def fun():
    if (combo.get()=="male"):
        lb.config(image=image2)
    elif (combo.get()=="female"):
        lb.config(image=image1)
    elif (combo.get()=="gay"):
        lb.config(image=image3)  
    elif (combo.get()=="exit"):
        root.quit()
vlist=["male","female","gay","exit"]
image1=Image.open("female.jpg")
image1=image1.resize((200,200), resample=Image.Resampling.LANCZOS)
image1=ImageTk.PhotoImage(image1)
image2=Image.open("male.jpg")
image2=image2.resize((200,200), resample=Image.Resampling.LANCZOS)
image2=ImageTk.PhotoImage(image2)
image3=Image.open("gay.jpg")
image3=image3.resize((200,200), resample=Image.Resampling.LANCZOS)
image3=ImageTk.PhotoImage(image3)
image4=Image.open("no.jpg")
image4=image4.resize((200,200), resample=Image.Resampling.LANCZOS)
image4=ImageTk.PhotoImage(image4)
combo=ttk.Combobox(root,values=vlist,bootstyle="danger")
combo.set("Pick an option")
combo.configure(state="readonly")
combo.pack(padx=5,pady=5)
button=ttk.Button(root,text="click me!!!",bootstyle="danger",command=fun)
button.pack(padx=5,pady=5)
lb=Label(root,image=image4)
lb.pack(padx=5,pady=5)


root.mainloop()