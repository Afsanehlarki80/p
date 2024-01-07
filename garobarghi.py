import turtle as ttl
import random
import time

def set_screen():
    screen = ttl.Screen()
    screen.setup(500,500)
    screen.title("جاروبرقی")
    return screen
# 
def set_bulkhead():
    bulkhead = ttl.Turtle()
    bulkhead.color(77,77,77)
    bulkhead.speed(10)
    bulkhead.up()
    bulkhead.goto(-200,200)
    bulkhead.down()
    bulkhead.width(4)
    for i in range(4):
        bulkhead.forward(400)
        bulkhead.right(90)
    #bulkhead.ht()
    return bulkhead
# 
def set_point(pX,pY):
    point = []
    for i in range(len(pX)):
        p = ttl.Turtle()
        p.speed(10)
        p.shape('circle')
        p.shapesize(0.75)
        R = random.randint(100,220)
        G = random.randint(100,220)
        B = random.randint(100,220)
        p.color(R,G,B)
        p.up()
        p.goto(pX[i],pY[i])
        point.append(p)
    return point
# 
def set_count_ball():
    count_ball = ttl.Turtle()
    
    count_ball.up()
    count_ball.goto(-160,210)
    count_ball.ht()
    count_ball.color(77,77,77)
    count_ball.write('count : ' + str(counter), font=('arial',15,'bold'))
    return count_ball
# 
def check_axis(x,y,pX,pY):
    for i in range(len(pX)):
        if(x == pX[i] and y == pY[i]):
            return i
    return -1
#
#
#
counter = 0
pX = []
pY = []
for i in range(-150,181,30):
    for j in range(-150,181,30):
        r = random.randint(1,10)
        if(r == 5):
            pX.append(i)
            pY.append(j)
#  
screen = set_screen()
# 
ttl.colormode(255)
ttl.bgcolor(189,189,189)
ttl.up()
ttl.shapesize(1.5)
ttl.goto(-180,180)
# 
bulkhead = set_bulkhead()
count_ball = set_count_ball()
point = set_point(pX,pY)
# 
while(1):
    ttl.fd(3)
    remove = check_axis(int(ttl.xcor()), int(ttl.ycor()), pX, pY)
    if(remove != -1):
        point[remove].color(189,189,189)
        point[remove].goto(150,223)
        # 
        counter += 1
        count_ball.clear()
        count_ball.write('count : ' + str(counter), font=('arial',15,'bold'))
    if(ttl.xcor() > 180):
        if(ttl.ycor() < -160):
            time.sleep(3)
            break
        ttl.right(90)
        ttl.forward(30)
        ttl.right(90)
    elif(ttl.xcor() < -180):
        ttl.left(90)
        ttl.forward(30)
        ttl.left(90)