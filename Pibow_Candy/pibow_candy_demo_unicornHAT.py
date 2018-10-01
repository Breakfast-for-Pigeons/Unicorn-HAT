#!/usr/bin/python3
"""
Pibow Candy Demo

This program is a collection of all my Pibow Candy programs. It picks
one at random and runs it for 15 seconds.

....................

Functions:
- get_diaginal_rainbow_1_or_3: Get the 15 rainbows for Pibow Candy
  rainbows 1 or 3.
- get_color: Extracts 3 individual integers from a tuple and returns
  them.
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
#########################################################################
#                          Import modules                              #
########################################################################

import time
import random
import unicornhat
from print_unicornhat_header import print_unicornhat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.HAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

R = (255, 105, 97)
O = (255, 179, 71)
Y = (253, 253, 150)
G = (119, 190, 119)
B = (119, 158, 203)
I = (150, 111, 214)
V = (203, 153, 201)
W = (244, 154, 194)
R2 = (128, 53, 49)
O2 = (128, 90, 36)
Y2 = (127, 127, 75)
G2 = (60, 95, 60)
B2 = (60, 79, 102)
I2 = (75, 56, 107)
V2 = (102, 77, 101)
W2 = (122, 77, 97)

COLOR_LIST = [(255, 105, 97), (255, 179, 71), (253, 253, 150), \
              (119, 190, 119), (119, 158, 203), (150, 111, 214), \
              (203, 153, 201), (244, 154, 194)]

X_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]
Y_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

X0_COLOR_TUPLE = (255, 105, 97)
X1_COLOR_TUPLE = (255, 179, 71)
X2_COLOR_TUPLE = (253, 253, 150)
X3_COLOR_TUPLE = (119, 190, 119)
X4_COLOR_TUPLE = (119, 158, 203)
X5_COLOR_TUPLE = (150, 111, 214)
X6_COLOR_TUPLE = (203, 153, 201)
X7_COLOR_TUPLE = (244, 154, 194)

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    This is the main function
    """

    print_unicornhat_header()

    # Force white text after selecting random colored header
    print("\033[1;37;40mPress Ctrl-C to stop the program.")

    function_list = [pibow_candy_rainbow, pibow_candy_rainbow_2, \
                     pibow_candy_rainbow_4, pibow_candy_rainbow_5, \
                     pibow_candy_rainbow_6, pibow_candy_rainbow_7, \
                     pibow_candy_ripple_1, pibow_candy_ripple_2, \
                     pibow_candy_ripple_3, pibow_candy_ripple_4, \
                     pibow_candy_ripple_5, pibow_candy_ripple_6, \
                     pibow_candy_ripple_7, pibow_candy_ripple_8, \
                     pibow_candy_double_ripple_1, \
                     pibow_candy_double_ripple_2, \
                     pibow_candy_double_ripple_3, \
                     pibow_candy_double_ripple_4, \
                     pibow_candy_sprinkles, pibow_candy_striper_1, \
                     pibow_candy_striper_2, pibow_candy_striper_3, \
                     pibow_candy_striper_4, pibow_candy_striper_5, \
                     pibow_candy_striper_6, pibow_candy_striper_7, \
                     pibow_candy_striper_8, pibow_candy_striper_9]

    try:
        while True:
            random.choice(function_list)()
    except KeyboardInterrupt:
        stop()


def get_pibow_candy_horizontal_rainbow():
    """
    Returns a horzontal rainbow
    """

    rainbow = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
        ]

    return rainbow


def get_horizontal_rainbow():
    """
    Returns 7 horzontal rainbow
    """

    rainbow1 = [
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R],
        [O, Y, G, B, I, V, W, R]
        ]

    rainbow2 = [
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O],
        [Y, G, B, I, V, W, R, O]
        ]

    rainbow3 = [
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y],
        [G, B, I, V, W, R, O, Y]
        ]

    rainbow4 = [
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G],
        [B, I, V, W, R, O, Y, G]
        ]

    rainbow5 = [
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B],
        [I, V, W, R, O, Y, G, B]
        ]

    rainbow6 = [
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I],
        [V, W, R, O, Y, G, B, I]
        ]

    rainbow7 = [
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V],
        [W, R, O, Y, G, B, I, V]
        ]

    return rainbow1, rainbow2, rainbow3, rainbow4, rainbow5, rainbow6, \
           rainbow7


