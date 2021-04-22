# Demonstrate the usage of namedtuple objects

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")

    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1, p2)#Point(x=10, y=20) Point(x=30, y=40)
    print(p1.x, p1.y)# 10 20

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)#Point(x=100, y=20)


if __name__ == "__main__":
    main()