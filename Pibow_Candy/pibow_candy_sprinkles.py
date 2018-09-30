#!/usr/bin/python3
"""
Pibow Candy Sprinkles

This program lights up a random LED with a random pastel color. It
also turns off a randomly selected LED.

....................

Functions:
- pibow_candy_ripple_8: Ripples the Pibow Candy rainbow
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
import random
import unicornhat
from print_unicornhat_header import print_unicornhat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.HAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

X_OR_Y_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

COLOR_LIST = [
    (255, 105, 97), (255, 179, 71), (253, 253, 150), (119, 190, 119),
    (119, 158, 203), (150, 111, 214), (203, 153, 201), (244, 154, 194)
    ]

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
            pibow_candy_sprinkles()
    except KeyboardInterrupt:
        stop()


def pibow_candy_sprinkles():
    """
    Generates random sprinkles on the Pimoroni UnicornHAT
    """
    # STEP01: Get a random color
    red, green, blue = get_random_color()
    # STEP02: Turn on a random LED with the random color
    light_up_random_led(red, green, blue)
    # STEP03: Turn off a randomly selected LED
    unicornhat.set_pixel(random_x_or_y_coordinate(),
                         random_x_or_y_coordinate(), 0, 0, 0)
    unicornhat.show()
    sleep(0.01)


def get_random_color():
    """
    This function returns a random color tuple from a color list
    """
    color_tuple = random.choice(COLOR_LIST)
    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])


def light_up_random_led(red, green, blue):
    """
    Turn on a randomly selected LED

    Arguments:
        red - the amount of red in the LED
        green - the amount of green in the LED
        blue - the amount of blue in the LED
    """
    unicornhat.set_pixel(random_x_or_y_coordinate(),
                         random_x_or_y_coordinate(), red, green, blue)


def random_x_or_y_coordinate():
    """
    This function returns a random integer for an x or y coordinate.
    """

    return int(random.choice(X_OR_Y_COORDINATES))


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
