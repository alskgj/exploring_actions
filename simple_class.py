class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def add_points(first, second):
    return Point(first.x + second.x, first.y + second.y)

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(3, 4)
    p3 = add_points(p1, p2)
    print(p3.x, p3.y)
