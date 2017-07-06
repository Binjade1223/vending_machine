import json
import requests

def server_interaction(uid = None, price = None):

    host = "http://192.168.50.87:4000"

    if (uid != None) & (price != None):

        # Warning: uid and account binding is better to be deployed on the server
        if uid==[58,249,134,171]:
            USER = "test3333@iii.org"
            PASSWORD = "lablab"
            MERCHANT = "test2222@iii.org"
        elif uid==[245,82,168,43]:
            USER = "test2222@iii.org"
            PASSWORD ="lablab"
            MERCHANT = "test3333@iii.org"

        login_data = resp(host, "login", [USER, PASSWORD])
        login_result = login_data["result"][0]
        login_ID = login_data["result"][2]

        if login_result:
            transfer_data = resp(host, "transfer", [USER, login_ID , MERCHANT, str(price)])
            transfer_result = transfer_data["result"][0]

            if transfer_result:
                qB_data = resp(host, "queryBalance", [USER, login_ID, USER])
                qB_result = qB_data["result"][0]
                balance = qB_data["result"][1]
                print "Balance: " + str(balance)

                if qB_result:
                    logout_data = resp(host, "logout", [USER, login_ID, USER])
                    logout_result = logout_data["result"][0]

                    if logout_result:
                        return True

                    else:
                        print ("logout fail")
                        return False
                else:
                    print ("queryBalance fail")
                    return False
            else:
                print ("transfer fail")
                return False
        else:
            print ("login fail")
            return False

def resp(host, method, params):
    #the bool params below is to decode json pkt
    true = True
    false = False
    #actions defined
    actions = ["login", "logout", "transfer", "queryBalance"]

    if method in actions:
        payload = {"method": method, "params": params, "jsonrpc": "2.0", "id": 0,}
        r = requests.post(host, json.dumps(payload))
        response = eval(r.text)
        return(response)
    
    else:
        mInteract.myPrint("Err: Method not defined", "Request error")
        return