def get_pibow_candy_vertical_rainbow():
    """
    Returns a vertical rainbow
    """

    rainbow = [
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W]
        ]

    return rainbow


def get_vertical_rainbow():
    """
    Returns 7 vertical rainbow
    """

    rainbow1 = [
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R]
        ]

    rainbow2 = [
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O]
        ]

    rainbow3 = [
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y]
        ]

    rainbow4 = [
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G]
        ]

    rainbow5 = [
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B]
        ]

    rainbow6 = [
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I]
        ]

    rainbow7 = [
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [O, O, O, O, O, O, O, O],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [G, G, G, G, G, G, G, G],
        [B, B, B, B, B, B, B, B],
        [I, I, I, I, I, I, I, I],
        [V, V, V, V, V, V, V, V]
        ]

    return rainbow1, rainbow2, rainbow3, rainbow4, rainbow5, rainbow6, \
           rainbow7


def get_diaginal_rainbow_1_or_3():
    """
    Returns 15 rainbows
    """

    rainbow00 = [
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V]
    ]

    rainbow01 = [
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I]
    ]

    rainbow02 = [
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B]
    ]

    rainbow03 = [
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G]
    ]

    rainbow04 = [
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y]
    ]

    rainbow05 = [
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O]
    ]

    rainbow06 = [
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R]
    ]

    rainbow07 = [
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W]
    ]

    rainbow08 = [
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V]
    ]

    rainbow09 = [
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I]
    ]

    rainbow10 = [
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B]
    ]

    rainbow11 = [
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G]
    ]

    rainbow12 = [
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y]
    ]

    rainbow13 = [
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R],
        [Y, G, B, I, V, W, R, O]
    ]

    rainbow14 = [
        [Y, G, B, I, V, W, R, O],
        [G, B, I, V, W, R, O, Y],
        [B, I, V, W, R, O, Y, G],
        [I, V, W, R, O, Y, G, B],
        [V, W, R, O, Y, G, B, I],
        [W, R, O, Y, G, B, I, V],
        [R, O, Y, G, B, I, V, W],
        [O, Y, G, B, I, V, W, R]
    ]

    return rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, \
           rainbow05, rainbow06, rainbow07, rainbow08, rainbow09, \
           rainbow10, rainbow11, rainbow12, rainbow13, rainbow14


def get_diaginal_rainbow_2_or_4():
    """
    Returns 15 rainbows
    """

    rainbow00 = [
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W]
    ]

    rainbow01 = [
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V]
    ]

    rainbow02 = [
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I]
    ]

    rainbow03 = [
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B]
    ]

    rainbow04 = [
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G]
    ]

    rainbow05 = [
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y]

    ]

    rainbow06 = [
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O]

    ]

    rainbow07 = [
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R]
    ]

    rainbow08 = [
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W]

    ]

    rainbow09 = [
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V]

    ]

    rainbow10 = [
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I]

    ]

    rainbow11 = [
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B]

    ]

    rainbow12 = [
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G]
    ]

    rainbow13 = [
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O],
        [O, R, W, V, I, B, G, Y]
    ]

    rainbow14 = [
        [O, R, W, V, I, B, G, Y],
        [Y, O, R, W, V, I, B, G],
        [G, Y, O, R, W, V, I, B],
        [B, G, Y, O, R, W, V, I],
        [I, B, G, Y, O, R, W, V],
        [V, I, B, G, Y, O, R, W],
        [W, V, I, B, G, Y, O, R],
        [R, W, V, I, B, G, Y, O]
    ]

    return rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, \
           rainbow05, rainbow06, rainbow07, rainbow08, rainbow09, \
           rainbow10, rainbow11, rainbow12, rainbow13, rainbow14


