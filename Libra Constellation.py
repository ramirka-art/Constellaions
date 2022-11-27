# This program displays Libra Constellation in 
# castesian coordinate system, the names of the stars,
# the costellation lines


# Set up graphics window and import turtle
import turtle
turtle.setup(700, 600)

# Set up the turtle
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates
Beta_Librae_X = 0
Beta_Librae_Y = 240

Sigma_Librae_X = 50
Sigma_Librae_Y = 20

υ_Lib_X = -150
υ_Lib_Y = -20

τ_Lib_X = -170
τ_Lib_Y = -80

γ_Lib_X = -140
γ_Lib_Y = 170

θ_Lib_X = -240
θ_Lib_Y = 150

Alpha_Librae_X = 110
Alpha_Librae_Y = 140

# Draw the stars as dots
turtle.goto(Beta_Librae_X, Beta_Librae_Y) 
turtle.dot()

turtle.goto(Sigma_Librae_X, Sigma_Librae_Y) 
turtle.dot()

turtle.goto(υ_Lib_X, υ_Lib_Y) 
turtle.dot()

turtle.goto(τ_Lib_X, τ_Lib_Y) 
turtle.dot()

turtle.goto(γ_Lib_X, γ_Lib_Y) 
turtle.dot()

turtle.goto(θ_Lib_X, θ_Lib_Y) 
turtle.dot()

turtle.goto(Alpha_Librae_X, Alpha_Librae_Y) 
turtle.dot()

# Display the star names
turtle.goto(Beta_Librae_X, Beta_Librae_Y) 
turtle.write('Beta Librae')

turtle.goto(Sigma_Librae_X, Sigma_Librae_Y) 
turtle.write('Sigma LIbrae')

turtle.goto(υ_Lib_X, υ_Lib_Y) 
turtle.write('υ Lib')

turtle.goto(τ_Lib_X, τ_Lib_Y) 
turtle.write('τ Lib')

turtle.goto(γ_Lib_X, γ_Lib_Y) 
turtle.write('γ Lib')

turtle.goto(θ_Lib_X, θ_Lib_Y) 
turtle.write('θ Lib')

turtle.goto(Alpha_Librae_X, Alpha_Librae_Y) 
turtle.write('Alpha Librae')

# Connect stars with lines part 1. Center of Libra Constellation
turtle.goto(Beta_Librae_X, Beta_Librae_Y)
turtle.pendown()
turtle.goto(Alpha_Librae_X, Alpha_Librae_Y)
turtle.goto(Sigma_Librae_X, Sigma_Librae_Y)
turtle.goto(Beta_Librae_X, Beta_Librae_Y)
turtle.penup()
# I use here turtle.pendown() and turtle. penup() to make the connection in the particular part
# in this case it is the Center fo Libra Constellation

# Connect stars with lines part 2. The Upper part of Libra Constellation
turtle.goto(Beta_Librae_X, Beta_Librae_Y)
turtle.pendown()
turtle.goto(θ_Lib_X, θ_Lib_Y) 
turtle.goto(γ_Lib_X, γ_Lib_Y)
turtle.goto(Beta_Librae_X, Beta_Librae_Y)
turtle.penup()
# I use here turtle.pendown() and turtle. penup() to make the connection in the particular part
# in this case it is the Upper fo Libra Constellation
# Here i use turtle.penup() to relocate the turtle(the cursor) to the Sigma Librae without
# drawing unnecessry lines

# Connect stars with lines part 2. The Bottom part of Libra Constellation
turtle.goto(Sigma_Librae_X, Sigma_Librae_Y)
turtle.pendown() # the pen is down which helps me out to connect the Bottom part of Constellation
turtle.goto(τ_Lib_X, τ_Lib_Y)
turtle.goto(υ_Lib_X, υ_Lib_Y) 
turtle.goto(Sigma_Librae_X, Sigma_Librae_Y)
turtle.penup() # the pen is up which means you won't draw lines
# I use here turtle.pendown() and turtle. penup() to make the connection in the particular part
# in this case it is the Bottom fo Libra Constellation

# Keep the graphics window open (Not necessary with IDLE)
turtle.done() 
