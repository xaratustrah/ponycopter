#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test raspi's PWM output for controlling an ESC

Be careful and use at your own risk.

2018 Xaratustrah

"""

from time import sleep
import pigpio
import sys

# Connect to pigpio
pi = pigpio.pi()

# Calibrate ESC
ESC_GPIO = 13  # GPIO13 which is pin number 33 on the Pi3 board

try:

    pi.set_servo_pulsewidth(ESC_GPIO, 0)  # Maximum throttle.
    input('Press any key whenever you are ready...')

    print('Setting up motor...')
    pi.set_servo_pulsewidth(ESC_GPIO, 2000)  # Maximum throttle.
    input('Connect LiPo then press any key...')

except KeyboardInterrupt:
    pi.set_servo_pulsewidth(ESC_GPIO, 0)  # Stop servo pulses.
    pi.stop()  # Disconnect pigpio.
    # quit
    sys.exit()


pi.set_servo_pulsewidth(ESC_GPIO, 1000)  # Minimum throttle.
sleep(0.5)


while True:
    try:
        a = input('Input number or ctrl-C to stop: ')
        try:
            assert(1000 < int(a) < 2000)
        except:
            print()
            print('Please enter a value in range 1000 and 2000')
            continue
        print('Setting the speed to ', a)
        # DO THINGS
        pi.set_servo_pulsewidth(ESC_GPIO, a)
    except KeyboardInterrupt:
        print()
        print('Exitting...')
        break

pi.set_servo_pulsewidth(ESC_GPIO, 0)  # Stop servo pulses.
pi.stop()  # Disconnect pigpio.
# quit
sys.exit()
