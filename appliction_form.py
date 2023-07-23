from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
from ttkbootstrap.constants import *
from datetime import date
import ttkbootstrap as ttk
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
# create root
root=  Tk()
root.geometry("600x400")
root.title("Applicationo Form")
root.iconbitmap(r'form.ico')
# frame
main_frame=Frame(root)
main_frame.pack(fill="both",expand=True)
# splash screen
def splach_screen():
    global image_frame
    image_frame=Frame(main_frame)
    image_frame.pack(fill="both",expand=True)
    splash=TkinterVideo(image_frame)
    splash.load("APPLICATION FORMD_2.mp4")
    splash.pack(fill="both",expand=True)
    splash.play()
def destory_splash():
     image_frame.destroy()
def home():
    global second_frame
    def chek():
        if (var1.get()==1):
            c1.config(text="Waiting")
            lb.config(image=image6)
        elif(var1.get()==0):
            c1.config(text="click to verify")
            lb.config(image=image5)
    def chek1():
        if (var2.get()==1):
            c2.config(text="Waiting")
            lb1.config(image=image6)
        elif(var2.get()==0):
            c2.config(text="click to verify")
            lb1.config(image=image5)
    def chek2():
        if (var3.get()==1):
            c3.config(text="Waiting")
            lb2.config(image=image6)
        elif(var3.get()==0):
            c3.config(text="click to verify")
            lb2.config(image=image5)
    def chek3():
        if (var4.get()==1):
            c4.config(text="Waiting")
            lb3.config(image=image6)
        elif(var4.get()==0):
            c4.config(text="click to verify")
            lb3.config(image=image5)
    def eny():
        nm=n_entry.get()
        rn=r_entry.get()
        if  (n_entry.get()==nm)  and (r_entry.get()==int(rn))  and (var1.get()==1)and (var2.get()==1)and (var3.get()==1)and (var4.get()==1)and (d_combo.get()=="BS physics") or(d_combo.get()=="BS Math")or(d_combo.get()=="BS Computer Science") or (d_combo.get()=="BS Chemistry") or (s_combo.get()=="1")or (s_combo.get()=="2")or (s_combo.get()=="3")or (s_combo.get()=="4")or (s_combo.get()=="5")or (s_combo.get()=="6")or (s_combo.get()=="7")or (s_combo.get()=="8"):
            lb.config(image=image1)
            lb1.config(image=image2)
            lb2.config(image=image3)
            lb3.config(image=image4)
            c1.config(text="verify")
            c2.config(text="verify")
            c3.config(text="verify")
            c4.config(text="verify")
            messagebox.showinfo("verification message", "Verification Done")
        else :
            (var1.get()==0)  and (var1.get()==0) and (var1.get()==0) and (var1.get()==0)
            lb.config(image=image5)
            lb1.config(image=image5)
            lb2.config(image=image5)
            lb3.config(image=image5)
            c1.config(text="click to verify")
            c2.config(text="click to verify")
            c3.config(text="click to verify")
            c4.config(text="click to verify") 
    # frame
    second_frame=Frame(main_frame)
    second_frame.pack(fill="both",expand=True)
    # images
    image6=Image.open("wait.jpg")
    image6=image6.resize((50,50), resample=Image.Resampling.LANCZOS)
    image6=ImageTk.PhotoImage(image6)
    image5=Image.open("rej.webp")
    image5=image5.resize((50,50), resample=Image.Resampling.LANCZOS)
    image5=ImageTk.PhotoImage(image5)
    image1=Image.open("verify.jpg")
    image1=image1.resize((50,50), resample=Image.Resampling.LANCZOS)
    image1=ImageTk.PhotoImage(image1)
    image2=Image.open("verify.jpg")
    image2=image2.resize((50,50), resample=Image.Resampling.LANCZOS)
    image2=ImageTk.PhotoImage(image2)
    image3=Image.open("verify.jpg")
    image3=image3.resize((50,50), resample=Image.Resampling.LANCZOS)
    image3=ImageTk.PhotoImage(image3)
    image4=Image.open("verify.jpg")
    image4=image4.resize((50,50), resample=Image.Resampling.LANCZOS)
    image4=ImageTk.PhotoImage(image4)
    # image label
    lb=Label(second_frame,image=image5)
    lb.grid(column=3,row=1,padx=15,pady=5)
    lb1=Label(second_frame,image=image5)
    lb1.grid(column=3,row=2,padx=15,pady=5)
    lb2=Label(second_frame,image=image5)
    lb2.grid(column=3,row=3,padx=15,pady=5)
    lb3=Label(second_frame,image=image5)
    lb3.grid(column=3,row=4,padx=15,pady=5)
    #  date entry
    dt2=date(2023,12,30)
    d_entRy=ttk.DateEntry(second_frame,bootstyle="success",dateformat='%Y-%m-%d',firstweekday=2,startdate=dt2)
    d_entRy.grid(column=0,row=0,padx=200,columnspan=4)
    # label
    name_label=Label(second_frame,text="Name",font="Garamond 15 bold",fg="white",bg="black")
    name_label.grid(column=0,row=1,pady=15)
    roll_label=Label(second_frame,text="Roll No",font="Garamond 15 bold",fg="white",bg="black")
    roll_label.grid(column=0,row=2,pady=15)
    dept_label=Label(second_frame,text="Department",font="Garamond 15 bold",fg="white",bg="black")
    dept_label.grid(column=0,row=3,pady=15)
    sem_label=Label(second_frame,text="Semester",font="Garamond 15 bold",fg="white",bg="black")
    sem_label.grid(column=0,row=4,pady=15)
    # entry
    n_entry=Entry(second_frame,width=25)
    n_entry.grid(row=1,column=1,pady=15)
    r_entry=Entry(second_frame,width=25)
    r_entry.grid(row=2,column=1,pady=15)
    # check button
    var1=ttk.IntVar()
    var2=ttk.IntVar()
    var3=ttk.IntVar()
    var4=ttk.IntVar()
    c1=ttk.Checkbutton(second_frame,text="click to verify ",variable=var1,onvalue=1,offvalue=0, bootstyle="success-round-toggle",command=chek)
    c1.grid(column=2,row=1,pady=15)
    c2=ttk.Checkbutton(second_frame,text="click to verify ",variable=var2,onvalue=1,offvalue=0, bootstyle="success-round-toggle",command=chek1)
    c2.grid(column=2,row=2,pady=15)
    c3=ttk.Checkbutton(second_frame,text="click to verify ",variable=var3,onvalue=1,offvalue=0, bootstyle="success-round-toggle",command=chek2)
    c3.grid(column=2,row=3,pady=15)
    c4=ttk.Checkbutton(second_frame,text="click to verify ",variable=var4,onvalue=1,offvalue=0, bootstyle="success-round-toggle",command=chek3)
    c4.grid(column=2,row=4,pady=15)
    # combo box
    d_list=["BS physics","BS Chemistry","BS Math","BS Computer Science"]
    d_combo=ttk.Combobox(second_frame,values=d_list,bootstyle="success")
    d_combo.set("Select Department")
    d_combo.configure(state="readonly")
    d_combo.grid(column=1,row=3,pady=15)
    s_list=["1","2","3","4","5","6","7","8"]
    s_combo=ttk.Combobox(second_frame,values=s_list,bootstyle="success")
    s_combo.set("Select Semester")
    s_combo.configure(state="readonly")
    s_combo.grid(column=1,row=4,pady=15)
    # button
    b1= ttk.Button(second_frame, text="Click To Verify", bootstyle="success",command=eny)
    b1.grid(row=5, column=1, padx=30, pady=30)
splach_screen()
root.after(4000,destory_splash)
root.after(4000,home)
root.mainloop()