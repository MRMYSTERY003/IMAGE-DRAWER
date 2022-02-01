import turtle as tu

pen = tu.Turtle()
pen.speed(0)


def get_coord(data):                
    tu = []
    for i in data.readlines():
        print(i)
        i = (i.strip('\n')).strip('(').strip(')')
        tu.append(tuple(map(int,i.split(','))))

    return tu


def draw_fn(file,co = (0,0,0),thickness = 1):
    co = (co[0]/255,co[1]/255,co[1]/255)

    pen.color(co)
    pen.width(thickness)

    data = open(f'{file}.txt','r')
    coord = get_coord(data)

    pen.penup()
    t_x,t_y = coord[0]
    pen.goto(t_x-300,(t_y*-1)+300)
    pen.pendown()
    pen.fillcolor(co)
    pen.begin_fill()

    for i in coord[1:]:
        print(i)
        x,y = i
        pen.goto(x-300,(y*-1)+300)
    pen.end_fill()


draw_fn('neck',co = (247, 164, 130))
draw_fn('dress',co = (75, 91, 153))
draw_fn('hair',co = (0,0,0))
draw_fn('glass_frame',co = (56, 53, 48))
draw_fn('l_glass',co = (7, 96, 148))
draw_fn('r_glass',co = (7, 96, 148))
draw_fn('inner_beard',co = (241, 152, 112))
draw_fn('lips',co = (238, 104, 114))
draw_fn('teeth',co = (0,0,0))


tu.done()












