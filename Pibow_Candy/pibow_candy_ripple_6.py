#!/usr/bin/env python
################################################################
#                    Pibow Candy Ripple 6                      #
################################################################
# Description:                                                 #
# This program "ripples" the Pibow Candy rainbow.              #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

import unicornhat, signal, time, random

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
R2 = (128, 52, 48)
O2 = (128, 90, 35)
Y2 = (126, 126, 75)
G2 = (60, 95, 60)
B2 = (60, 80, 101)
I2 = (75, 55, 107)
V2 = (101, 76, 100)
W2 = (122, 77, 97)


def pibow_candy_ripple_6():

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
		[R, O, Y, G, B, I, V, W]
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

	while True:
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

def main():
	while True:
		pibow_candy_ripple_6()

if __name__ == '__main__':
    main()
