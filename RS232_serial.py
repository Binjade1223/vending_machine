import serial

ser=serial.Serial("COM8" , 115200)

def hex2str(data):
    data = repr(data)
    if 'x' not in data:
        data = data[1].encode("hex")
    else:
        data = data[3:5]
    return data

def recv_pkt(ser):
    if ser.isOpen():
        print "open"
        reading = True
    pkt = []
    a5_num = 0
    while reading:
        data = ser.read()
        if hex2str(data) == 'af':
            pkt.append(hex2str(data))
            data = ser.read()
            pkt.append(hex2str(data))
        else:
            if hex2str(data) == 'a5':
                pkt.append(hex2str(data))
                a5_num += 1
            else:
                pkt.append(hex2str(data))
        if a5_num == 2:
            reading = False
    ser.close()
    
    return pkt

def pkt_append(pkt, data):
    # check whether we need to add 'Escape Char'
    if data == None:
        pass
    elif (data == 0xa5) or (data == 0xaf):
        pkt.append(0xaf)
        pkt.append(data)
    elif type(data)==list:
        for i in data:
            pkt.append(i)
    else:
        pkt.append(data)

def assign_param(cmd, channel):
    if cmd == 0x01: # Polling
        return None
    elif cmd == 0x21: # Flow channel check
        return channel 
    elif cmd == 0x22: # Execution of transactions
        #[0]: channel; [1:2]: transaction code; [3:6]: price
        param = [channel, 0x10, 0, 0, 0, 0, 1]
        return param
    else:
        print "Warning: Command not found."

def check_cum_XOR(sn, cmd, param): # a little bit complex... (but confirmed)
    ans = []
    elements = [sn, cmd, param]
    carry = 0
    for i in xrange(2):
        a = 0
        for j in elements:
            j = hex(j)
            if len(j) != 4:
                j = j[:2] + '0' + j[2:]
            a += int(j[-(i+1)], 16)
        add = a % 16
        ans.append(hex((add + carry) ^ 0xf)[2])
        carry = a / 16
    ans = ans[1]+ans[0]
    return int(ans, 16)

def check_sum(sn, cmd, param):
    if param == None:
        param = 0
    return check_cum_XOR(sn, cmd, param)

def send_pkt(ser, sn, cmd, channel=None):
    # sn: 'Serial Number'; cmd: 'Command'
    packet = bytearray()
    
    packet.append(0xa5) # add Interval Char (0xa5) ---START---

    pkt_append(packet, sn) # add SN
    pkt_append(packet, cmd) # add CMD
    param = assign_param(cmd, channel) # add PARAMETERS
    pkt_append(packet, param)
    checksum = check_sum(sn, cmd, param)
    pkt_append(packet, checksum) # add  CHECKSUM

    packet.append(0xa5) # add Interval Char (0xa5) ---END---
    
    ser.write(packet) # send
    ser.close()

def modify_recv_pkt(data): # input: a list from recv_pkt
    data, new_data = data[1:-1], [] # cut head and tail
    be_aware = False
    for i in data:
        if i == 'af':
            if be_aware:
                new_data.append(i)
            else:
                be_aware = True
        else:
            new_data.append(i)
    SN = new_data[0]
    CMD = new_data[1]
    Parameter = new_data[2:-1]
    Checksum = new_data[-1]
    return [SN, CMD, Parameter, Checksum]

def check_recv_pkt(send_sn, recv_sn):
    # TODO: check whether the pkt is correct or not
    pass

def decode_recv_pkt(data): # input: a list from modify_recv_pkt
    # TODO: decode the meaning of the pkt(from VMC)
    pass
