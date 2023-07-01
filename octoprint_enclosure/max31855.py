import ctypes
import struct
import sys

import board
import digitalio
import adafruit_max31855


def main():

    spi = board.SPI()
    cs = digitalio.DigitalInOut(board.D5)


    sensor = adafruit_max31855.MAX31855(spi, cs)

    temp = sensor.temperature

    print('{0:0.1f}'.format(temp))

if __name__ == "__main__":
    main()
