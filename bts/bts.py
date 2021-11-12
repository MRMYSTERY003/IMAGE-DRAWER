import turtle as tu

pen = tu.Turtle()
pen.speed(5)


def draw_fn(file,thickness = 1,co = (0.5,0.5,0.5)):
    pen.color(co)
    pen.width(thickness)
    data = open(f'{file}.txt','r')
    f = 1
    for i in data.readlines():
        print(i)
        i = (i.strip('\n')).strip('(').strip(')')
        x,y = tuple(map(int,i.split(',')))
        if f:
            pen.penup()
            pen.goto(x-300,(y*-1)+300)
            f= 0
            pen.pendown()
        else:
            pen.goto(x-300,(y*-1)+300)

draw_fn('face_cut')
draw_fn('l_eye')
draw_fn('l_eye_ball')
draw_fn('r_eye')
draw_fn('r_eye_ball')
draw_fn('dress')
draw_fn('nose')
draw_fn('mouth')
draw_fn('l_ear')
draw_fn('hair_out')
draw_fn('r_ear')
draw_fn('eye_brow')
draw_fn('dress_shade')


tu.done()