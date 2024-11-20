print("https://github.com/Lotux003/TurtleGraphics-Maze")
import turtle as trtl, random

wn = trtl.Screen()

GridTrtl, Runner, PathCreator, Solver = trtl.Turtle(), trtl.Turtle(), trtl.Turtle(), trtl.Turtle()

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
_width, _height, = size, size
xpos, ypos, start_xpos, start_ypos = -(_width*10), 10*_height, -(_width*10), 10*_height

CurrentXPos, CurrentYPos = -(_width*10), _width*10
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

def GridSquare():
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

def PracticeDict():
    global GridTrtl, Runner, PathCreator, Solver
    gridValueX = xpos
    gridValueY = ypos
    for k in range(_height):
        for l in range(_width): 
            gridValueX += _length
        gridValueX = xpos
        gridValueY -= _length

def CheckRoutes(CurrentX, CurrentY):
    global GridTrtl, Runner, PathCreator, Solver, onFinish, FinishPath, Path
    if CurrentX == _width*10-_length and CurrentY == -(_height*10)+_length and onFinish != True:
        onFinish = True
        FinishPath = Path.copy()
        LastCoords = Path[-1]
        LastX = LastCoords[0]
        LastY = LastCoords[1]
    else:
        UpCoords = (CurrentX, CurrentY + _length)
        DownCoords = (CurrentX, CurrentY - _length)
        RightCoords = (CurrentX + _length, CurrentY)
        LeftCoords = (CurrentX - _length, CurrentY)
        Options.clear()
        CheckPosInDict(UpCoords, 1, CurrentX, CurrentY)
        CheckPosInDict(DownCoords, 2, CurrentX, CurrentY)
        CheckPosInDict(RightCoords, 3, CurrentX, CurrentY)
        CheckPosInDict(LeftCoords, 4, CurrentX, CurrentY)
    
def CheckPosInDict(Coords, direction, CurrentX, CurrentY):
    global GridTrtl, Runner, PathCreator, Solver, CurrentCoords
    if (xpos <= Coords[0] < xpos + (_width * _length)) and \
       (ypos - (_height * _length) < Coords[1] <= ypos):
        if Coords not in BeenTo and Coords not in Options and Coords not in NotOptions:
            Options.append(Coords)
            Direction.append(direction) 
    elif Coords not in NotOptions:
        NotOptions.append(Coords)
    if CurrentCoords not in Options and CurrentCoords not in BeenTo:
        BeenTo.append(CurrentCoords)

def Move():
    global GridTrtl, Runner, PathCreator, Solver, endloopBool, CurrentCoords, _length, CurrentYPos, CurrentXPos
    Path.append((CurrentXPos, CurrentYPos))
    if Options:
        MoveVar = random.randint(0, len(Options) - 1)
        direction = Direction[MoveVar]
        NewCoords = Options[MoveVar]
        runner.goto(NewCoords)
        first_number = NewCoords[0]
        second_number = NewCoords[1]
        CurrentXPos = first_number
        CurrentYPos = second_number
        if direction == 1:
            pathCreator.penup()
            pathCreator.goto(CurrentXPos + 1, CurrentYPos - _length)
            pathCreator.pendown()
            pathCreator.right(90)
            pathCreator.forward(_length - 1)
            pathCreator.right(180)
            pathCreator.forward(_length - 1)
            pathCreator.right(90)
        elif direction == 2:
            pathCreator.penup()
            pathCreator.goto(CurrentXPos + 1, CurrentYPos)
            pathCreator.pendown()
            pathCreator.right(90)
            pathCreator.forward(_length - 1)
            pathCreator.right(180)
            pathCreator.forward(_length - 1)
            pathCreator.right(90)
        elif direction == 3:
            pathCreator.penup()
            pathCreator.goto(CurrentXPos, CurrentYPos - 1)
            pathCreator.pendown()  
            pathCreator.right(180)
            pathCreator.forward(_length - 1)
            pathCreator.right(180)
            pathCreator.forward(_length - 1)
        elif direction == 4:
            pathCreator.penup()
            pathCreator.goto(CurrentXPos + _length, CurrentYPos - 1)
            pathCreator.pendown()  
            pathCreator.right(180)
            pathCreator.forward(_length - 1)
            pathCreator.right(180)
            pathCreator.forward(_length - 1)
        Direction.clear()
        BeenTo.append(NewCoords)
        previous_position = (CurrentXPos, CurrentYPos)
        if previous_position not in NotOptions:
            NotOptions.append(previous_position)
        CheckRoutes(CurrentXPos, CurrentYPos)
    else:
        if len(Path) < 2:
            print("No options available to move.")
        else:
            while len(Options) == 0:
                if len(Path) != 1:
                    runner.goto(Path[-2])
                    Path2bak = Path[-2]
                    CurrentXPos = Path2bak[0]
                    CurrentYPos = Path2bak[1]
                    CheckRoutes(CurrentXPos, CurrentYPos)
                    if len(Options) == 0:
                        del Path[-1]
                    else:
                        Move(runner, pathCreator, solver, wn)
                else:
                    if endloopBool == True:
                        endloopBool = False
                        runner.pendown()
                        runner.color("white")
                        runner.forward(_length)
                        runner.hideturtle()
                        pathComplete = True
                        Complete()
                        
def Start():
    global GridTrtl, Runner, PathCreator, Solver
    runner.penup()
    runner.goto(start_xpos, start_ypos)    
    solver.penup()
    solver.goto(xpos + 10, ypos+_length)
    solver.pendown()
    
    for _i in range(500):
        PracticeDict()
        CheckRoutes(CurrentXPos, CurrentYPos)
        Move()
        Options.clear()
    
def Complete():
    global GridTrtl, Runner, PathCreator, Solver
    print("Complete!")
    print(f"Finish Path: {FinishPath}")
    AskToSolve()
    
def AskToSolve():
    global GridTrtl, Runner, PathCreator, Solver
    while True:
        _solve = input("Do you want me to solve it? (y/n) ")
        if _solve == "y":
            Solve()
            return False
        elif _solve == "n":
            print("Okay... ")
            return False
        else:
            print("I'm sorry but thats not an option... ")
    
def Solve():
    global GridTrtl, Runner, PathCreator, Solver
    solveValue = 0
    while len(FinishPath) != 0:
        solverCoords = FinishPath[0]
        solverX = solverCoords[0]
        solverY = solverCoords[1]
        solver.goto(solverX + 10, solverY - 10)
        del FinishPath[0]
        solveValue += 1
    choice = input("")

ML.DrawGrid()
Start()

wn.mainloop()
