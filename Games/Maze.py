import turtle as trtl
import MazeLib as mm

wn = trtl.Screen()
GridTrtl = trtl.Turtle()
Runner = trtl.Turtle()
PathCreator = trtl.Turtle()
Solver = trtl.Turtle()
GridTrtl.speed(0)
GridTrtl.color("black")
Runner.color("black")
Solver.color("blue")
Runner.speed(0)
PathCreator.color("white")
PathCreator.speed(0)
PathCreator.left(90)
PathCreator.hideturtle()
Solver.hideturtle()

#add a turtle you can draw with in the top left of sreen

mm.DrawGrid(GridTrtl, wn)
mm.Start(Runner, PathCreator, Solver, wn)
        
wn.mainloop()