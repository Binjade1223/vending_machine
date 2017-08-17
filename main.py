# -*- coding: utf8 -*-
import time
import rfid_read
import server_connection as sc
import RS232_serial as rs
#import VMC_Emulator as vmc

products_list = [["iii_ex", 9999999],
                 ["Coke", 15],
                 ["Milk", 30],
                 ["Soymilk", 20],
                 ["Orange juice", 25],
                 ["Apple juice", 25],
                 ["Grape juice", 25]
                 ]
def decode_pkt(cmd, recv_pkt):
    return rs.decode_recv_pkt(cmd, rs.modify_recv_pkt(recv_pkt))


def main():
    tb = sc.transaction_buffer("transaction_buffer.json")
    tb.deleteT()
    time_start = time.time()
    while True:
        print ("Welcome to use vending machine in III.")
        print ("Below are our drinks:")
        for i in xrange(len(products_list)):
            print str(i) + ". " + products_list[i][0] + "; $: " + str(products_list[i][1])
        index = int(raw_input("Please choose: "))
        ser = rs.assign_serial("COM7")
        rs.send_pkt(ser, 1, 33) # 33 means 0x21
        if decode_pkt('21',rs.recv_pkt(ser))[0]:
            print "Please touch your card"
            card_ID = rfid_read.read()
            if card_ID:
                print "Success: your cardID is" + str(card_ID)
                buffer_balance = tb.queryT(card_ID)
                if sc.server_balance(card_ID) != False:
                    server_balance = sc.server_balance(card_ID)
                else:
                    update_msg(label_3, "Err: server connection broke")

                product_price, quantity = products_list[index][1], 1
                payment =  quantity * product_price

                if type(server_balance) == str:
                    print server_balance
                    print "Please try later"
                else:
                    if server_balance - buffer_balance > payment: #check whether the user has enough money or not
                        payload = {"price": product_price, "uid": card_ID, "sent":False, "quantity": quantity }
                        new_balance = server_balance - buffer_balance - payment
                        rs.send_pkt(ser, 2, 34, index) # 34 means 0x22
                        
                        if decode_pkt('22', rs.recv_pkt(ser))[0]:
                            tb.addT(payload)
                            print "Here you go. Balance: " + str(new_balance)
                    else:
                        pre_balance = server_balance - buffer_balance
                        print ( "Insufficient balance. Balance: " + str(pre_balance))

                rs.serial_close(ser)
                #transfer the data to server in transaction_buffer.json
                tb.transferT()

                time.sleep(5)
                
main()
