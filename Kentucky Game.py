import turtle
import math
import os
import random
import time 


turtle.register_shape("/Users/Macbook/Desktop/space invader/pressq.gif")
#----------------------------- The Screen -----------------------------#
wn= turtle.Screen()
wn.bgcolor("Black")
wn.bgpic("/Users/Macbook/Desktop/space invader/Fast food.gif")
wn.setup(width = 1000 , height = 600)
name = ("Kenney's Food Chase")

pressq = turtle.Turtle()
pressq.shape("/Users/Macbook/Desktop/space invader/pressq.gif")
pressq.goto(0, 0)
pressq.hideturtle()

#----------------------------- Pen to draw the score -----------------------------#
mypen = turtle.Turtle()
mypen.color("white")
mypen.pendown()
mypen.pensize(3)
mypen.hideturtle()

#----------------------------- Register the Images -----------------------------#
turtle.register_shape("/Users/Macbook/Desktop/space invader/New Game.gif")
turtle.register_shape("/Users/Macbook/Desktop/space invader/Fast food.gif")
turtle.register_shape("/Users/Macbook/Desktop/space invader/Drumstick.gif")
turtle.register_shape("/Users/Macbook/Desktop/space invader/bad_drumstick.gif")
turtle.register_shape("/Users/Macbook/Desktop/space invader/image.gif")
#----------------------------- The New Game Button -----------------------------#
# how the button looks
button = turtle.Turtle()
button.shape("/Users/Macbook/Desktop/space invader/New Game.gif")
button.goto(0, 0)

# how the button is clicked
def btnclick(x,y):
    if  x > -10 and x <10 and y >4 and  y < 8:
        button.hideturtle()

    button.hideturtle()
    
#----------------------------- Press A to stop the game -----------------------------#    
    pressa = turtle.Turtle()
    pressa.penup()
    pressa.setposition(-5, -287)
    pressa.color("white")
    pressa.write("Press a two times, to stop game", False, align = "left", font=("Arial",15,"normal"))
    
    
#----------------------------- Score/final score writing  -----------------------------#
    score = 0 

    
#----------------------------- Create the player graphic/characteristics -----------------------------#
    player = turtle.Turtle()
            #Set certain attributes/apperance to graphic
    player.color("blue")
    player.shape("/Users/Macbook/Desktop/space invader/image.gif")
        # cause not drawing a line put pen up
    player.penup()
        # set the speed to 0 because thats fastest option 
    player.speed(0)
        # setting the graphic to the center of screen and towards the bottom
    player.setposition(-340,0)
    # This is the code to get the arrow to face upwards
    player.setheading(90)

    #----------------------------- Create Multiple Good Chicken Drumsticks-----------------------------#

            # Find the code to increase by 4 each time the score goes up by 2

    number_of_goodenemy =  5
            #create an empty list of enemies
    goodenemy = []
            #add 5 enemties to the list
    for i in range(number_of_goodenemy):
                #the appemnnd method allows for an object to be added to the list (the list is going to be the enemies)
     goodenemy.append(turtle.Turtle())

    #----------------------------- Code to get the Good drumsticks to look the same-----------------------------#
    for good in goodenemy:
        good.color("red")
        good.shape("/Users/Macbook/Desktop/space invader/Drumstick.gif")
        good.penup()
        good.speed(0)
                # so enemies start at a random position on the screen
        x = random.randint(590, 800)
        y = random.randint(-250, 250)
                # start each enemy at a random spot 
        good.setposition(x, y)
                
        goodspeed = random.randint(3,25)

    #----------------------------- Arrow Keys -----------------------------#
    def up():
        player.setheading(90)
        player.forward(30)

    def down():
        player.setheading(-90)
        player.backward(-30)

    def right():
        player.setheading(0)
        player.backward(-30)

    def left():
        player.setheading(0)
        player.backward(30)

    def restart():
        button.undo()
        pressq.hideturtle()
        pressq.hideturtle()
        mypen.clear()



    def finishgame():
        for good in goodenemy:
            good.hideturtle()
        for bad in badenemy:
            bad.hideturtle()
        player.hideturtle()
        pressq.undo()
        pressa.undo()
        mypen.penup
        mypen.goto(-30,10)
        mypen.write( score, False, align = "left", font=("Arial",70,"normal") )
        
    

        #Set keyboard binding
    wn.listen()
    wn.onkey(up, "Up")
    wn.onkey(down, "Down")
    wn.onkey(right, "Right")
    wn.onkey(left, "Left")
    wn.onkey(restart,"q")
    wn.onkey(finishgame,"a")
          
     #----------------------------- Create Multiple Bad Chicken Drumsticks-----------------------------#

    number_of_badenemy =  6
            #create an empty list of enemies
    badenemy = []
            #add 2 enemties to the list
    for i in range(number_of_badenemy):
                #the appemnnd method allows for an object to be added to the list (the list is going to be the enemies)
        badenemy.append(turtle.Turtle())
            
     #----------------------------- Code to get the bad drumsticks to look the same-----------------------------#
    for bad in badenemy:
        bad.color("yellow")
        bad.shape("/Users/Macbook/Desktop/space invader/bad_drumstick.gif")
        bad.penup()
        bad.speed(0)
                # so enemies start at a random position on the screen
        x = random.randint(500, 900)
        y = random.randint(-250, 250)
                # start each enemy at a random spot 
        bad.setposition(x, y)
                
    badspeed = random.randint(7,10)

    #----------------------------- Code to get all the drumsticks to move across the screen, generating 3 more when scor +10-----------------------------#

    while True: 
            
        for good in goodenemy:
            x = good.xcor()
            x -= goodspeed
            good.setx(x)
        for bad in badenemy:
            x = bad.xcor()
            x -= badspeed
            bad.setx(x)

    #----------------------------- Collision between player and chicken to increase score -----------------------------#
        for good in goodenemy:
            d = math.sqrt(math.pow(player.xcor()-good.xcor(),2)+math.pow(player.ycor()-good.ycor(),2))
            if d < 74:
                good.setposition(random.randint(-1000, 900), random.randint(-250,250))
                goodspeed = random.randint(10,14)
                score += 10
                           #draw score
                mypen.undo()
                mypen.penup()
                mypen.hideturtle()
                mypen.setposition(-470, 280)
                scorestring = "Score: {0}".format(score)
                mypen.write(scorestring, False, align = "left", font=("Arial",14,"normal"))
                        
        #----------------------------- Collision between player and the bad chicken to decrease score -----------------------------#
        for bad in badenemy:
            d = math.sqrt(math.pow(player.xcor()-bad.xcor(),2)+math.pow(player.ycor()-bad.ycor(),2))
            if d < 74:
                bad.setposition(random.randint(-1000, 900), random.randint(-250,250))
                badspeed = random.randint(10,14)
                score -= 10
                                   #draw score
                mypen.undo()
                mypen.penup()
                mypen.hideturtle()
                mypen.setposition(-470, 280)
                scorestring = "Score: {0}".format(score)
                mypen.write(scorestring, False, align = "left", font=("Arial",14,"normal"))

        #----------------------------- Border Collision -----------------------------#
        for good in goodenemy:
            if good.xcor() < -490:
                good.goto(random.randint(-1000, 900), random.randint(-250,250))
                goodspeed = random.randint(16, 19)

        for bad in badenemy:
            if  bad.xcor() < -490:
                bad.goto(random.randint(-1000, 900), random.randint(-250,250))
                badspeed = random.randint(16, 19)

    



#----------------------------- Listen for the button -----------------------------#
turtle.onscreenclick(btnclick, 1)
turtle.listen()

turtle.done()



    
