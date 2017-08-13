# This is an VMC Emulator
import serial

def hex2str(data):
    data = repr(data)
    if 'x' not in data:
        data = data[1].encode("hex")
    else:
        data = data[3:5]
    return data

ser=serial.Serial("COM7" , 115200)

def recv_pkt(ser):
    if ser.isOpen():
        print "open (I am VMC_Emulator)"
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
    return pkt

def send_pkt(ser, sn, cmd, param):
    # sn: 'Serial Number'
    # cmd: 'Command'
    # param: 'Parameter'
    
    packet = bytearray()
    # add Interval Char (0xa5)
    packet.append(0xa5)
    # add SN
    if (sn == 0xa5) or (sn == 0xaf):
        packet.append(0xaf)
        packet.append(sn)
    else:
        packet.append(sn)
    # add CMD
    packet.append(0)
    # add PARAMETERS 
    packet.append(0x2)
    # add  CHECKSUM
    packet.append(0)
    # add Interval Char (0xa5)
    packet.append(0xa5)
    # send
    ser.write(packet)
    
print recv_pkt(ser)
ser.close()
