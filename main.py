#!/usr/bin/env python3

try:
    from pyfirmata2 import Arduino, util, INPUT, OUTPUT
except:
    import pip
    pip.main(['install', 'pyfirmata'])
    from pyfirmata2 import Arduino, util, INPUT, OUTPUT

import time

board = Arduino(Arduino.AUTODETECT)

it = util.Iterator(board)
it.start()

button = board.get_pin('d:2:i')

led_green = board.get_pin('d:3:o')
led_red = board.get_pin('d:5:o')

analog_input = board.get_pin('a:0:i')
sensor_input_1 = board.get_pin('a:1:i')

laser_input = board.get_pin('d:7:o')

while True:
    value = button.read()

    if value is True:
        led_green.write(1)
        led_red.write(0)

        laser_input.write(1)

        analog_value = analog_input.read()
        sensor_value = sensor_input_1.read()
        laser_value = laser_input.read()

        print(analog_value)
        print(sensor_value)
        print(laser_value)

        time.sleep(analog_value * 2)
    else:
        led_green.write(0)
        led_red.write(1)
        time.sleep(1)
