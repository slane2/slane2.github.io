import webbrowser, math

#address= "2600 NW College Way, Bend, OR, 97703"
#webbrowser.open('https://www.gooogle.com/maps/place/' + address);


class Rectangle:
    """ The point p1 represents lower left corner
        height is y axis
        width is x axis
    """
    def __init__(self, p1, height, width):
        self.LLcorner = p1
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
"""    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 +
                         (self.y - other.y)**2)
"""
rectOne = Rectangle(Point(0,0), 3,5)
print(Point(3,4))
"""
print(rectOne.area())
one = Point(1,1)
two = Point(4,5)
three = Point(2,3)
print(str(one))
print(str(two))
print(one == two)
print(one == three)
print(one.distance(two))
print("shayla")
"""
