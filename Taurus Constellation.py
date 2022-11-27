# This program displays Taurus Constellation
# in cartesian coordinate system, the names
# of the stars, the costellation lines

# Set up the graphics window and import turtle
import turtle
turtle.setup(600, 600)

# Set up the turtle
turtle.penup()
turtle.hideturtle()
turtle.speed(5)

# Create named constants for the stars coordinates
STAR_ONE_X = 2
STAR_ONE_Y = -8

STAR_TWO_X = 24
STAR_TWO_Y = -8

STAR_THREE_X = 14
STAR_THREE_Y = 16

STAR_FOUR_X = -4
STAR_FOUR_Y = 36

STAR_FIVE_X = -28
STAR_FIVE_Y = 4

STAR_SIX_X = -44
STAR_SIX_Y = 86

STAR_SEVEN_X = -168
STAR_SEVEN_Y = 164

STAR_EIGHT_X = -208
STAR_EIGHT_Y = 72

STAR_NINE_X = 84
STAR_NINE_Y = -48

STAR_TEN_X = 178
STAR_TEN_Y = -40

STAR_ELEVEN_X = 192
STAR_ELEVEN_Y = -80

STAR_TWELWE_X = 200
STAR_TWELWE_Y = -88

STAR_THIRTEEN_X = 40
STAR_THIRTEEN_Y = -96

STAR_FOURTEEN_X = 80
STAR_FOURTEEN_Y = -134

# Draw stars with dots
turtle.goto(STAR_ONE_X, STAR_ONE_Y)
turtle.dot()
turtle.goto(STAR_TWO_X, STAR_TWO_Y)
turtle.dot()
turtle.goto(STAR_THREE_X, STAR_THREE_Y)
turtle.dot()
turtle.goto(STAR_FOUR_X, STAR_FOUR_Y)
turtle.dot()
turtle.goto(STAR_FIVE_X, STAR_FIVE_Y)
turtle.dot()
turtle.goto(STAR_SIX_X, STAR_SIX_Y)
turtle.dot()
turtle.goto(STAR_SEVEN_X, STAR_SEVEN_Y)
turtle.dot()
turtle.goto(STAR_EIGHT_X, STAR_EIGHT_Y)
turtle.dot()
turtle.goto(STAR_NINE_X, STAR_NINE_Y)
turtle.dot()
turtle.goto(STAR_TEN_X, STAR_TEN_Y)
turtle.dot()
turtle.goto(STAR_ELEVEN_X, STAR_ELEVEN_Y)
turtle.dot()
turtle.goto(STAR_TWELWE_X, STAR_TWELWE_Y)
turtle.dot()
turtle.goto(STAR_THIRTEEN_X, STAR_THIRTEEN_Y)
turtle.dot()
turtle.goto(STAR_FOURTEEN_X, STAR_FOURTEEN_Y)
turtle.dot()

# Display names
turtle.goto(STAR_ONE_X, STAR_ONE_Y)
turtle.write('ϑ')
turtle.goto(STAR_TWO_X, STAR_TWO_Y)
turtle.write('γ')
turtle.goto(STAR_THREE_X, STAR_THREE_Y)
turtle.write('δ')
turtle.goto(STAR_FOUR_X, STAR_FOUR_Y)
turtle.write('ε')
turtle.goto(STAR_FIVE_X, STAR_FIVE_Y)
turtle.write('Aldebaran')
turtle.goto(STAR_SIX_X, STAR_SIX_Y)
turtle.write('τ')
turtle.goto(STAR_SEVEN_X, STAR_SEVEN_Y)
turtle.write('Alnath')
turtle.goto(STAR_EIGHT_X, STAR_EIGHT_Y)
turtle.write('ζ')
turtle.goto(STAR_NINE_X, STAR_NINE_Y)
turtle.write('λ')
turtle.goto(STAR_ELEVEN_X, STAR_ELEVEN_Y)
turtle.write('ξ')
turtle.goto(STAR_THIRTEEN_X, STAR_THIRTEEN_Y)
turtle.write('μ')
turtle.goto(STAR_FOURTEEN_X, STAR_FOURTEEN_Y)
turtle.write('ν')

# Draw lines in the Center "Aldebaran" or the Head
turtle.goto(STAR_ONE_X, STAR_ONE_Y)
turtle.pendown()
turtle.goto(STAR_TWO_X, STAR_TWO_Y)
turtle.goto(STAR_THREE_X, STAR_THREE_Y)
turtle.goto(STAR_FOUR_X, STAR_FOUR_Y)
turtle.goto(STAR_FIVE_X, STAR_FIVE_Y)
turtle.goto(STAR_ONE_X, STAR_ONE_Y)
turtle.penup()

# Draw the Bottom Horn
turtle.goto(STAR_FIVE_X, STAR_FIVE_Y)
turtle.pendown()
turtle.goto(STAR_EIGHT_X, STAR_EIGHT_Y)
turtle.penup()

# Draw the Upper Horn
turtle.goto(STAR_FOUR_X, STAR_FOUR_Y)
turtle.pendown()
turtle.goto(STAR_SIX_X, STAR_SIX_Y)
turtle.goto(STAR_SEVEN_X, STAR_SEVEN_Y)
turtle.penup()

# Draw the Neck of the Bull which is STAR_TWO TO STAR_TWO
turtle.goto(STAR_TWO_X, STAR_TWO_Y)
turtle.pendown()
turtle.goto(STAR_NINE_X, STAR_NINE_Y)
turtle.penup()

# Draw the Upper Body Part
turtle.goto(STAR_NINE_X, STAR_NINE_Y)
turtle.pendown()
turtle.goto(STAR_TEN_X, STAR_TEN_Y)
turtle.goto(STAR_ELEVEN_X, STAR_ELEVEN_Y)
turtle.goto(STAR_TWELWE_X, STAR_TWELWE_Y)
turtle.penup()

# Draw the Bottom Body part
turtle.goto(STAR_NINE_X, STAR_NINE_Y)
turtle.pendown()
turtle.goto(STAR_THIRTEEN_X, STAR_THIRTEEN_Y)
turtle.goto(STAR_FOURTEEN_X, STAR_FOURTEEN_Y)
turtle.penup()

# To keep the graphics window open. (Not necessary with IDLE)
turtle.done()


