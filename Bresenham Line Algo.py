# Input for Coordinates
print("Enter the two Coordinates:")
x1 = int(input("Value for X1:\t"))
y1 = int(input("Value for Y1:\t"))
x2 = int(input("Value for X2:\t"))
y2 = int(input("Value for Y2:\t"))

# Calculating values for delta X, delta Y, and Decision Parameter
dx = x2 - x1
dy = y2 - y1
x = x1
y = y1
pk = ((2 * dy) - dx)

# Printing the Decision Parameter and the Coordinates for generated line
while x < x2 - 1:
    if pk > 0:      # If Decision Parameter(pk) > 0
        x = x + 1
        y = y + 1
        print('\nDecision Parameter:\t', pk)
        print('Coordinates:\t({},{})'.format(x, y))
        pk = pk + (2 * dy) - (2 * dx)
    else:       # If Decision Parameter(pk) > 0
        x = x + 1
        print('\nDecision Parameter:\t', pk)
        print('Coordinates:\t({},{})'.format(x, y))
        pk = pk + (2 * dy)
