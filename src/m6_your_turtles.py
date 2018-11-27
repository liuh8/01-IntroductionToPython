"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Hongyu Liu.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################


########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

didi = rg.SimpleTurtle('turtle')
didi.pen = rg.Pen('red', 5)
didi.speed = 15


import math


for k in range (8):
    didi.draw_circle(100)
    didi.right(135)
    didi.forward(100 * math.sqrt(2))
    didi.right(90)
    didi.forward(100 * math.sqrt(2))
    didi.draw_circle(-100)

window.tracer(500)

ains = rg.SimpleTurtle('square')
ains.pen = rg.Pen('pink', 2)
ains.forward(50)

for k in range (699):
    ains.right(99)
    ains.forward(k)


window.close_on_mouse_click()
