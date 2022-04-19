class Point(object):
    pass

class Rectangle(object):
    pass

r=Rectangle()

bl=Point()
bl.x=3.0
bl.y=5.0

tr=Point()
tr.x=5.0
tr.y=10.0

r.c1=bl
r.c2=tr

dx=5.0
dy=12.0

def move_rectangle(Rectangle, dx, dy):
    print(f"New bottom left {Rectangle.c1.x} {Rectangle.c1.y}")
    print(f"New top right {Rectangle.c2.x} {Rectangle.c2.y}")
    Rectangle.c1.x=Rectangle.c1.x+dx
    Rectangle.c2.x=Rectangle.c2.x+dx
    Rectangle.c1.y=Rectangle.c1.y+dy
    Rectangle.c2.y=Rectangle.c2.y+dy
    print(f"New bottom left {Rectangle.c1.x} {Rectangle.c1.y}")
    print(f"New top right {Rectangle.c2.x} {Rectangle.c2.y}")

move_rectangle(r, dx, dy)
