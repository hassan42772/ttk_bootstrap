from tkinter import *
from tkinter import ttk
from ttkbootstrap.constants import *
root=  Tk()
root.geometry("400x400")
import tkinter as tk
from tkinter import ttk

def on_enter(event):
    # Set focus to the second Entry widget when Enter key is pressed in the first Entry widget
    entry2.focus_set()

# Create a Tkinter window
root = tk.Tk()
root.title("Move Cursor on Enter Key")

# Create two ttk Entry widgets
entry1 = ttk.Entry(root)
entry1.pack(pady=10)
entry1.bind('<Return>', on_enter)

entry2 = ttk.Entry(root)
entry2.pack(pady=10)

root.mainloop()

# entry1=ttk.Entry(bootstyle="danger")
# entry1.pack()
# entry2=ttk.Entry(bootstyle="danger")
# entry2.pack()
# entry1.bind('<Return>',)
root.mainloop()