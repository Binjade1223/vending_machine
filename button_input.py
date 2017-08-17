# -*- coding: utf8 -*-

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()


def GUI():
   win = tk.Tk()
   win.title("Vending Machine")

   # some_products_data
   products_list = [["iii_ex", 9999999],
                    ["Coke", 15],
                    ["Milk", 30],
                    ["Soymilk", 20],
                    ["Orange juice", 25],
                    ["Apple juice", 25],
                    ["Grape juice", 25]
                    ]

   # label
   label_1 = tk.Label(win, text="Welcome to use vending machine in III.")
   label_2 = tk.Label(win, text="Below are our drinks:")
   label_3 = tk.Label(win, text="")
   label_1.pack() # display the label
   label_2.pack()
   label_3.pack()

   # button

   # product_button
   button_list = []
   for i in xrange(len(products_list)):
       product_price_str = str(products_list[i][1])
       button = tk.Button(win, text = str(i) + ". Product: " + products_list[i][0] +
                          "; Price: " + product_price_str, command = get_button_input(i))
       button_list.append(button)

   for i in button_list:
       i.pack()

   win.mainloop()
