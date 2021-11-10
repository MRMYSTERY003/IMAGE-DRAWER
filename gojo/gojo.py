import turtle as tu

pen = tu.Turtle()
pen.speed(5)


def draw_fn(file):
    data = open(f'{file}.txt','r')
    f = 1
    for i in  data.readlines():
        print(i)
        i = (i.strip('\n')).strip('(').strip(')')
        x,y = tuple(map(int,i.split(',')))
        if f:
            pen.penup()
            pen.goto(x-300,(y*-1)+300)
            f = 0
            pen.pendown()
        else:
            pen.goto(x-300,(y*-1)+300)

draw_fn('mask')
draw_fn('hair')
draw_fn('face')
draw_fn('dress')
draw_fn('face_shades')
draw_fn('mouth')
draw_fn('dress_extra')
draw_fn('hair_shade')



tu.done()