def move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, \
                                  rainbow3, rainbow4, rainbow5, \
                                  rainbow6, rainbow7):
    """
    Cycles through 8 rainbows to move them horizontally
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow0)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow1)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow2)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow3)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow4)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow5)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow6)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow7)
        unicornhat.show()
        time.sleep(0.5)


def move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14):
    """
    Cycles through rainbows to move them diagonally
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow00)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow01)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow02)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow03)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow04)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow05)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow06)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow07)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow08)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow09)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow10)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow11)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow12)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow13)
        unicornhat.show()
        time.sleep(0.15)
        unicornhat.set_pixels(rainbow14)
        unicornhat.show()
        time.sleep(0.15)


def pibow_candy_rainbow():
    """
    Gets 8 rainbows and sends them to the move_the_rainbow_horizontally
    function
    """

    rainbow0 = get_pibow_candy_horizontal_rainbow()

    rainbow1, rainbow2, rainbow3, rainbow4, \
    rainbow5, rainbow6, rainbow7 = get_horizontal_rainbow()

    move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, \
                                  rainbow3, rainbow4, rainbow5, \
                                  rainbow6, rainbow7)


def pibow_candy_rainbow_2():
    """
    Gets 8 rainbows and sends them to the move_the_rainbow_horizontally
    function
    """

    rainbow0 = get_pibow_candy_horizontal_rainbow()

    rainbow7, rainbow6, rainbow5, rainbow4, rainbow3, \
    rainbow2, rainbow1 = get_horizontal_rainbow()

    move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, \
                                  rainbow3, rainbow4, rainbow5, \
                                  rainbow6, rainbow7)


def pibow_candy_rainbow_3():
    """
    Gets 8 rainbows and sends them to the move_the_rainbow_horizontally
    function
    """

    rainbow0 = get_pibow_candy_vertical_rainbow()

    rainbow1, rainbow2, rainbow3, rainbow4, \
    rainbow5, rainbow6, rainbow7 = get_vertical_rainbow()

    move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, \
                                  rainbow3, rainbow4, rainbow5, \
                                  rainbow6, rainbow7)


def pibow_candy_rainbow_4():
    """
    Gets 8 rainbows and sends them to the move_the_rainbow_horizontally
    function
    """

    rainbow0 = get_pibow_candy_vertical_rainbow()

    rainbow7, rainbow6, rainbow5, rainbow4, rainbow3, \
    rainbow2, rainbow1 = get_vertical_rainbow()

    move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, \
                                  rainbow3, rainbow4, rainbow5, \
                                  rainbow6, rainbow7)


def pibow_candy_rainbow_5():
    """
    Gets 15 rainbows and sends them to the move_the_rainbow_diagonally
    function
    """

    rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
    rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, rainbow11, \
    rainbow12, rainbow13, rainbow14 = get_diaginal_rainbow_1_or_3()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)


def pibow_candy_rainbow_6():
    """
    Gets 15 rainbows and sends them to the move_the_rainbow_diagonally
    function
    """

    rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
    rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, rainbow11, \
    rainbow12, rainbow13, rainbow14 = get_diaginal_rainbow_2_or_4()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)


def pibow_candy_rainbow_7():
    """
    Gets 15 rainbows and sends them to the move_the_rainbow_diagonally
    function
    """

    rainbow14, rainbow13, rainbow12, rainbow11, rainbow10, rainbow09, \
    rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, rainbow03, \
    rainbow02, rainbow01, rainbow00 = get_diaginal_rainbow_1_or_3()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)


def pibow_candy_rainbow_8():
    """
    Gets 15 rainbows and sends them to the move_the_rainbow_diagonally
    function
    """

    rainbow14, rainbow13, rainbow12, rainbow11, rainbow10, rainbow09, \
    rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, rainbow03, \
    rainbow02, rainbow01, rainbow00 = get_diaginal_rainbow_2_or_4()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)


def get_diagonal_ripple_rainbow_1_or_3():
    """
    Returns 15 ripple rainbows
    """

    ripple00 = [
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple01 = [
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple02 = [
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple03 = [
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple04 = [
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple05 = [
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple06 = [
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple07 = [
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W]
    ]

    ripple08 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W]
    ]

    ripple09 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y2, G, B, I, V, W]
    ]

    ripple10 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G2, B, I, V, W]
    ]

    ripple11 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B2, I, V, W]
    ]

    ripple12 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I2, V, W]
    ]

    ripple13 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V2, W]
    ]

    ripple14 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W2]
    ]

    return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, \
           ripple06, ripple07, ripple08, ripple09, ripple10, ripple11, \
           ripple12, ripple13, ripple14


def ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, \
                                  ripple02, ripple03, ripple04, \
                                  ripple05, ripple06, ripple07, \
                                  ripple08, ripple09, ripple10, \
                                  ripple11, ripple12, ripple13, \
                                  ripple14):
    """
    Ripples 15 ripple rainbows
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow)
        unicornhat.show()
        time.sleep(3.0)
        unicornhat.set_pixels(ripple00)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple01)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple02)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple03)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple04)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple05)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple06)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple07)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple08)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple09)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple10)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple11)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple12)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple13)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple14)
        unicornhat.show()
        time.sleep(0.05)


def get_diagonal_ripple_rainbow_2_or_4():
    """
    Returns 15 rainbows
    """

    ripple00 = [
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple01 = [
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple02 = [
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple03 = [
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple04 = [
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple05 = [
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple06 = [
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple07 = [
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V, W2]
    ]

    ripple08 = [
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I, V2, W]
    ]

    ripple09 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B, I2, V, W]
    ]

    ripple10 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G, B2, I, V, W]
    ]

    ripple11 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y, G2, B, I, V, W]
    ]

    ripple12 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W]
    ]

    ripple13 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W]
    ]

    ripple14 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W]
    ]

    return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, \
           ripple06, ripple07, ripple08, ripple09, ripple10, ripple11, \
           ripple12, ripple13, ripple14


def pibow_candy_ripple_1():
    """
    Gets 15 rainbows and sends them to the ripple_the_rainbow_diagonally
    function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, \
    ripple06, ripple07, ripple08, ripple09, ripple10, ripple11, \
    ripple12, ripple13, ripple14 = get_diagonal_ripple_rainbow_1_or_3()

    ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, \
                                  ripple02, ripple03, ripple04, \
                                  ripple05, ripple06, ripple07, \
                                  ripple08, ripple09, ripple10, \
                                  ripple11, ripple12, ripple13, \
                                  ripple14)


def pibow_candy_ripple_2():
    """
    Gets 15 rainbows and sends them to the ripple_the_rainbow_diagonally
    function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, \
    ripple06, ripple07, ripple08, ripple09, ripple10, ripple11, \
    ripple12, ripple13, ripple14 = get_diagonal_ripple_rainbow_2_or_4()

    ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, \
                                  ripple02, ripple03, ripple04, \
                                  ripple05, ripple06, ripple07, \
                                  ripple08, ripple09, ripple10, \
                                  ripple11, ripple12, ripple13, \
                                  ripple14)


def pibow_candy_ripple_3():
    """
    Gets 15 rainbows and sends them to the ripple_the_rainbow_diagonally
    function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple14, ripple13, ripple12, ripple11, ripple10, ripple09, \
    ripple08, ripple07, ripple06, ripple05, ripple04, ripple03, \
    ripple02, ripple01, ripple00 = get_diagonal_ripple_rainbow_1_or_3()

    ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, \
                                  ripple02, ripple03, ripple04, \
                                  ripple05, ripple06, ripple07, \
                                  ripple08, ripple09, ripple10, \
                                  ripple11, ripple12, ripple13, \
                                  ripple14)


