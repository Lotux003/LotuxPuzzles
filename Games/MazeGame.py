print("https://github.com/Lotux003/TurtleGraphics-Maze")
import turtle as trtl, random

wn = trtl.Screen()

GridTrtl = trtl.Turtle()
Runner = trtl.Turtle()
PathCreator = trtl.Turtle()
Solver = trtl.Turtle()

GridTrtl.pensize(2)
Runner.pensize(2)
PathCreator.pensize(2)
Solver.pensize(1)

GridTrtl.speed(0)
Runner.speed(0)
Solver.speed(0)
PathCreator.speed(0)

GridTrtl.color("black")
Runner.color("black")
Solver.color("red")
PathCreator.color("white")

PathCreator.hideturtle()
Runner.hideturtle()
GridTrtl.hideturtle()
Solver.hideturtle()

PathCreator.left(90)

size, _length = 20, 20
_width, _height = size, size
xpos, ypos = -(_width*10), 10*_height
start_xpos, start_ypos = -(_width*10), 10*_height

CurrentXPos = -(_width*10)
CurrentYPos = _width*10
CurrentCoords = (CurrentXPos, CurrentYPos)

endloopBool = True
onFinish = False
pathComplete = False

BeenTo = []
Options = []
NotOptions = []
Direction = []
Path = []
FinishPath = []

solverCoords = (0, 0)

def DrawGrid():
    global GridTrtl, Runner, PathCreator, Solver
    GridTrtl.penup()
    GridTrtl.goto(xpos, ypos)
    GridTrtl.pendown()
    GridSquare()

def GridSquare(turtle, wn):
    global Runner, PathCreator, Solver
    wn.tracer(0)
    newypos = ypos
    for i in range(_height - 1):
        for j in range(_width):
            for k in range(4):
                turtle.forward(_length)
                turtle.right(90)
            turtle.forward(_length)
            
        newypos -= _length
        turtle.penup()
        turtle.goto(xpos, newypos)
        turtle.pendown()
        
    for l in range(_width - 1):
        for m in range(4):
            turtle.forward(_length)
            turtle.right(90)
        turtle.forward(_length)
            
    turtle.forward(_length)
    turtle.right(90)
    turtle.forward(_length)
    turtle.right(90)
    turtle.color("white")
    turtle.forward(_length)
    turtle.right(90)
    turtle.color("black")
    turtle.forward(_length)
    turtle.right(90)
    turtle.hideturtle()
    turtle.bye()
    wn.tracer(1)
    wn.update()

Start(Runner, PathCreator, Solver, wn)

wn.mainloop()