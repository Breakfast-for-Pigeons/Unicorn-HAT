#!/usr/bin/python3
"""
Pibow Candy Rainbow

This program displays the pastel colors of the Pimoroni Pibow Candy
case.

....................

Functions:
- pibow_candy_rainbow: Lights up the LEDs in the pastel colors of the
  Pimoroni Pibow Candy case
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
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

    try:
        while True:
            pibow_candy_rainbow()
    except KeyboardInterrupt:
        stop()


def pibow_candy_rainbow():
    """
    Lights up the LEDs in the pastel colors of the Pimoroni
    Pibow Candy case
    """

    rainbow0 = [
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W],
        [R, O, Y, G, B, I, V, W]
        ]

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

    unicornhat.set_pixels(rainbow0)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow1)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow2)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow3)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow4)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow5)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow6)
    unicornhat.show()
    sleep(0.5)
    unicornhat.set_pixels(rainbow7)
    unicornhat.show()
    sleep(0.5)


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
