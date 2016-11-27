#!/usr/bin/env python
################################################################
#                 Pibow Candy Rainbow 2                        #
################################################################
# Description:                                                 #
# It's like Pibow Canday Rainbow except that it moves in the   #
# other direction.                                             #
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
off = (0, 0, 0)

def pibow_candy_rainbow_2():

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
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V]
	]

	rainbow2 = [
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I]
	]

	rainbow3 = [
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B],
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B]
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
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y]
	]

	rainbow6 = [
		[Y, G, B, I, V, W, R, O],
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O],
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O]
	]

	rainbow7 = [
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R] 
	]

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

def main():
	while True:
		pibow_candy_rainbow_2()

if __name__ == '__main__':
	main()
