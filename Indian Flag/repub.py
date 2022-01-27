import turtle as tu

pen = tu.Turtle()
pen.speed(5)

x_offset = 350
y_offset = 340




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
        #print(i)
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
            #print(i)
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

def run():
    draw_fn('uind',co = (0,0,255))
    draw_fn('lind',co = (0,0,255))
    draw_fn('frup',co = (255, 167, 31))
    draw_fn('frdo',co = (255, 167, 31))
    draw_fn('grdo',co = (1, 174, 59))
    draw_fn('rshade',co = (220, 79, 10))
    draw_fn('b_spokes',co = (0,0,255))
    draw_fn('spokes',co = (255,255,255))
    go(417, 452)
    pen.color((0//255,0//255,200//255))
    pen.write("Happy Republic Day", font=("Verdana",20, "normal"))
    pen.hideturtle()
    tu.done()


run()












