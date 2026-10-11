import serial

filename = "data.txt"

def read_serial(comport, baudrate):
    data = ''

    ser = serial.Serial(comport, baudrate, timeout=0.1)

    while True:
        line = ser.readline().decode().strip()

        if line == '\n' or line == '': 
            continue
        
        if line == "END": 
            fstream = open(filename, 'a')
            fstream.write(data)
            fstream.close()
            return None
        
        correction = input("Please sensor's x, y position in format <x, y> without brackets ").strip()
        data += line + ', ' + correction + '\n'