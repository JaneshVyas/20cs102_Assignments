from pikepdf import Rectangle


class point(object):
    pass

class rectangle(object):
    pass

r=rectangle()

bl=point()
bl.x=2
bl.y=4

tr=point()
tr.x=3
tr.y=6

r.c1=bl
r.c2=tr

dx=14
dy=16

def move_rectangle(r,dx, dy):
    print(f"Bottom Left corner at {r.c1.x},{r.c1.y}")
    print(f"Topr Right corner at {r.tr.x}, {r.tr.y}")
    r.c1.x=r.c1.x+dx
    r.c2.x=r.c2.x+dx
    r.c1.y=r.c2.y+dx
    r.c2.y=r.c2.y+dy
    print(f"Bottom right at {r.c1.x},{r.c1.y}")
    print(f"Top left at {r.c2.x},{r.c2.y}")

move_rectangle(r, dx, dy)
