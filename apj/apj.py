import turtle as tu

pen = tu.Turtle()
pen.speed(0)

x_offset = 550
y_offset = 270


def get_coord(data):                
    tu = []
    for i in data.readlines():
        i = (i.strip('\n')).strip('(').strip(')')
        tu.append(tuple(map(int,i.split(','))))

    return tu

def go(x,y):
    pen.penup()
    pen.goto(x-x_offset,(y*-1)+y_offset)
    pen.pendown()  


def paint(coord,co=(0,0,0)):
    pen.color(co)
    t_x,t_y = coord[0]
    go(t_x,t_y)
    pen.fillcolor(co)
    pen.begin_fill()
    t = 0
    for i in coord[1:]:
        print(i)
        x,y = i
        if t:
            go(x,y)
            t = 0
            pen.begin_fill()
            continue
        if x == -1 and y == -1:
            t = 1
            pen.end_fill()
            continue
        else:
            pen.goto(x-x_offset,(y*-1)+y_offset) 
    pen.end_fill()


def draw_fn(file,mode = 0,co = (0,0,0),thickness = 1):
    co = (co[0]/255,co[1]/255,co[2]/255)

    pen.color(co)

    data = open(f'{file}.txt','r')
    coord = get_coord(data)

    if mode:
        pen.width(thickness)
        t_x,t_y = coord[0]
        go(t_x,t_y)
        t = 0
        for i in coord[1:]:
            print(i)
            x,y = i
            if t:
                go(x,y)
                t = 0
                continue
            if x == -1 and y == -1:
                t = 1
                continue
            else:
                pen.goto(x-x_offset,(y*-1)+y_offset)
    else:
        paint(coord=coord,co = co)


draw_fn('i_l_b',mode = 0, co = (0,0,0))
draw_fn('i_l_t')
draw_fn('i_r_t')
draw_fn('i_r_b')
draw_fn('bottom')
draw_fn('l_f')
draw_fn('mouth')
draw_fn('teeth',co=(255,255,255),thickness=1)
draw_fn('r_eye')
draw_fn('r_eye_w1',co = (255,255,255))
draw_fn('r_eye_w2',co = (255,255,255))
draw_fn('l_eye')
draw_fn('eye_dots',mode = 1,thickness = 2,co = (255,255,255))
draw_fn('s1')
draw_fn('l1',thickness=2,mode=1)

tu.done()












