#!/usr/bin/env python
# -*- coding: utf8 -*-
import time

import button_input
import rfid_read
import get_product
import server_connection as SC

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
    while True:
        print ("Welcome to use vendind machine in III.")
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
        
        result = SC.server_interaction(card_ID, product_price)
        if result:
            #TODO: let the machine drop the drinks 
            print("Here you go.")
        else:
            print("Sorry! Try later.")

        time.sleep(2)


if __name__ == '__main__':
    main()
