#!/usr/bin/python3
"""
Cycle Colors - Pibow Candy

This program cyles through all the colors of the Pibow Candy
case, one color at a time.

....................

Functions:
- cycle_colors: Cycle through all the colors one at a time.

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
#                         Import variables                             #
########################################################################

from bfp_unicornhat import R
from bfp_unicornhat import O
from bfp_unicornhat import Y
from bfp_unicornhat import G
from bfp_unicornhat import B
from bfp_unicornhat import I
from bfp_unicornhat import V
from bfp_unicornhat import W

########################################################################
#                            Functions                                 #
########################################################################


def cycle_colors():
    """ Cycle through all the colors one at a time. """

    colors = [R, O, Y, G, B, I, V, W]

    for color in colors:
        unicornhat.set_all(color)
        unicornhat.show()
        sleep(1.0)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        cycle_colors()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
