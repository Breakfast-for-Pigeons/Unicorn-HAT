#!/usr/bin/python3
"""
Pibow Candy Moving Diagonal Rainbow

This program moves the Pibow Candy rainbow diagonally.

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
########################################################################
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
B = (174, 198, 207)
I = (119, 158, 203)
V = (203, 153, 201)
W = (244, 154, 194)

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

    function_list = [diagonal_rainbow_1, diagonal_rainbow_2,
                     diagonal_rainbow_3, diagonal_rainbow_4]

    try:
        while True:
            random.choice(function_list)()
    except KeyboardInterrupt:
        stop()


def get_diaginal_rainbow_1_or_3():
    """
    Returns the 15 rainbows for either rainbow 1 or rainbow 3
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
    Returns the 15 rainbows for either rainbow 2 or rainbow 4
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


def move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14):
    """
    "Moves" the 15 rainbows for 15 seconds.

    Arguments:
        rainbow00 through rainbow14
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

def diagonal_rainbow_1():
    """
    Gets the 15 rainbows for rainbow 1 and sends them to the move
    function.
    """

    rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
    rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, rainbow11, \
    rainbow12, rainbow13, rainbow14 = get_diaginal_rainbow_1_or_3()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)

def diagonal_rainbow_2():
    """
    Gets the 15 rainbows for rainbow 2 and sends them to the move
    function.
    """

    rainbow00, rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
    rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, rainbow11, \
    rainbow12, rainbow13, rainbow14 = get_diaginal_rainbow_2_or_4()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)

def diagonal_rainbow_3():
    """
    Gets the 15 rainbows for rainbow 3 and sendd them to the move
    function.
    """

    rainbow14, rainbow13, rainbow12, rainbow11, rainbow10, rainbow09, \
    rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, rainbow03, \
    rainbow02, rainbow01, rainbow00 = get_diaginal_rainbow_1_or_3()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)

def diagonal_rainbow_4():
    """
    Gets the 15 rainbows for rainbow 4 and sendd them to the move
    function.
    """

    rainbow14, rainbow13, rainbow12, rainbow11, rainbow10, rainbow09, \
    rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, rainbow03, \
    rainbow02, rainbow01, rainbow00 = get_diaginal_rainbow_2_or_4()

    move_the_rainbow_diagonally(rainbow00, rainbow01, rainbow02, \
                                rainbow03, rainbow04, rainbow05, \
                                rainbow06, rainbow07, rainbow08, \
                                rainbow09, rainbow10, rainbow11, \
                                rainbow12, rainbow13, rainbow14)


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()

if __name__ == '__main__':
    main()
