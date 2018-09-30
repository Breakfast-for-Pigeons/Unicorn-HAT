#!/usr/bin/python3
"""
Print UnicornHAT Header

This is the print_unicornhat_header module for my Pimoroni
UnicornHAT programs.

....................

Functions:

- print_unicornhat_header: Prints a header

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""


def print_unicornhat_header():
    """
    Prints a header


    This function will print out the program header in a randomly
    selected color.
    """

    import random

    color_list = ['\033[1;31;40m', '\033[1;32;40m', '\033[1;33;40m',
                  '\033[1;34;40m', '\033[1;35;40m', '\033[1;36;40m',
                  '\033[1;37;40m']

    color = random.choice(color_list)

    print(color)
    print(r"""

  _   _       _                        _   _    _  _____ 
 | | | |_ __ (_) ___ ___  _ __ _ __   | | | |  / \|_   _|
 | | | | '_ \| |/ __/ _ \| '__| '_ \  | |_| | / _ \ | |  
 | |_| | | | | | (_| (_) | |  | | | | |  _  |/ ___ \| |  
  \___/|_| |_|_|\___\___/|_|  |_| |_| |_| |_/_/   \_\_|  
                                                         

    """)


if __name__ == '__main__':
    print_unicornhat_header()
