#import Tkinter as tk

from Tkinter import *

master = Tk()

w = Canvas(master, width=2000, height=100)
w.pack()
"""
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
"""
w.create_text(300,20,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")
w.create_text(300,40,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")
w.create_text(300,60,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")

mainloop()
