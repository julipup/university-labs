# Assume that we specify two points in space by defining the x and y
# coordinate of each using x1, y1, x2, and y2 all which are float.
# Write an expression that computes...

# Reading values of two points from user
x1 = 2.5
y1 = 2.5

x2 = 4.5
y2 = 4.5


# 1) ...the distance between these points
print(f'Distance between these two points: { ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 }')

# 2) ...the slope of the line from the first point to the second
print(f'The slope of the line from the first point to the second: { (y2 - y1) / (x2 - x1) }')

# 3) ...whether both points lie on the same line from the origin
# https://stackoverflow.com/a/11908158
# I'll try to figure out how it works (or won't)
x0 = 0
y0 = 0

cross = ((x1 - x2) * (y2 - y0)) - ((y1 - y2) * (x2 - x0))
print(f'Do both point lie on the same line from the origin?: { cross == 0 }')

# 4) ...whether the first point is above the second
print(f'Is the first point above the second?: { y1 > y2 }')


# Helper function for 5th and 6th tasks
def point_quadrant(x, y):
    # 2  |  1
    # ---|---
    # 3  |  4
    if x > 0 and y > 0:
        return 1
    elif x > 0 > y:
        return 4
    elif x < 0 < y:
        return 2
    elif x < 0 and y < 0:
        return 3
    # or more reader-friendly approach
    # if x > 0:
    #     if y > 0:
    #         return 1
    #     else:
    #         return 4
    # else:
    #     if y > 0:
    #         return 2
    #     else:
    #         return 3


# 5) ...what quadrant the first point lies in (1st, 2nd, 3rd, or 4th)
print(f'Quadrant in which first point lies: {point_quadrant(x1, y1)} Quadrant')

# 6) ...whether the two points lie in the same quadrant
print(f'Do this two points lie in the same quadrant?: { point_quadrant(x1, y1) == point_quadrant(x2, y2) }')
