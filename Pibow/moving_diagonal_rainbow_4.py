#!/usr/bin/python3
"""
Moving Diagonal Rainbow 4 - Pibow

Retrieves the rainbows and sends them to the move function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows move
from the bottom right the top left.

....................

Functions:
- moving_diagonal_rainbow_4: Retrieves the rainbows and sends them to
      the move function.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornhat import print_header
from bfp_unicornhat import stop
from bfp_unicornhat import get_diagonal_rainbows_2
from bfp_unicornhat import move_diagonally

########################################################################
#                            Functions                                 #
########################################################################


def moving_diagonal_rainbow_4():
    """
    Gets 4 rainbows, assigns them in reverse order, and sends them to
    the move_diagonally function
    """

    rainbow14, rainbow13, rainbow12, rainbow11, rainbow10, rainbow09, \
        rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, \
        rainbow03, rainbow02, rainbow01, \
        rainbow00 = get_diagonal_rainbows_2()

    md_rainbows_4 = [rainbow00, rainbow01, rainbow02, rainbow03,
                     rainbow04, rainbow05, rainbow06, rainbow07,
                     rainbow08, rainbow09, rainbow10, rainbow11,
                     rainbow12, rainbow13, rainbow14]

    move_diagonally(md_rainbows_4)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        moving_diagonal_rainbow_4()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
