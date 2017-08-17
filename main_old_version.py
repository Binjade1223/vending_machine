#!/usr/bin/env python
# -*- coding: utf8 -*-
import time
import Tkinter as tk
import rfid_read
import server_connection as sc
import RS232_serial as rs

# Warning: products_list is better to be deployed on the server

msg = "Please click on the button"

products_list = [["iii_ex", 9999999],
                 ["Coke", 15],
                 ["Milk", 30],
                 ["Soymilk", 20],
                 ["Orange juice", 25],
                 ["Apple juice", 25],
                 ["Grape juice", 25]
                 ]

# TODO: channel_status = [False] * 24 # there are 24 channels of drinks 

def service_begin(index, product_price, quantity=1):
    ser = rs.assign_serial("COM1")
    rs.send_pkt(ser, 1, 33) # CMD 33 means '0x21'
    if type(rs.recv_pkt(ser)) == list:
        print rs.recv_pkt
        if rs.decode_recv_pkt('21',rs.modify_recv_pkt(rs.recv_pkt(ser)))[0]:
            update_msg(label_3, "Choose: " + str(index) + ". Please touch your rfid_card")
            card_ID = rfid_read.read()
            if card_ID: 
                update_msg(label_3, "Success: your cardID is" + str(card_ID))
                #add transaction to buffer
                buffer_balance = tb.queryT(card_ID)
                if sc.server_balance(card_ID) != False:
                    server_balance = sc.server_balance(card_ID)
                else:
                    update_msg(label_3, "Err: server connection broke")
                payment = quantity * product_price

                if type(server_balance) == str:
                    update_msg(label_3, server_balance)
                    update_msg(label_3, "Please try later")
                else:
                    if server_balance - buffer_balance > payment: #check whether the user has enough money or not
                        payload = {"price": product_price, "uid": card_ID, "sent":False, "quantity": quantity }
                        tb.addT(payload)
                        new_balance = server_balance - buffer_balance - payment
                        if type(rs.recv_pkt(ser)) == list:
                            if rs.decode_recv_pkt('21',rs.modify_recv_pkt(rs.recv_pkt(ser)))[0]:
                                update_msg(label_3, "Here you go. Balance: " + str(new_balance))
                    else:
                        pre_balance = server_balance - buffer_balance
                        update_msg(label_3, "Insufficient balance. Balance: " + str(pre_balance))

                #transfer the data to server in transaction_buffer.json
                tb.transferT()

                time.sleep(5)

def update_msg(label,m):
    msg=m
    def update():
        global msg
        label.config(text=m)
    update()
    
def main():
    global tb
    tb = sc.transaction_buffer("transaction_buffer.json")
    tb.deleteT()
    time_start = time.time()
    while True:
        global win
        win = tk.Tk()
        win.title("Vending Machine")

        # label
        global label_3
        label_1 = tk.Label(win, text="Welcome to use vending machine in III.")
        label_2 = tk.Label(win, text="Below are our drinks:")
        label_3 = tk.Label(win, text="Please click what you want", fg = "dark green")
        label_1.pack() # display the label
        label_2.pack()
        label_3.pack()

        # product_butt
        button_list = []
        
        for i in xrange(len(products_list)):
            product_price_str = str(products_list[i][1])
            button_list.append(tk.Button(win, text = str(i) + ". Product: " + products_list[i][0] +
                           "; Price: " + product_price_str, command = lambda i=i : service_begin(i,products_list[i][1])))
        
            button_list[-1].pack()
        
        
        win.mainloop()

        """
            #while nobody come to buy, buffer list will update 
            time_end = time.time()
            if time_end - time_start > 300:
                tb.deleteT()
                time_start = time.time()
        """

if __name__ == '__main__':
    # TODO: check all the channel, and save which channel is OK
    main()
