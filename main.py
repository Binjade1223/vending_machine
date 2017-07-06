#!/usr/bin/env python
# -*- coding: utf8 -*-
import time

import button_input
import rfid_read
import server_connection as SC


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

        print "Welcome to use vendind machine in III."
        
        product_num = None
        wait_button_input = True

        while wait_button_input: # customers choose their drinks
            product_num = button_input.get_button_input()
            if product_num != None:
                wait_button_input = False

        #params needed to be transfered to C_coin server
        card_ID = rfid_read.read()
        product_price = products_list[product_num][price_index]

        print [card_ID, product_price]
        
        SC.serverConnect(card_ID, product_price)
        time.sleep(1)


if __name__ == '__main__':
    main()
