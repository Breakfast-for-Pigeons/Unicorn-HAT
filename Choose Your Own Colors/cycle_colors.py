#!/usr/bin/python3
"""
Cycle Colors - Choose Your Own Colors

This program cyles through all the colors of the Pibow Zero 1.3
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


def cycle_colors():
    """ Cycle through all the colors one at a time. """

    colors = [C1, C2, C3, C4, C5, C6, C7, C8]

    for color in colors:
        unicornhat.set_all(color)
        unicornhat.show()
        sleep(1)


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
