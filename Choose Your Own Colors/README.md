These are the programs that I wrote for the Pimoroni UnicornHAT, but you get to choose your own colors.

1) Use a webite like https://rgbcolorcode.com to get RGB color codes.

2) Open the bfp_unicornhat.py file and scroll down to the following section:

```python
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

```

By default, the colors are the colors of the rainboow, but you can insert your own color codes. Each number in the tuple
represents red, green, and blue respectively. For example:

(255, 0, 0) is the RGB tuple for the color red. 255 reprents red , 0 represents green, 0 represents blue.

You can insert your own red, green, and blue color tuples. Then on the right-hand side, you can make a note of which color you
chose. For example, if you want Color 1 to be "Air Force Blue", change the line to read

```python
C1 = (93, 138, 168)         # Color 1: Air Force blue
```

Then change the C1H line to read

```python
C1H = (46, 69, 84)        # Half the values of Color 1
```

Once you have all the colors you want (even duplicate colors - you don't have to have 8 different colors) save the file and
then run one of the programs.
