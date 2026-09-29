#Game Variables
x=0 #x co ordinates of the objects
y=0 #y co ordinates of the objects
score1=0 #Tracking score
diff=0 # difficulty variable according to which the timer will shorten(.1s for every increment)
cl=0 #extra variable used to stop execution while closing the game window
time=60 # Game timer(in seconds)
Hole_pos=[(25, 90),   (197, 90),   (367, 90), (25, 190), (197, 190), (367, 190),(25, 290), (197, 290), (367, 290), (25, 390), (197, 390), (367, 390)]

root=None
canvas=None
var=None
var2=None
Start=None

time_id=None
countdown_id=None

mole=None
mole_snout=None
mole_eye1=None
mole_eye2=None