# Yong Jun Nam 902879851
# jnam08@gatech.edu
# My partner, Brett Davis, and I worked on this assignment alone, using only this semester's course materials.

from Graphics import *
from Myro import timer #keeps track of timer

NUMBALLS = 1
WINSIZE = 500
win = Window("Pong", WINSIZE, WINSIZE)
win.mode = "manual" # to make it look "smoother"
balls = []
dx = []
dy = []