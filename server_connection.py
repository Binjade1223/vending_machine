import json
import requests
import machine_interaction as mInteract

"""
TODO:
1. serverConnect >>> "login", "logout", "transfer", "queryBalance"
2. 
"""
def serverConnect(card = None, product = None):
    if (product != None) && (card != None):
            r = req("", "login", card ) #card information to be modified
            if r != None:
                


def resp(host, method, params):
    actions = ["login", "logout", "transfer", "queryBalance"]
    if method in actions:
        payload = {"method": method, "params": params, "jsonrpc": "2.0", "id": 0,}
        r = requests.post(host, json = payload)
        return r
    else:
        mInteract.myPrint("Err: Method not defined", "Request error")
        return None
