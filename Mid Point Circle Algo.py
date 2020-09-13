# Input for Coordinates and Radius
print("Enter the two Coordinates:")
x = int(input("Value for X:\t"))
y = int(input("Value for Y:\t"))
r = int(input("Value for Radius:\t"))

# Calculating values for Decision Parameter
x1 = x
y1 = r
pk = (5//4 - r)

# Printing the Decision Parameter and the Coordinates for generated line
while x1 < y1:
    if pk < 0:  # If Decision Parameter(pk) < 0
        x1 = x1 + 1
        print('\nDecision Parameter:\t', pk)
        print('Coordinates:\t({},{})'.format((x1+x), (y1+y)))
        pk = pk + (2 * x1) + 1
    else:  # If Decision Parameter(pk) > 0
        x1 = x1 + 1
        y1 = y1 - 1
        print('\nDecision Parameter:\t', pk)
        print('Coordinates:\t({},{})'.format((x1+x), (y1+y)))
        pk = pk + (2 * x1) + 1 - (2 * y1)
