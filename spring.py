### SETUP ELEMENTS FOR GRAPHING, SIMULATION, VISUALIZATION, TIMING
# ------------------------------------------------------------------------



# Define scene objects (units are in meters)
springLengthInitial = 1.0
spring_length =  2.0
# helix(axis = (0, 1, 0), length = springLengthInitial, radius = 0.1,  thickness = 0.05, color = color.green)



### SETUP PARAMETERS AND INITIAL CONDITIONS
# ----------------------------------------------------------------------------------------

# Define parameters
mass_m = 0.5 # mass of cart in kg
mass_pos = [0, springLengthInitial, 0] # initial position of the mass in(x, y, z) form, units are in meters
mass_v = [0, 0, 0] # initial velocity of mass in (vx, vy, vz) form, units are m/s

g = -9.8 # acceleration due to gravity; units are m/s/s

k = 15.0 # spring constant; units are N/m

# Define time parameters
t = 0 # starting time
deltat = 0.01  # time step units are s


### CALCULATION LOOP; perform physics updates and drawing
# ------------------------------------------------------------------------------------
import math,sys
from PIL import Image, ImageDraw

def mag(v):
  return math.sqrt(v[0]*v[0]+ v[1]*v[1]+ v[2]*v[2])

while t < 2 :  # run for one second

    # Required to make animation visible / refresh smoothly (keeps program from running faster
    #    than 1000 frames/s)

    # calculate the spring displacement
    springDisplacement = (spring_length - springLengthInitial)
    print "springDisplacement=%r\n"%(springDisplacement)

    # compute the force on the mass by the spring
    Fspring = -k * springDisplacement
    print "Fspring=%r\n"%(Fspring)

    # compute the force on the mass by the gravitational field
    Fgravity = mass_m * g
    print "Fgravity=%r\n"%(Fgravity)

    # Compute Net Force
    Fnet = [0, Fspring + Fgravity, 0]
    print "Fnet=%r\n"%(Fnet)

    # Newton's 2nd Law
    new_Fnet=[x/mass_m for x in Fnet]
    print "mass_m=%r\n"%(mass_m)
    print "new_Fnet=%r\n"%(new_Fnet)


    calc=[x*deltat for x in new_Fnet]
    print "calc=%r\n"%(calc)
    mass_v=[sum(x) for x in zip(mass_v, calc)]
    print "mass_v=%r\n"%(mass_v)


    # Position update
    calc=[x*deltat for x in mass_v]
    print "calc=%r\n"%(calc)
    mass_pos=[sum(x) for x in zip(mass_pos, calc)]
    print "mass_pos=%r\n"%(mass_pos)

    spring_length = mass_pos[1]# attribute y'



    # Calculate energy
    KE = 0.5 * mass_m * mag(mass_v)**2
    GPE = mass_m * (-g) * mass_pos[1] # relative to the ground
    EPE = 0.5 * k * springDisplacement**2

    # Update graphs
    #energyGraph.plot(t, KE, GPE, EPE, (KE + GPE + EPE)) # plot energies

    # Time update
    t = t + deltat

    print "mass_pos=%r\n"%(mass_pos)


    #draw points
    im = Image.open("Untitled.png")

    draw = ImageDraw.Draw(im)
    #draw.point((mass_pos[0], mass_pos[1]) , fill=(255,0,0))
    draw.ellipse((mass_pos[0], mass_pos[1], mass_pos[0]+1, mass_pos[1]+1), fill = 'blue', outline ='blue')
    draw.point((200,150),fill=255)

    #del draw

    # write to stdout
    im.save( "output/%s_%s.png"%(mass_pos[0],mass_pos[1]), "PNG")


### OUTPUT
# --------------------------------------------------------------------------------------

# Print the final time
print t
