#!/usr/bin/python3
"""
Corner to Corner 5 - Pibow Candy

Selects a color and then sends it to one of four functions.

Can move a square from the lower left corner to the upper right corner.
Can move a square from the upper right corner to the lower left corner.
Can move a square from the lower right corner to the upper left corner.
Can move a square from the upper left corner to the lower right corner.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from corner_to_corner_1_v2 import corner_to_corner_1_v2
from corner_to_corner_2_v2 import corner_to_corner_2_v2
from corner_to_corner_3_v2 import corner_to_corner_3_v2
from corner_to_corner_4_v2 import corner_to_corner_4_v2
from bfp_unicornhat import print_header
from bfp_unicornhat import stop

########################################################################
#                        Import Variables                              #
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


def corner_to_corner_5():
    """
    Moves a square from one corner to the opposite corner.
    """
    off = (0, 0, 0)

    corner_to_corner_4_v2(off)
    corner_to_corner_1_v2(R)
    corner_to_corner_3_v2(O)
    corner_to_corner_2_v2(Y)
    corner_to_corner_4_v2(G)
    corner_to_corner_1_v2(B)
    corner_to_corner_3_v2(I)
    corner_to_corner_2_v2(V)
    corner_to_corner_4_v2(W)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        corner_to_corner_5()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
