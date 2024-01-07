import turtle as ttl
import random as r
import time as t

def set_point(x,y):
    point = ttl.Turtle()
    point.shape('circle')
    point.shapesize(0.75)
    point.color(50,158,65)
    point.up()
    point.goto(x,y)
    return point
# 
def set_speed_point(x,y):
    speed_point = ttl.Turtle()
    speed_point.shape('circle')
    speed_point.shapesize(0.75)
    speed_point.color(11,84,180)
    speed_point.up()
    speed_point.goto(x,y)
    return speed_point
# 
def to_up():
    ttl.setheading(90)
# 
def to_down():
    ttl.setheading(270)
# 
def to_left():
    ttl.setheading(180)
# 
def to_right():
    ttl.setheading(0)
# 
def set_rand():
    return r.randint(-287,250)
# 
def check_axis(x,y,pX,pY):
    n = 21
    a = pX - (n // 2)
    b = pY - (n // 2)
    for i in range(n):
        for j in range(n):
            if(x == a+i and y == b+j):
                return 1
    return 0
#
def show_blue_point():
    blue_point = ttl.Turtle()
    blue_point.shape('circle')
    blue_point.shapesize(0.75)
    blue_point.color(11,84,180)
    blue_point.up()
    blue_point.goto(130,281)
    # 
    blue_text = ttl.Turtle()
    blue_text.up()
    blue_text.goto(142,270)
    blue_text.ht()
    blue_text.color(77,77,77)
    blue_text.write(' : speed', font=('arial',15,'bold'))
# 
# 
# 
counter = 16
# 
screen = ttl.Screen()
screen.setup(600,600)
screen.title("my title")
# 
ttl.colormode(255)
ttl.bgcolor( 189,189,189)
ttl.listen()
ttl.onkey(to_up,'Up')
ttl.onkey(to_down,'Down')
ttl.onkey(to_left,'Left')
ttl.onkey(to_right,'Right')
ttl.shape("turtle")
ttl.up()
# 
bulkhead = ttl.Turtle()
bulkhead.color(77,77,77)
bulkhead.speed(10)
bulkhead.up()
bulkhead.goto(-297,260)
bulkhead.down()
bulkhead.width(4)
for i in range(4):
    bulkhead.forward(590)
    bulkhead.right(90)
bulkhead.ht()
# 
c_score = ttl.Turtle()
c_score.up()
c_score.goto(-220,270)
c_score.ht()
c_score.color(77,77,77)
c_score.write('score : ' + str(counter), font=('arial',15,'bold'))
show_blue_point()
# 
pX = set_rand()
pY = set_rand()
point = set_point(pX,pY)
point_speed_x = set_rand()
point_speed_y = set_rand()
speed_point = set_speed_point(point_speed_x,point_speed_y)
while(1):
    ttl.fd(2)
    if(check_axis(int(ttl.xcor()), int(ttl.ycor()), point_speed_x, point_speed_y)):
        for i in range(50):
            if(ttl.xcor() > 285 or ttl.xcor() < -292 or ttl.ycor() > 250 or ttl.ycor() < -325):
                ttl.right(180)
                counter -= 16
                if(counter < 0):
                    break
                c_score.clear()
                c_score.write('score : ' + str(counter), font=('arial',15,'bold'))
            ttl.forward(30)
        point_speed_x = set_rand()
        point_speed_y = set_rand()
        speed_point.goto(point_speed_x, point_speed_y)
    if(check_axis(int(ttl.xcor()), int(ttl.ycor()), pX, pY)):
        pX = set_rand()
        pY = set_rand()
        point.goto(pX, pY)
        # 
        counter += 2
        c_score.clear()
        c_score.write('score : ' + str(counter), font=('arial',15,'bold'))
    if(ttl.xcor() > 285 or ttl.xcor() < -292 or ttl.ycor() > 250 or ttl.ycor() < -325):
        ttl.right(180)
        counter -= 6   # counter = counter - 6
        c_score.clear()
        c_score.write('score : ' + str(counter), font=('arial',15,'bold'))
    if(counter > 20):
        c_score.goto(-40,0)
        ttl.clearscreen()
        c_score.write('you win', font=('arial',15,'bold'))
        t.sleep(2)
        break
    if(counter < 0):
        c_score.goto(-40,0)
        ttl.clearscreen()
        c_score.write('you lose', font=('arial',15,'bold'))
        t.sleep(2)
        break