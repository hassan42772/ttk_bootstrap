import tkinter as tk
from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
import time
import datetime

def on_scroll(*args):
    canvas.yview(*args)
    # for widget in widgets:
    #     widget.yview(*args)

root = tk.Tk()
root.title("Simple Scroll Bar")
root.geometry("650x450")
main=tk.Frame(root)
main.pack(fill="both",expand=True)
# Create a canvas and a vertical scrollbar
canvas = tk.Canvas(main)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(main, orient=tk.VERTICAL, command=on_scroll)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Create a frame to hold the widgets
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")
det_label=Label(frame,text=f"Minimum marks % of computer science",font="Garamond 15 bold",fg="white",bg="black")
det_label.pack(padx=100)
cs_meter = ttk.Meter(frame,
    metersize=130,
    padding=8,
    amountused=60,
    metertype="full",
    interactive= False,
    bootstyle='success',
    stripethickness=5,
    textright='%')
cs_meter.pack()
det_label1=Label(frame,text=f"Minimum marks % of software engineering",font="Garamond 15 bold",fg="white",bg="black")
det_label1.pack()
cs_meter = ttk.Meter(frame,
    metersize=130,
    padding=8,
    interactive= False,
    amountused=50,
    metertype="full",
    bootstyle='success',
    stripethickness=5,
    textright='%')
cs_meter.pack()
det_label2=Label(frame,text=f"Minimum marks %  of computer science",font="Garamond 15 bold",fg="white",bg="black")
det_label2.pack()
cm_meter = ttk.Meter(frame,
metersize=130,
padding=8,
amountused=60,
metertype="full",
interactive= False,
bootstyle='success',
stripethickness=5,
textright='%')
cm_meter.pack()
det_label3=Label(frame,text=f"Minimum marks %  of software engineering",font="Garamond 15 bold",fg="white",bg="black")
det_label3.pack()
m_meter = ttk.Meter(frame,
metersize=130,
padding=8,
interactive= False,
amountused=50,
metertype="full",
bootstyle='success',
stripethickness=5,
textright='%')
m_meter.pack()


# Configure the canvas to update its scroll region
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", configure_canvas)



root.mainloop()
