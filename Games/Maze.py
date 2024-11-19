print("https://github.com/Lotux003/TurtleGraphics-Maze")
import turtle as trtl, MazeLib as ML

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
GridTrtl.color("black")
Runner.color("black")
Solver.color("red")
Runner.speed(0)
PathCreator.color("white")
PathCreator.speed(0)
PathCreator.left(90)
PathCreator.hideturtle()
Solver.hideturtle()

ML.DrawGrid(GridTrtl, wn)
ML.Start(Runner, PathCreator, Solver, wn)
        
wn.mainloop()
