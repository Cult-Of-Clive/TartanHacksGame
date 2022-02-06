# A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
import math


# Get the area of a triangle from its vertices
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
# Code credit: https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/
def point_in_triangle(pt, triangle):
    # Break the triangle up into coordinates
    x1 = triangle[0][0]
    y1 = triangle[0][1]
    x2 = triangle[1][0]
    y2 = triangle[1][1]
    x3 = triangle[2][0]
    y3 = triangle[2][1]

    # Break the point up into coordinates
    x = pt[0]
    y = pt[1]

    # Calculate area of triangle ABC
    abc = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    pbc = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    pac = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    pab = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    return abc == pbc + pac + pab


# Gets the distance between two points
def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)
