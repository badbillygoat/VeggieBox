#!/usr/bin/env python3
import LCD1602
import time


def write(line1display,line2display):
    LCD1602.init(0x27, 1)   # init(slave address, background light)
    LCD1602.write(0, 0, line1display)
    LCD1602.write(1, 1, line2display)
    time.sleep(2)

def destroy():
    LCD1602.clear()

write(str(4.0) + "F/ " + str(2.0) + "C",str(.33*100) + "% Humidity")