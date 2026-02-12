import math 

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

hasil = jarak (0, 0, 3, 4)
print("Jarak =", hasil)
