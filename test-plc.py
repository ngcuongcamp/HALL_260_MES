import serial

COM1 = "COM1"
COM2 = "COM2"
COM3 = "COM3"
COM4 = "COM4"
COM5 = "COM5"
COM6 = "COM6"

BAUDRATE = 9600


# connect COM 1
try:
    ser_1 = serial.Serial(
        port=COM1,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.0009,
    )
except Exception as E:
    print(E, "Error serial")


# connect COM 2
try:
    ser_2 = serial.Serial(
        port=COM2,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.0009,
    )
except Exception as E:
    print(E, "Error serial")


# connect COM 3
try:
    ser_3 = serial.Serial(
        port=COM3,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.0009,
    )
except Exception as E:
    print(E, "Error serial")


# connect COM 4
try:
    ser_4 = serial.Serial(
        port=COM4,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.0009,
    )
except Exception as E:
    print(E, "Error serial")

# connect COM 5
try:
    ser_5 = serial.Serial(
        port=COM5,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.0009,
    )
except Exception as E:
    print(E, "Error serial")


# connect COM 6
try:
    ser_6 = serial.Serial(
        port=COM6,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.0009,
    )
except Exception as E:
    print(E, "Error serial")


# READ DATA SEND FROM PLC

while True:
    signal_1 = ser_1.readline()
    signal_2 = ser_2.readline()
    signal_3 = ser_3.readline()
    signal_4 = ser_4.readline()
    signal_5 = ser_5.readline()
    signal_6 = ser_6.readline()

    if len(signal_1) > 0:
        print(f"Nhan tin hieu tu com 1: {signal_1}")
        ser_1.write(b"1")
        print("Da gui tien hieu 1 cho plc tu com 1")
    if len(signal_2) > 0:
        print(f"Nhan tin hieu tu com 2: {signal_2}")
        ser_2.write(b"1")
        print("Da gui tien hieu 1 cho plc tu com 2")
    if len(signal_3) > 0:
        print(f"Nhan tin hieu tu com 3: {signal_3}")
        ser_3.write(b"1")
        print("Da gui tien hieu 1 cho plc tu com 3")
    if len(signal_4) > 0:
        print(f"Nhan tin hieu tu com 4: {signal_4}")
        ser_4.write(b"1")
        print("Da gui tien hieu 1 cho plc tu com 4")
    if len(signal_5) > 0:
        print(f"Nhan tin hieu tu com 5: {signal_5}")
        ser_5.write(b"1")
        print("Da gui tien hieu 1 cho plc tu com 5")
    if len(signal_6) > 0:
        print(f"Nhan tin hieu tu com 6: {signal_6}")
        ser_5.write(b"1")
        print("Da gui tien hieu 1 cho plc tu com 6")
