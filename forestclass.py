
import turtle
import random
pen=turtle.Turtle()
pen.speed(0)
def shape(x,y,siz,color='green'): #drawing the shape of the star
        pen.up()
        pen.goto(x,y)
        pen.down()
        pen.color(color)
        pen.begin_fill()
        for i in range(5):
 
        # moving turtle 100 units forward
         pen.forward(siz) 
 
        # rotating turtle 144 degree right
         pen.right(144)
    
        pen.end_fill()

def star(s): #getting random elements to call the function
    t1=random.randrange(0,3)
    rang=ls[t1]
    
    x1=random.randrange(-400,300)
    y1=random.randrange(-250,250)
    shape(x1,y1,s,rang)
def draw_moon():
    pen.up()
    pen.goto(0,-200)
    pen.color('skyblue')
    pen.begin_fill()
    pen.circle(200)
    pen.end_fill()
def sky():
    turtle.bgcolor('darkblue')
    draw_moon()
    num1=random.randrange(20,40)
    color1=f"#{255:02x}{255:02x}00"
    color2=f"#{237:02x}{210:02x}{27:02x}"
    color3=f"#{247:02x}{166:02x}{17:02x}"
    color4=f"#{217:02x}{232:02x}{32:02x}"
    ls.extend([color1,color2,color3,color4]) #choosing a random color outta 4
    print(ls)
    for i in range(num1):
     size=random.randrange(30,150)
     size_list.append(size)
     newSizeList= sorted(size_list,reverse=True)
     print(newSizeList)
    for s in newSizeList:
         star(s)
size_list=[]
ls=[]
sky()
turtle.mainloop()