#!/usr/bin/python3
"""
bfp_unicornhat - Choose Your Own Colors

This is a module containing the support functions and variables for my
UnicornPHAT programs. Each program imports only the needed functions and
variables.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import time
import random
import unicornhat

########################################################################
#                      Initialize UnicornPHAT                          #
########################################################################

unicornhat.set_layout(unicornhat.HAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

########################################################################
#                      CHOOSE YOUR OWN COLORS                          #
########################################################################
#   Feel free to modify the Red, Green, and Blue color tuples below.   #
#   Then make a note on the right side with that color.                #
#   Modify ONLY the section directly below.                            #
########################################################################

C1 = (255, 0, 0)         # Color 1: Red
C2 = (255, 128, 0)       # Color 2: Orange
C3 = (255, 255, 0)       # Color 3: Yellow
C4 = (0, 255, 0)         # Color 4: Green
C5 = (0, 0, 255)         # Color 5: Blue
C6 = (0, 204, 204)       # Color 6: Indigo
C7 = (127, 0, 255)       # Color 7: Violet
C8 = (255, 255, 255)     # Color 8: White
C1H = (128, 0, 0)        # Half the values of Color 1
C2H = (128, 64, 0)       # Half the values of Color 2
C3H = (128, 128, 0)      # Half the values of Color 3
C4H = (0, 128, 0)        # Half the values of Color 4
C5H = (0, 0, 128)        # Half the values of Color 5
C6H = (0, 102, 102)      # Half the values of Color 6
C7H = (64, 0, 128)       # Half the values of Color 7
C8H = (128, 128, 128)    # Half the values of Color 8

########################################################################
#                           Variables                                  #
########################################################################

HEADER_COLORS = ['\033[1;31;40m', '\033[1;32;40m', '\033[1;33;40m',
                 '\033[1;34;40m', '\033[1;35;40m', '\033[1;36;40m',
                 '\033[1;37;40m']

OFF = (0, 0, 0)

Y_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]
X_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

Y0_COLOR_TUPLE = C1      # Color 1
Y1_COLOR_TUPLE = C2      # Color 2
Y2_COLOR_TUPLE = C3      # Color 3
Y3_COLOR_TUPLE = C4      # Color 4
Y4_COLOR_TUPLE = C5      # Color 5
Y5_COLOR_TUPLE = C6      # Color 6
Y6_COLOR_TUPLE = C7      # Color 7
Y7_COLOR_TUPLE = C8      # Color 8

# Red, Orange, Yellow, White respectively
COLOR_LIST = [C1, C2, C3, C4, C5, C6, C7, C8]

X0_COLOR_TUPLE = C1      # Color 1
X1_COLOR_TUPLE = C2      # Color 2
X2_COLOR_TUPLE = C3      # Color 3
X3_COLOR_TUPLE = C4      # Color 4
X4_COLOR_TUPLE = C5      # Color 5
X5_COLOR_TUPLE = C6      # Color 6
X6_COLOR_TUPLE = C7      # Color 7
X7_COLOR_TUPLE = C8      # Color 8

########################################################################
#                            Functions                                 #
########################################################################


def print_header():
    """
    Prints the UnicornPHAT Header

    Arguments:
       color: the header will be printed in this color
    """

    color = random.choice(HEADER_COLORS)

    print(color)
    print(r"""
  _   _       _                        _   _    _  _____
 | | | |_ __ (_) ___ ___  _ __ _ __   | | | |  / \|_   _|
 | | | | '_ \| |/ __/ _ \| '__| '_ \  | |_| | / _ \ | |
 | |_| | | | | | (_| (_) | |  | | | | |  _  |/ ___ \| |
  \___/|_| |_|_|\___\___/|_|  |_| |_| |_| |_/_/   \_\_|


    """)


def stop():
    """
    Print exit message and turn off the UnicornPHAT
    """

    print("\nExiting program.")
    unicornhat.off()


def get_horizontal_rainbow_00():
    """
    Returns the main horizontal rainbow

    Programs that use this function:
        - Diagonal Ripple 1
        - Diagonal Ripple 2
        - Diagonal Ripple 3
        - Diagonal Ripple 4
        - Double Ripple 1
        - Double Ripple 2
        - Double Ripple 3
        - Double Ripple 4
        - Horizontal Ripple 1
        - Horizontal Ripple 2
        - Moving Horizontal Rainbow 1
        - Moving Horizontal Rainbow 2
    """

    rainbow00 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    return rainbow00


def get_diagonal_ripple_rainbows_1():
    """
    Returns 15 diagonal ripple rainbows.

    Programs that use this function:
        - Diagonal Ripple 1
        - Diagonal Ripple 2
        - Diagonal Ripple 3
        - Diagonal Ripple 4
    """

    rainbow01 = [
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow02 = [
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow03 = [
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow04 = [
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow05 = [
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow06 = [
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow07 = [
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow08 = [
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow09 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8]
    ]

    rainbow10 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8]
    ]

    rainbow11 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8]
    ]

    rainbow12 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8]
    ]

    rainbow13 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8]
    ]

    rainbow14 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8]
    ]

    rainbow15 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, \
        rainbow11, rainbow12, rainbow13, rainbow14, rainbow15


def get_diagonal_ripple_rainbows_2():
    """
    Returns 11 diagonal ripple rainbows

    Programs that use this function:
        - Diagonal Ripple 3
        - Diagonal Ripple 4
    """

    rainbow01 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow02 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8]
    ]

    rainbow03 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8]
    ]

    rainbow04 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8]
    ]

    rainbow05 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8]
    ]

    rainbow06 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8]
    ]

    rainbow07 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8]
    ]

    rainbow08 = [
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H]
    ]

    rainbow09 = [
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow10 = [
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow11 = [
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow12 = [
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow13 = [
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow14 = [
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow15 = [
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, \
        rainbow11, rainbow12, rainbow13, rainbow14, rainbow15


def get_double_ripple_rainbows_1():
    """
    Returns 8 rainbows

    Programs that use this function:
        - Double Ripple 1
        - Double Ripple 2
    """

    rainbow01 = [
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H]
    ]

    rainbow02 = [
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8]
    ]

    rainbow03 = [
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8]
    ]

    rainbow04 = [
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8]
    ]

    rainbow05 = [
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8]
    ]

    rainbow06 = [
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8]
    ]

    rainbow07 = [
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2H, C3, C4, C5, C6, C7, C8]
    ]

    rainbow08 = [
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08


def get_double_ripple_rainbows_2():
    """
    Returns 8 rainbows

    Programs that use this function:
        - Double Ripple 3
        - Double Ripple 4
    """

    rainbow01 = [
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow02 = [
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8]
    ]

    rainbow03 = [
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8]
    ]

    rainbow04 = [
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8]
    ]

    rainbow05 = [
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8]
    ]

    rainbow06 = [
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8]
    ]

    rainbow07 = [
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H],
        [C1, C2, C3, C4, C5, C6, C7H, C8]
    ]

    rainbow08 = [
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1H, C2H, C3H, C4H, C5H, C6H, C7H, C8H]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08


def get_horizontal_ripple_rainbows():
    """
    Returns 8 rainbows

    Programs that use this function:
        - Horizontal Ripple 1
        - Horizontal Ripple 2
    """

    rainbow01 = [
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8],
        [C1H, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow02 = [
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8],
        [C1, C2H, C3, C4, C5, C6, C7, C8]
    ]

    rainbow03 = [
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8],
        [C1, C2, C3H, C4, C5, C6, C7, C8]
    ]

    rainbow04 = [
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8],
        [C1, C2, C3, C4H, C5, C6, C7, C8]
    ]

    rainbow05 = [
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8],
        [C1, C2, C3, C4, C5H, C6, C7, C8]
    ]

    rainbow06 = [
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8],
        [C1, C2, C3, C4, C5, C6H, C7, C8]
    ]

    rainbow07 = [
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8],
        [C1, C2, C3, C4, C5, C6, C7H, C8]
    ]

    rainbow08 = [
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H],
        [C1, C2, C3, C4, C5, C6, C7, C8H]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08


def get_diagonal_rainbows_1():
    """
    Returns 8 different versions of diagonal rainbows

    Programs that use this function:
        - Moving Diagonal Rainbow 1
        - Moving Diagonal Rainbow 2
    """

    rainbow00 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7]
    ]

    rainbow01 = [
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6]
    ]

    rainbow02 = [
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5]
    ]

    rainbow03 = [
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4]
    ]

    rainbow04 = [
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3]
    ]

    rainbow05 = [
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2]
    ]

    rainbow06 = [
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1]
    ]

    rainbow07 = [
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8]
    ]

    rainbow08 = [
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7]
    ]

    rainbow09 = [
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6]
    ]

    rainbow10 = [
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5]
    ]

    rainbow11 = [
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4]
    ]

    rainbow12 = [
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3]
    ]

    rainbow13 = [
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C3, C4, C5, C6, C7, C8, C1, C2]
    ]

    rainbow14 = [
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C1, C2, C3, C4, C5, C6, C7, C8],
        [C2, C3, C4, C5, C6, C7, C8, C1]
    ]

    return rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, \
           rainbow05, rainbow06, rainbow07, rainbow08, rainbow09, \
           rainbow10, rainbow11, rainbow12, rainbow13, rainbow14


def get_diagonal_rainbows_2():
    """
    Returns 8 different versions of diagonal rainbows

    Programs that use this function:
        - Moving Diagonal Rainbow 3
        - Moving Diagonal Rainbow 4
    """

    rainbow00 = [
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8]
    ]

    rainbow01 = [
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7]
    ]

    rainbow02 = [
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6]
    ]

    rainbow03 = [
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5]
    ]

    rainbow04 = [
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4]
    ]

    rainbow05 = [
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3]

    ]

    rainbow06 = [
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2]

    ]

    rainbow07 = [
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1]
    ]

    rainbow08 = [
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8]

    ]

    rainbow09 = [
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7]

    ]

    rainbow10 = [
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6]

    ]

    rainbow11 = [
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5]

    ]

    rainbow12 = [
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4]
    ]

    rainbow13 = [
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2],
        [C2, C1, C8, C7, C6, C5, C4, C3]
    ]

    rainbow14 = [
        [C2, C1, C8, C7, C6, C5, C4, C3],
        [C3, C2, C1, C8, C7, C6, C5, C4],
        [C4, C3, C2, C1, C8, C7, C6, C5],
        [C5, C4, C3, C2, C1, C8, C7, C6],
        [C6, C5, C4, C3, C2, C1, C8, C7],
        [C7, C6, C5, C4, C3, C2, C1, C8],
        [C8, C7, C6, C5, C4, C3, C2, C1],
        [C1, C8, C7, C6, C5, C4, C3, C2]
    ]

    return rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, \
           rainbow05, rainbow06, rainbow07, rainbow08, rainbow09, \
           rainbow10, rainbow11, rainbow12, rainbow13, rainbow14


def get_horizontal_rainbows():
    """
    Returns 7 different versions of horizontal rainbows

    Programs that use this function:
        - Moving Horizontal Rainbow 1
        - Moving Horizontal Rainbow 2
    """

    rainbow01 = [
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1],
        [C2, C3, C4, C5, C6, C7, C8, C1]
    ]

    rainbow02 = [
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2],
        [C3, C4, C5, C6, C7, C8, C1, C2]
    ]

    rainbow03 = [
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3],
        [C4, C5, C6, C7, C8, C1, C2, C3]
    ]

    rainbow04 = [
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4],
        [C5, C6, C7, C8, C1, C2, C3, C4]
    ]

    rainbow05 = [
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5],
        [C6, C7, C8, C1, C2, C3, C4, C5]
    ]

    rainbow06 = [
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6],
        [C7, C8, C1, C2, C3, C4, C5, C6]
    ]

    rainbow07 = [
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7],
        [C8, C1, C2, C3, C4, C5, C6, C7]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07


def get_vertical_rainbow_00():
    """
    Returns the main vertical rainbow

    Programs that use this function:
        - Moving Vertical Rainbow 1
        - Moving Vertical Rainbow 2
        - Vertical Ripple 1
        - Vertical Ripple 1
    """

    rainbow00 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    return rainbow00


def get_vertical_rainbows():
    """
    Returns 7 different versions of vertical rainbows

    Programs that use this function:
        - Moving Vertical Rainbow 1
        - Moving Vertical Rainbow 2
    """

    rainbow01 = [
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8]
    ]

    rainbow02 = [
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7]
    ]

    rainbow03 = [
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6]
    ]

    rainbow04 = [
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5]
    ]

    rainbow05 = [
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4]
    ]

    rainbow06 = [
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3]
    ]

    rainbow07 = [
        [C1, C1, C1, C1, C1, C1, C1, C1],
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07


def get_vertical_ripple_rainbows():
    """
    Returns 8 vertical rainbows


    Programs that use this function:
        - Vertical Ripple 1
        - Vertical Ripple 2
    """

    rainbow01 = [
        [C8H, C8H, C8H, C8H, C8H, C8H, C8H, C8H],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow02 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7H, C7H, C7H, C7H, C7H, C7H, C7H, C7H],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow03 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6H, C6H, C6H, C6H, C6H, C6H, C6H, C6H],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow04 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5H, C5H, C5H, C5H, C5H, C5H, C5H, C5H],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow05 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4H, C4H, C4H, C4H, C4H, C4H, C4H, C4H],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow06 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3H, C3H, C3H, C3H, C3H, C3H, C3H, C3H],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow07 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2H, C2H, C2H, C2H, C2H, C2H, C2H, C2H],
        [C1, C1, C1, C1, C1, C1, C1, C1]
    ]

    rainbow08 = [
        [C8, C8, C8, C8, C8, C8, C8, C8],
        [C7, C7, C7, C7, C7, C7, C7, C7],
        [C6, C6, C6, C6, C6, C6, C6, C6],
        [C5, C5, C5, C5, C5, C5, C5, C5],
        [C4, C4, C4, C4, C4, C4, C4, C4],
        [C3, C3, C3, C3, C3, C3, C3, C3],
        [C2, C2, C2, C2, C2, C2, C2, C2],
        [C1H, C1H, C1H, C1H, C1H, C1H, C1H, C1H]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, \
        rainbow05, rainbow06, rainbow07, rainbow08


def get_y_color(y_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Parameter:
        y_color_tuple: a tuple of red, green and blue values for y
            coordinates

    Programs that use this function:
        - Horizontal Striper 1 through 16, but get_y_color is called
          directly by the following functions
            - stripe_horizontally
            - stripe_horizontally_alternate
            - stripe_horizontally_alternate_2
            - stripe_horizontally_reverse
            - stripe_horizontally_reverse_alt
            - stripe_horizontally_rev_alt_2

    """

    return int(y_color_tuple[0]), int(y_color_tuple[1]), \
        int(y_color_tuple[2])


def get_x_color(x_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Parameter:
        x_color_tuple: a tuple of red, green and blue values for x
            coordinates

    Programs that use this function:
        - Vertical Striper 1 through 16, but get_x_color is called
          directly by the following functions.
            - stripe_vertically
            - stripe_vertically_alternate
            - stripe_vertically_alternate_2
            - stripe_vertically_reverse
            - stripe_vertically_reverse_alt
            - stripe_vertically_reverse_alt_2
    """

    return int(x_color_tuple[0]), int(x_color_tuple[1]), \
        int(x_color_tuple[2])


def ripple_diagonally(static_rainbow, rainbow_list):
    """
    Cycles through 12 rainbows to make them ripple diagonally

    Parameters:
        static_rainbow: a single horizontal rainbow
        rainbow_list: a list containing 11 rainbows that will ripple

    Programs that use this function:
       - Diagonal Ripple 1: passes in rainbow00 and diagonal_rainbows_1
       - Diagonal Ripple 2: passes in rainbow00 and diagonal_rainbows_2
       - Diagonal Ripple 3: passes in rainbow00 and diagonal_rainbows_3
       - Diagonal Ripple 4: passes in rainbow00 and diagonal_rainbows_4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main horizontal rainbow
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(static_rainbow)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def double_ripple(static_rainbow, rainbow_list):
    """
    Cycles through 9 rainbows to ripple them

    Parameters:
        static_rainbow: a single horizontal rainbow
        rainbow_list: a list containing 9 rainbows that will ripple

    Programs that use this function:
        - Double Ripple 1: passes in rainbow00 and dr_rainbows_1
        - Double Ripple 2: passes in rainbow00 and dr_rainbows_2
        - Double Ripple 3: passes in rainbow00 and dr_rainbows_3
        - Double Ripple 4: passes in rainbow00 and dr_rainbows_4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main horizontal rainbow
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(static_rainbow)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def ripple_horizontally(static_rainbow, rainbow_list):
    """
    Cycles through 9 rainbows to ripple them horizontally

    Parameters:
        static_rainbow: a single horizontal rainbow
        rainbow_list: a list containing 8 rainbows that will ripple

    Programs that use this function:
        - Horizontal Ripple 1: passes in rainbow00 and hr_rainbows_1
        - Horizontal Ripple 2: passes in rainbow00 and hr_rainbows_1
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main horizontal rainbow
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(static_rainbow)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def stripe_horizontally(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Horizontal Striper 1
        - Horizontal Striper 2
        - Horizontal Striper 3
        - Horizontal Striper 4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 4:
                red, green, blue = get_y_color(Y4_COLOR_TUPLE)
            if y_coordinate == 5:
                red, green, blue = get_y_color(Y5_COLOR_TUPLE)
            if y_coordinate == 6:
                red, green, blue = get_y_color(Y6_COLOR_TUPLE)
            if y_coordinate == 7:
                red, green, blue = get_y_color(Y7_COLOR_TUPLE)

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_alternate(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. It alternates from right to left and left to right.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Horizontal Striper 5
        - Horizontal Striper 6
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 4:
                red, green, blue = get_y_color(Y4_COLOR_TUPLE)
            if y_coordinate == 5:
                red, green, blue = get_y_color(Y5_COLOR_TUPLE)
            if y_coordinate == 6:
                red, green, blue = get_y_color(Y6_COLOR_TUPLE)
            if y_coordinate == 7:
                red, green, blue = get_y_color(Y7_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES
            else:
                x_coordinate_list = X_COORDINATES[::-1]

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_alternate_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. It alternates from left to right to right to left.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

     Programs that use this function:
        - Horizontal Striper 7
        - Horizontal Striper 8
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 4:
                red, green, blue = get_y_color(Y4_COLOR_TUPLE)
            if y_coordinate == 5:
                red, green, blue = get_y_color(Y5_COLOR_TUPLE)
            if y_coordinate == 6:
                red, green, blue = get_y_color(Y6_COLOR_TUPLE)
            if y_coordinate == 7:
                red, green, blue = get_y_color(Y7_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES[::-1]
            else:
                x_coordinate_list = X_COORDINATES

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_reverse(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Horizontal Striper 9
        - Horizontal Striper 10
        - Horizontal Striper 11
        - Horizontal Striper 12
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y7_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y6_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y5_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y4_COLOR_TUPLE)
            if y_coordinate == 4:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 5:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 6:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 7:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_reverse_alt(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Horizontal Striper 5 and 6.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Horizontal Striper 13
        - Horizontal Striper 14
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y7_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y6_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y5_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y4_COLOR_TUPLE)
            if y_coordinate == 4:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 5:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 6:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 7:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES
            else:
                x_coordinate_list = X_COORDINATES[::-1]

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_rev_alt_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Horizontal Striper 7 and 8.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Horizontal Striper 15
        - Horizontal Striper 16
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y7_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y6_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y5_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y4_COLOR_TUPLE)
            if y_coordinate == 4:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 5:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 6:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 7:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES[::-1]
            else:
                x_coordinate_list = X_COORDINATES

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def move_diagonally(rainbow_list):
    """
    Cycles through 4 rainbows to make them appear to move diagonally

    Parameters:
        rainbow_list: 4 different rainbow images

    Programs that use this function:
        - Moving Diagonal Rainbow 1: passes in md_rainbows_1
        - Moving Diagonal Rainbow 2: passes in md_rainbows_2
        - Moving Diagonal Rainbow 3: passes in md_rainbows_3
        - Moving Diagonal Rainbow 4: passes in md_rainbows_4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def move_horizontally(rainbow_list):
    """
    Cycles through 4 rainbows to make them appear to move horizontally

    Parameters:
        rainbow_list: a list containing 4 horizontal rainbows that will
        ripple

    Programs that use this function:
        - Moving Horizontal Rainbow 1: passes in mh_rainbows_1
        - Moving Horizontal Rainbow 2: passes in mh_rainbows_2
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def move_vertically(rainbow_list):
    """
    Cycles through 4 rainbows to make them appear to move vertically

    Programs that use this function:
        - Moving Vertical Rainbow 1: passes in mv_rainbows_1
        - Moving Vertical Rainbow 2: passes in mv_rainbows_2
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def get_random_color():
    """
    Extracts 3 individual integers from a tuple and returns them.

    The integers represent the red, green, and blue color values
    respectively. Index 0 is red, index 1 is green, index 2 is blue.

    Programs that use this function:
        - Sprinkles
    """

    color_tuple = random.choice(COLOR_LIST)

    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])


def light_up_random_led(red, green, blue):
    """
    Lights up a random LED

    Parameters:
        red, green, and blue: integers that represent the amount of
            red, green, and blue in an LED

     Programs that use this function:
        - Sprinkles
    """

    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(),
                         red, green, blue)


def random_x_coordinate():
    """
    Returns a random x coordinate

    Programs that use this function:
        - Sprinkles
    """

    return int(random.choice(X_COORDINATES))


def random_y_coordinate():
    """
    Returns a random y coordinate

    Programs that use this function:
        - Sprinkles
    """

    return int(random.choice(Y_COORDINATES))


def ripple_vertically(static_rainbow, rainbow_list):
    """
    Cycles through 5 rainbows to ripple them vertically

    Parameters:
        static_rainbow: a single vertical rainbow
        rainbow_list: a list containing 8 rainbows that will ripple

    Programs that use this function:
        - Vertical Ripple 1: passes in rainbow00 and vr_rainbows_1
        - Vertical Ripple 2: passes in rainbow00 and vr_rainbows_2
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main vertical rainbow
        unicornhat.set_pixels(static_rainbow)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def stripe_vertically(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Vertical Striper 1
        - Vertical Striper 2
        - Vertical Striper 3
        - Vertical Striper 4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)

            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_alternate(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Vertical Striper 5
        - Vertical Striper 6
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES
            else:
                y_coordinate_list = Y_COORDINATES[::-1]
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_alternate_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs in this function:
        - Vertical Striper 7
        - Vertical Striper 8
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES[::-1]
            else:
                y_coordinate_list = Y_COORDINATES
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_reverse(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Vertical Striper 9
        - Vertical Striper 10
        - Vertical Striper 11
        - Vertical Striper 12
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the y coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)

            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_reverse_alt(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Vertical Striper 13
        - Vertical Striper 14
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES
            else:
                y_coordinate_list = Y_COORDINATES[::-1]
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_reverse_alt_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Vertical Striper 7 and 8

    Parameters:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7


    Programs that use this function:
        - Vertical Striper 15
        - Vertical Striper 16
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES[::-1]
            else:
                y_coordinate_list = Y_COORDINATES
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)
