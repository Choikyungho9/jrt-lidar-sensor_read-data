import time

import serial

import select

import sys

 

def input_with_timeout(prompt, timeout):

    sys.stdout.write(prompt)

    sys.stdout.flush()

    ready, _, _ = select.select([sys.stdin], [],[], timeout)

    if ready:

        return sys.stdin.readline().rstrip('\n') 

    return None

 

try:

    ser = serial.Serial(

        port='/dev/ttyUSB0', 

        baudrate = 19200,

        parity=serial.PARITY_NONE,

        stopbits=serial.STOPBITS_ONE,

        bytesize=serial.EIGHTBITS,

        timeout=0.01

        )

    while True:

        ser.write('F'.encode('utf-8'))

        s_rcv = ser.readline().rstrip(b'\r').decode('utf-8')

        if s_rcv != '':

            if s_rcv == 'exit':

                break

            else:

                print(s_rcv)

        s_snd = input_with_timeout('', 0.001) 

        if s_snd != None:

            ser.write((s_snd + '\n').encode('utf-8')) 

 

except KeyboardInterrupt:

    print("Pressed 'Ctrl+C'")

 

except (OSError, serial.SerialException):

    print("Check Serial port")

 

else:

    ser.close()

 

finally:

    print("exit")
