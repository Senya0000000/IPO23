import math
def area_of_quadrilateral(a, b, c, d, diagonal):
    s = (a + b + c + d) / 2
    area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - (a * c + b * d - diagonal**2) / 4)
    return area