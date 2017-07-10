#!/usr/bin/env python
# -*- coding: utf8 -*-
import time

import button_input
import rfid_read
import get_product
import server_connection as sc

# Warning: products_list is better to be deployed on the server
products_list = [["iii_ex", 9999999],
                 ["Coke", 15],
                 ["Milk", 30],
                 ["Soymilk", 20],
                 ["Orange juice", 25],
                 ["Apple juice", 25],
                 ["Grape juice", 25]
                 ]
price_index = 1

def main():
    time_start = time.time()
    while True:
        print ("Welcome to use vending machine in III.")
        print ("Below are our drinks:")

        j=0
        for i in products_list:
            print str(j) + ". Drinks: " + i[0] + ", Price: " + str(i[1])
            j+=1

        product_index = None
        product_num = None
        wait_button_input = True

        while wait_button_input: # customers choose their drinks
            product_index = button_input.get_button_input()
            if product_index != None:
                wait_button_input = False

        print("Quantity ?")
        quantity = button_input.get_button_input()
        
        #params needed to be transfered to C_coin server
        card_ID = rfid_read.read()
        product_price = products_list[product_index][price_index] * quantity

        #add transaction to buffer
        tb = sc.transaction_buffer("transaction_buffer.json")
        buffer_balance = tb.queryT(card_ID)
        server_balance = sc.server_balance(card_ID)
        payment = quantity * product_price

        if server_balance - buffer_balance > payment: #check whether the user has enough money or not
            payload = {"price": product_price, "uid": card_ID, "sent":False, "quantity": quantity }
            tb.addT(payload)
            print("Here you go.")
            print("")
            print("")
        else:
            print("Insufficient balance")

        #transfer the data to server in transaction_buffer.json
        tb.transferT()
        
        time_end = time.time()
        if time_end - time_start > 300:
            tb.deleteT()
            time_start = time.time()

        time.sleep(3)

if __name__ == '__main__':
    main()
