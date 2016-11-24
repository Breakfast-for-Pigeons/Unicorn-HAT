#!/usr/bin/python
################################################################
#                         Pibow Candy                          #
################################################################
# Description:                                                 #
# This is a modification of my Moving Rainbow program. I just  #
# changed the colors to pastels to match the Pibow Candy case. #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.HAT)
unicornhat.brightness(0.5)
# Comment out the following line to make it move in the opposiste direction.
unicornhat.rotation(180)

def get_color():
    return int(random.randint(1, 255))

R = (255, 105, 97)
O = (255, 179, 71)
Y = (253, 253, 150)
G = (119, 190, 119)
B = (119, 158, 203)
I = (150, 111, 214)
V = (203, 153, 201)
W = (244, 154, 194)
off = (0, 0, 0)

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
    [W, R, O, Y, G, B, I, V],
]


while True:
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
