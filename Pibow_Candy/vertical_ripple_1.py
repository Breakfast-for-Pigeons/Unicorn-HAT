#!/usr/bin/python3
"""
Vertical Ripple 1 - Pibow Candy

Retrieves the rainbows and sends them to the ripple function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows ripple
from the bottom to the top.

....................

Functions:
- vertical_ripple_1: Gets 5 rainbows and sends them to the ripple
      vertically function

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornhat import print_header
from bfp_unicornhat import stop
from bfp_unicornhat import get_vertical_rainbow_00
from bfp_unicornhat import get_vertical_ripple_rainbows
from bfp_unicornhat import ripple_vertically

########################################################################
#                            Functions                                 #
########################################################################


def vertical_ripple_1():
    """
    Gets 5 rainbows and sends them as an argument to the ripple
    diagonally function
    """

    rainbow00 = get_vertical_rainbow_00()

    rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, rainbow06, \
        rainbow07, rainbow08 = get_vertical_ripple_rainbows()

    vr_rainbows_1 = [rainbow01, rainbow02, rainbow03, rainbow04,
                     rainbow05, rainbow06, rainbow07, rainbow08]

    ripple_vertically(rainbow00, vr_rainbows_1)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        vertical_ripple_1()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
