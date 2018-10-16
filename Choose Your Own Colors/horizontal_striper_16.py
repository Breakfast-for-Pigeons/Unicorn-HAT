#!/usr/bin/python3
"""
Horizontal Striper 16 - Choose Your Own Colors

With the Raspberry Pi oriented with the GPIO pins at the top, this
program stripes from the bottom to the top and alternates from left to
right and right to left.

This is exactly the same as Horizontal Striper 8 except the color order
is reversed.

....................

Functions:
- horizontal_striper_16: Gets x and y coordinates and sends them to the
      striping function

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornhat import print_header
from bfp_unicornhat import stop
from bfp_unicornhat import stripe_horizontally_rev_alt_2

########################################################################
#                         Import variables                             #
########################################################################

from bfp_unicornhat import X_COORDINATES
from bfp_unicornhat import Y_COORDINATES

########################################################################
#                            Functions                                 #
########################################################################


def horizontal_striper_16():
    """
    Sends x and y coordinates to the striper function
    """

    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES

    stripe_horizontally_rev_alt_2(x_coordinate_list, y_coordinate_list)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        horizontal_striper_16()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()