def pibow_candy_ripple_4():
    """
    Gets 15 rainbows and sends them to the ripple_the_rainbow_diagonally
    function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple14, ripple13, ripple12, ripple11, ripple10, ripple09, \
    ripple08, ripple07, ripple06, ripple05, ripple04, ripple03, \
    ripple02, ripple01, ripple00 = get_diagonal_ripple_rainbow_2_or_4()

    ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, \
                                  ripple02, ripple03, ripple04, \
                                  ripple05, ripple06, ripple07, \
                                  ripple08, ripple09, ripple10, \
                                  ripple11, ripple12, ripple13, \
                                  ripple14)


def get_horizontal_ripple_rainbow():
    """
    Returns 8 rainbows
    """

    ripple00 = [
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W]
    ]

    ripple01 = [
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W]
    ]

    ripple02 = [
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W]
    ]

    ripple03 = [
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W]
    ]

    ripple04 = [
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W]
    ]

    ripple05 = [
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W]
    ]

    ripple06 = [
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W]
    ]

    ripple07 = [
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2]
    ]

    return ripple00, ripple01, ripple02, ripple03, \
           ripple04, ripple05, ripple06, ripple07


def get_vertical_ripple_rainbow():
    """
    Returns 8 rainbows
    """

    ripple00 = [
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple01 = [
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple02 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple03 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
    ]

    ripple04 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple05 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple06 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W]
    ]

    ripple07 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2]
    ]

    return ripple00, ripple01, ripple02, ripple03, \
           ripple04, ripple05, ripple06, ripple07


def ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07):
    """
    Takes 8 rainbows and ripples them
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow)
        unicornhat.show()
        time.sleep(3.0)
        unicornhat.set_pixels(ripple00)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple01)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple02)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple03)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple04)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple05)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple06)
        unicornhat.show()
        time.sleep(0.05)
        unicornhat.set_pixels(ripple07)
        unicornhat.show()
        time.sleep(0.05)


def pibow_candy_ripple_5():
    """
    Gets 15 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple00, ripple01, ripple02, ripple03, ripple04, \
    ripple05, ripple06, ripple07 = get_horizontal_ripple_rainbow()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def pibow_candy_ripple_6():
    """
    Gets 15 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple00, ripple01, ripple02, ripple03, ripple04, \
    ripple05, ripple06, ripple07 = get_vertical_ripple_rainbow()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def pibow_candy_ripple_7():
    """
    Gets 15 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple07, ripple06, ripple05, ripple04, ripple03, \
    ripple02, ripple01, ripple00 = get_horizontal_ripple_rainbow()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def pibow_candy_ripple_8():
    """
    Gets 15 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple07, ripple06, ripple05, ripple04, ripple03, \
    ripple02, ripple01, ripple00 = get_vertical_ripple_rainbow()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def get_double_ripple_rainbow_1_or_3():
    """
    Returns 8 rainbows
    """

    ripple00 = [
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W]
    ]

    ripple01 = [
        [R, O2, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W]
    ]

    ripple02 = [
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W]
    ]

    ripple03 = [
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W]
    ]

    ripple04 = [
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W]
    ]

    ripple05 = [
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W]
    ]

    ripple06 = [
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V2, W]
    ]

    ripple07 = [
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R2, O2, Y2, G2, B2, I2, V2, W2]
    ]

    return ripple00, ripple01, ripple02, ripple03, \
           ripple04, ripple05, ripple06, ripple07


def get_double_ripple_rainbow_2_or_4():
    """
    Returns 8 rainbows
    """

    ripple00 = [
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2],
        [R, O, Y, G, B, I, V, W2]
    ]

    ripple01 = [
        [R, O, Y, G, B, I, V2, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W],
        [R, O, Y, G, B, I, V2, W]
    ]

    ripple02 = [
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W],
        [R, O, Y, G, B, I2, V, W]
    ]

    ripple03 = [
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W],
        [R, O, Y, G, B2, I, V, W]
    ]

    ripple04 = [
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W],
        [R, O, Y, G2, B, I, V, W]
    ]

    ripple05 = [
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O, Y2, G, B, I, V, W],
        [R, O, Y2, G, B, I, V, W]
    ]

    ripple06 = [
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R, O2, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2],
        [R, O2, Y, G, B, I, V, W]
    ]

    ripple07 = [
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O, Y, G, B, I, V, W],
        [R2, O2, Y2, G2, B2, I2, V2, W2]
    ]

    return ripple00, ripple01, ripple02, ripple03, \
           ripple04, ripple05, ripple06, ripple07


