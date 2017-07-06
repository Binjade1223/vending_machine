#!/usr/bin/env python
# -*- coding: utf8 -*-
import button_input
import rfid_read
import server_connection as SC

def main():
    while True:
        product_num = None
        wait_button_input = True

        while wait_button_input: # customers choose their drinks
            product_num = button_input.get_button_input()
            if product_num != None:
                wait_button_input = False

        card_ID = rfid_read.read()
        print [card_ID, product_num]

        


if __name__ == '__main__':
    main()
