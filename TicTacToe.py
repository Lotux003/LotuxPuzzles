#initization
import turtle as trtl
import string
import random

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic('r.png')

#setup
circle = trtl.Turtle()
circle.hideturtle
x = trtl.Turtle()
x.hideturtle


spots = {
    1 : (-75, 75),
    2 : (0, 75 ),
    3 : (75, 75),
    4 : (-75, 0),
    5 : (0, 0),
    6 : (75, 0),
    7 : (-75, -75),
    8 : (0, -75),
    9 : (-75, -75),
}


wn.mainloop()