def pibow_candy_double_ripple_1():
    """
    Gets 8 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple00, ripple01, ripple02, ripple03, ripple04, \
    ripple05, ripple06, ripple07 = get_double_ripple_rainbow_1_or_3()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def pibow_candy_double_ripple_2():
    """
    Gets 8 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple00, ripple01, ripple02, ripple03, ripple04, \
    ripple05, ripple06, ripple07 = get_double_ripple_rainbow_2_or_4()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def pibow_candy_double_ripple_3():
    """
    Gets 8 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple07, ripple06, ripple05, ripple04, ripple03, \
    ripple02, ripple01, ripple00 = get_double_ripple_rainbow_1_or_3()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def pibow_candy_double_ripple_4():
    """
    Gets 8 rainbows and sends them to the
    ripple_the_rainbow_horizontally function
    """
    rainbow = get_pibow_candy_horizontal_rainbow()

    ripple07, ripple06, ripple05, ripple04, ripple03, \
    ripple02, ripple01, ripple00 = get_double_ripple_rainbow_2_or_4()

    ripple_the_rainbow_horizontally(rainbow, ripple00, ripple01, \
                                     ripple02, ripple03, ripple04, \
                                     ripple05, ripple06, ripple07)


def random_x_coordinate():
    """
    Returns a random x coordinate
    """
    return int(random.choice(X_COORDINATES))


def random_y_coordinate():
    """
    Returns a random y coordinate
    """
    return int(random.choice(Y_COORDINATES))


def get_random_color():
    """
    Extracts 3 individual integers from a tuple and returns them.

    Arguments:
        x_coordinate_color_tuple: a tuple of red, green, and blue
        integers

    Returns:
        3 integers representing red, green, and blue respectively
    """
    color_tuple = random.choice(COLOR_LIST)
    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])


def light_up_random_led(red, green, blue):
    """
    Lights up a random LED

    Arguments:
        red, green, and blue: integers that represent the amount of
            red, green, and blue in an LED
        integers
    """
    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), \
                         red, green, blue)


def pibow_candy_sprinkles():
    """
    Lights up and turns off random LEDs
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        # Turn on a random LED
        red, green, blue = get_random_color()
        light_up_random_led(red, green, blue)
        #Turn off a random LED
        unicornhat.set_pixel(random_x_coordinate(), \
                             random_y_coordinate(), \
                             0, 0, 0)
        unicornhat.show()
        time.sleep(0.01)


def get_color(x_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Arguments:
        x__color_tuple: a tuple of red, green, and blue
        integers

    Returns:
        3 integers representing red, green, and blue respectively
    """
    return int(x_color_tuple[0]), \
           int(x_color_tuple[1]), \
           int(x_color_tuple[2])


def pibow_candy_striper_1():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES

    pibow_candy_striper(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_2():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES[::-1]

    pibow_candy_striper(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_3():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES

    pibow_candy_striper(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_4():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES[::-1]

    pibow_candy_striper(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_5():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES
    random.shuffle(x_coordinate_list)
    y_coordinate_list = Y_COORDINATES

    pibow_candy_striper_shuffle(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_6():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES
    random.shuffle(x_coordinate_list)
    y_coordinate_list = Y_COORDINATES[::-1]

    pibow_candy_striper_shuffle(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_7():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES[::-1]

    pibow_candy_striper_alternate(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_8():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES

    pibow_candy_striper_alternate(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_9():
    """
    Gets a list of x and y coordinates and sends the to the
    pibow_candy_striper function
    """
    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES

    pibow_candy_striper_shuffle_alternate(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7
    """
    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()
        for x_coordinate in x_coordinate_list:
            #Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_color(X7_COLOR_TUPLE)
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def pibow_candy_striper_shuffle(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. It shuffles the x coordinates.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7
    """
    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()
        random.shuffle(x_coordinate_list)
        for x_coordinate in x_coordinate_list:
            #Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_color(X7_COLOR_TUPLE)
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def pibow_candy_striper_alternate(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()
        for x_coordinate in x_coordinate_list:
            #Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_color(X7_COLOR_TUPLE)
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


def pibow_candy_striper_shuffle_alternate(x_coordinate_list, \
                                          y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:

        seconds_elapsed = time.time() - start_time
        unicornhat.clear()
        random.shuffle(x_coordinate_list)

        for x_coordinate in x_coordinate_list:
            #Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_color(X7_COLOR_TUPLE)

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


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
