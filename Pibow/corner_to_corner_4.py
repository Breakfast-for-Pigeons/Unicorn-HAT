#!/usr/bin/python3
"""
Corner to Corner 4 - Pibow

Moves a square from the upper left corner to the lower right corner.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
import unicornhat
from bfp_unicornhat import print_header
from bfp_unicornhat import stop

########################################################################
#                        Import Variables                              #
########################################################################

from bfp_unicornhat import C1
from bfp_unicornhat import C2
from bfp_unicornhat import C3
from bfp_unicornhat import C4
from bfp_unicornhat import C5
from bfp_unicornhat import C6
from bfp_unicornhat import C7
from bfp_unicornhat import C8

########################################################################
#                            Functions                                 #
########################################################################


def corner_to_corner_4():
    """
    Moves a square from the upper left corner to the lower right corner.
    """

    sleep_speed = 0.1
    off = (0, 0, 0)
    colors = [off, C1, C2, C3, C4, C5, C6, C7, C8]

    for color in colors:

        unicornhat.set_pixel(0, 0, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(1, 0, color)
        unicornhat.set_pixel(1, 1, color)
        unicornhat.set_pixel(0, 1, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(2, 0, color)
        unicornhat.set_pixel(2, 1, color)
        unicornhat.set_pixel(2, 2, color)
        unicornhat.set_pixel(1, 2, color)
        unicornhat.set_pixel(0, 2, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(3, 0, color)
        unicornhat.set_pixel(3, 1, color)
        unicornhat.set_pixel(3, 2, color)
        unicornhat.set_pixel(3, 3, color)
        unicornhat.set_pixel(2, 3, color)
        unicornhat.set_pixel(1, 3, color)
        unicornhat.set_pixel(0, 3, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(4, 0, color)
        unicornhat.set_pixel(4, 1, color)
        unicornhat.set_pixel(4, 2, color)
        unicornhat.set_pixel(4, 3, color)
        unicornhat.set_pixel(4, 4, color)
        unicornhat.set_pixel(3, 4, color)
        unicornhat.set_pixel(2, 4, color)
        unicornhat.set_pixel(1, 4, color)
        unicornhat.set_pixel(0, 4, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(5, 0, color)
        unicornhat.set_pixel(5, 1, color)
        unicornhat.set_pixel(5, 2, color)
        unicornhat.set_pixel(5, 3, color)
        unicornhat.set_pixel(5, 4, color)
        unicornhat.set_pixel(5, 5, color)
        unicornhat.set_pixel(4, 5, color)
        unicornhat.set_pixel(3, 5, color)
        unicornhat.set_pixel(2, 5, color)
        unicornhat.set_pixel(1, 5, color)
        unicornhat.set_pixel(0, 5, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(6, 0, color)
        unicornhat.set_pixel(6, 1, color)
        unicornhat.set_pixel(6, 2, color)
        unicornhat.set_pixel(6, 3, color)
        unicornhat.set_pixel(6, 4, color)
        unicornhat.set_pixel(6, 5, color)
        unicornhat.set_pixel(6, 6, color)
        unicornhat.set_pixel(5, 6, color)
        unicornhat.set_pixel(4, 6, color)
        unicornhat.set_pixel(3, 6, color)
        unicornhat.set_pixel(2, 6, color)
        unicornhat.set_pixel(1, 6, color)
        unicornhat.set_pixel(0, 6, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(7, 0, color)
        unicornhat.set_pixel(7, 1, color)
        unicornhat.set_pixel(7, 2, color)
        unicornhat.set_pixel(7, 3, color)
        unicornhat.set_pixel(7, 4, color)
        unicornhat.set_pixel(7, 5, color)
        unicornhat.set_pixel(7, 6, color)
        unicornhat.set_pixel(7, 7, color)
        unicornhat.set_pixel(6, 7, color)
        unicornhat.set_pixel(5, 7, color)
        unicornhat.set_pixel(4, 7, color)
        unicornhat.set_pixel(3, 7, color)
        unicornhat.set_pixel(2, 7, color)
        unicornhat.set_pixel(1, 7, color)
        unicornhat.set_pixel(0, 7, color)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(0, 0, off)
        unicornhat.set_pixel(1, 0, off)
        unicornhat.set_pixel(2, 0, off)
        unicornhat.set_pixel(3, 0, off)
        unicornhat.set_pixel(4, 0, off)
        unicornhat.set_pixel(5, 0, off)
        unicornhat.set_pixel(6, 0, off)
        unicornhat.set_pixel(7, 0, off)
        unicornhat.set_pixel(0, 1, off)
        unicornhat.set_pixel(0, 2, off)
        unicornhat.set_pixel(0, 3, off)
        unicornhat.set_pixel(0, 4, off)
        unicornhat.set_pixel(0, 5, off)
        unicornhat.set_pixel(0, 6, off)
        unicornhat.set_pixel(0, 7, off)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(1, 1, off)
        unicornhat.set_pixel(2, 1, off)
        unicornhat.set_pixel(3, 1, off)
        unicornhat.set_pixel(4, 1, off)
        unicornhat.set_pixel(5, 1, off)
        unicornhat.set_pixel(6, 1, off)
        unicornhat.set_pixel(7, 1, off)
        unicornhat.set_pixel(1, 2, off)
        unicornhat.set_pixel(1, 3, off)
        unicornhat.set_pixel(1, 4, off)
        unicornhat.set_pixel(1, 5, off)
        unicornhat.set_pixel(1, 6, off)
        unicornhat.set_pixel(1, 7, off)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(2, 2, off)
        unicornhat.set_pixel(3, 2, off)
        unicornhat.set_pixel(4, 2, off)
        unicornhat.set_pixel(5, 2, off)
        unicornhat.set_pixel(6, 2, off)
        unicornhat.set_pixel(7, 2, off)
        unicornhat.set_pixel(2, 3, off)
        unicornhat.set_pixel(2, 4, off)
        unicornhat.set_pixel(2, 5, off)
        unicornhat.set_pixel(2, 6, off)
        unicornhat.set_pixel(2, 7, off)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(3, 3, off)
        unicornhat.set_pixel(4, 3, off)
        unicornhat.set_pixel(5, 3, off)
        unicornhat.set_pixel(6, 3, off)
        unicornhat.set_pixel(7, 3, off)
        unicornhat.set_pixel(3, 4, off)
        unicornhat.set_pixel(3, 5, off)
        unicornhat.set_pixel(3, 6, off)
        unicornhat.set_pixel(3, 7, off)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(4, 4, off)
        unicornhat.set_pixel(5, 4, off)
        unicornhat.set_pixel(6, 4, off)
        unicornhat.set_pixel(7, 4, off)
        unicornhat.set_pixel(4, 5, off)
        unicornhat.set_pixel(4, 6, off)
        unicornhat.set_pixel(4, 7, off)
        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(5, 5, off)
        unicornhat.set_pixel(6, 5, off)
        unicornhat.set_pixel(7, 5, off)
        unicornhat.set_pixel(5, 6, off)
        unicornhat.set_pixel(5, 7, off)

        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(6, 6, off)
        unicornhat.set_pixel(7, 6, off)
        unicornhat.set_pixel(6, 7, off)

        unicornhat.show()
        sleep(sleep_speed)

        unicornhat.set_pixel(7, 7, off)
        unicornhat.show()
        sleep(sleep_speed)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        corner_to_corner_4()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
