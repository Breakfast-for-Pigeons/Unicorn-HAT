#!/usr/bin/python3
"""
Pibow Candy Striper 1

This program lights up each column one at a time with the pastel colors
of the Pimoroni Pibow Candy case. It lights them up from left
(the side with the USB and ethernet ports) to right.

....................

Functions:
- pibow_candy_striper_1: Gets the x and y coordinates and the
  RGB integers for the x coordinates.
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

from time import sleep
import unicornhat
from print_unicornhat_header import print_unicornhat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.HAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

X_OR_Y_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

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

    try:
        while True:
            pibow_candy_striper_1()
    except KeyboardInterrupt:
        stop()


def pibow_candy_striper_1():
    """
    Gets the x and y coordinates and the RGB integers for the
    x coordinates.
    """

    unicornhat.clear()
    x_coordinate_list = X_OR_Y_COORDINATES
    y_coordinate_list = X_OR_Y_COORDINATES

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
        # Light up selected x_coordinate column
        for y_coordinate in y_coordinate_list:
            unicornhat.set_pixel(x_coordinate, y_coordinate,
                                 red, green, blue)
            unicornhat.show()
            sleep(0.05)
    sleep(1.0)


def get_color(x_coordinate_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Arguments:
        x_coordinate_color_tuple: a tuple of red, green, and blue
        integers

    Returns:
        3 integers representing red, green, and blue respectively
    """

    return int(x_coordinate_color_tuple[0]), \
           int(x_coordinate_color_tuple[1]), \
           int(x_coordinate_color_tuple[2])


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nEx_coordinateiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
