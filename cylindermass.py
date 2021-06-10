'''
calculates mass of a cylinder given input of radius(r) and height (h)
works by first working out the volume in cubic centimetres, then volumec3 / 1000 to
work out volume in cubic decimetres, then prints a string of volumed3
rounded to 2 decimal places concatenated between two strings for context
'''

import math

def main():

    def weight(r, h):
        if r == 69 and h == 69:
            print ("lol mate you have put the sex number in there, dunno if you noticed you absolute joker")
        else:
            pi = math.pi
            volumec3 = pi * r**2 * h
            volumed3 = volumec3 / 1000
            print("The mass of the cylinder in Kg is: " + (str(round(volumed3, 2))) + "Kg")

    weight(10,69)

if __name__ == "__main__":
    main()