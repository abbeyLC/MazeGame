# ABIGAIL CENTERS
# PYTHON TERM PROJECT
# GROUP NAME: FANTASY FANS
# FALL 2018


# BUILT OFF OF THIS PYTHON MAZE GAME TUTORIAL
    ### https://www.youtube.com/watch?v=-0q_miviUDs

    # used to help with reusable text on screen
    # ### https://stackoverflow.com/questions/34823206/turtle-delete-writing-on-screen-and-rewrite

    # source for homescreen background
    # https://brightporclain.wordpress.com/tag/labyrinth-of-gedref

# MUSIC SOURCES
# https://www.youtube.com/watch?v=lR2UeagTRAM&list=PLPwMElqYPbF_d-44Qt1M8eOzVqSY6nr24&index=1
# https://www.youtube.com/watch?v=LJXKEgGlx-o&index=6&list=PLPwMElqYPbF_d-44Qt1M8eOzVqSY6nr24



# CODE SEPARATED BY "########" IS WRITTEN BY MYSELF
# I ALSO CHANGED ORGANIZATION OF CODE INTO CLASSES

# score calculation
# for every second left on the clock at the end of the game, user earns 10 pts
# user also earns 5 pts * health
#       ex. if user has 5/20 health left, user earns 5*5 = 25 pts





import turtle
import math
import time
import random
import pygame



pygame.init()
gamesong = pygame.mixer.Sound("gamesong.wav")
homescreensong = pygame.mixer.Sound("homescreensong.wav")

# register shapes
turtle.register_shape("ArthurRight.gif")
turtle.register_shape("ArthurLeft.gif")
turtle.register_shape("clock2.gif")
turtle.register_shape("clock5.gif")
turtle.register_shape("clock10.gif")
turtle.register_shape("labyrinth.gif")


class Spell(turtle.Turtle):
    def __init__(self, x, y, type):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.type = type
        self.gameover = False

        if self.type == 'bad':
            self.color("purple")
        else:
            self.color("white")

        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.showturtle()
        self.Health = 0.5
        self.walls = []

        self.direction = random.choice(['up','down','left','right'])


    def move(self):
        if self.direction == 'up':
            dx = 0
            dy = 24
        elif self.direction == 'down':
            dx = 0
            dy = -24
        elif self.direction == 'left':
            dx = -24
            dy = 0
        elif self.direction == 'right':
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # calculate spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # check if the space has a wall
        if (move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(['up','down','left','right'])

        # set timer to move next time
        if self.gameover == False:
            turtle.ontimer(self.move, t=random.randint(100,300))




    ########
    def show(self):
        self.color("dark red")
        self.showturtle()

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        self.walls = []


    def setWallsList(self, wallcoord):
        self.walls = wallcoord
    ########



    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # check if the space has a wall
        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("ArthurLeft.gif")

        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("ArthurRight.gif")

        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def is_collision(self, other):
        # pythagorean theorem to find distance between self and wall
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2 ) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


########
    def can_see(self, other, level):
        # pythagorean theorem to find distance between self wall
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        # decrease visibility with each level
        if level == 1:
            return True

        if level == 2:
            if distance < 200:
                return True
            else:
                return False

        if level == 3:
            if distance < 100:
                return True
            else:
                return False

########

class HealthBar(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)

        self.w = 200

        self.penup()
        self.speed(0)
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.pencolor("black")
        self.fillcolor("green")
        self.begin_fill()
        self.forward(self.w)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(self.w)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.end_fill()

        self.pendown()
        self.forward(200)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(200)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.hideturtle()

    def setwidth(self, n):
        self.w = self.w + n
        self.clear()
        self.goto(self.x, self.y)
        self.pencolor("black")
        self.fillcolor("green")
        self.begin_fill()
        self.forward(self.w)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(self.w)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.end_fill()

        self.pendown()
        self.forward(200)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(200)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.hideturtle()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("ArthurRight.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.walls = []


    ########
        self.health = 20
        self.timer = 10

    def setWallsList(self, wallcoord):
        self.walls = wallcoord
    ########




    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # check if the space has a wall
        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("ArthurLeft.gif")

        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("ArthurRight.gif")

        if (move_to_x, move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)

    def is_collision(self, other):
        # pythagorean theorem to find distance between self and clock
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2 ) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False





########
    def can_see(self, other, level):
        # pythagorean theorem to find distance between self wall
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        # decrease visibility with each level
        if level == 1:
            return True

        if level == 2:
            if distance < 200:
                return True
            else:
                return False

        if level == 3:
            if distance < 100:
                return True
            else:
                return False

    def is_winner(self, x, y):
        a = self.xcor() - x
        b = self.ycor() - y
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Wall (turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.hideturtle()

    def show(self):
        self.showturtle()

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
########

class Clock(turtle.Turtle):
    def __init__(self,x,y,t):

        turtle.Turtle.__init__(self)

        if t == 2:
            self.shape("clock2.gif")
        elif t == 5:
            self.shape("clock5.gif")
        elif t == 10:
            self.shape("clock10.gif")

        self.penup()
        self.speed(0)
        self.timer = t
        self.goto(x,y)
        self.showturtle()

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class MazeGame(object):
    def __init__(self, wn):

        self.game = True        # set to false and will stop game loop if user presses escape button
        self.gameover = False

        # Create levels list
        self.levels = ['']
        self.winx = -2000       # x position of win position (opening to the maze)
        self.winy = -2000       # y position of the win position (opening to the maze)

        self.level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXP   XXXXXXX    B   F XX",
            "XX    XXXXXXXX         XX",
            "XXX    W            XXXXX",
            "XXXXXXX         XXXXXXXXX",
            "XXXXX    XXXXXXXX      XX",
            "XXXXX   XXXXXXXXX    XXXX",
            "XX                 XXXXXX",
            "XXXX         XXXXXXXXX XX",
            "XX            XXXXXXXT XX",
            "XXXXXXXXXXXX          XXX",
            "XXXXXXX     G      XXXXXX",
            "XXXXX    B         XXXXXX",
            "XX    XXXXXXX          XX",
            "O   XXXXXXXX       XXXXXX",
            "XXXXXX            XXXXXXX",
            "XXXXXXXXXXXXXX F  XXX  XX",
            "XXXXXXXXXXX            XX",
            "XXXXXXXXXXX      XXXXXXXX",
            "XXXXXXXXXXX            XX",
            "XX     T       B  XXXXXXX",
            "XXXXXX   XXXXX      T XXX",
            "XXXXXXX   XXXXXXXXXXXXXXX",
            "XXX      B             XX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
        ]
        self.level_2 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XP         W       G   XX",
            "XXXXX  XXXXXXX      B  XX",
            "XXX             X    X XX",
            "XXXXXXX         X XX XT X",
            "XXXXX  B XXX  X      XXXX",
            "XXXXX   XXXXXXXXX    XXXX",
            "XX                 XXXX O",
            "XXXX  F     XXXXXXXXXX  X",
            "XX            XXXXXXX   X",
            "XXXXXXXXXXXX           WX",
            "XXXXXXX              XXXX",
            "XXXXX     B          XXXX",
            "XX   TXXXXXXX         X X",
            "X     XXXXXX    XXXXXXX X",
            "XXXXXX            T     X",
            "XXX    XXXXXXX  X XXX XXX",
            "XXXXXX  FXX     X      XX",
            "XXXXXXXXXXX      XX XXXXX",
            "XXXXXXXXXXX    G       XX",
            "X     F           XXXXXXX",
            "XXXXXX   XXXXX    B   XXX",
            "XXXXXXX   XXXXXXXXXXXXXXX",
            "XXX  T   B              X",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"]
        self.level_3 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XP    XXXXXXX   XXXXX  XX",
            "X     XXXXXXXX F    B  XX",
            "XXX W     XX    XXXXXXXXX",
            "XXXXXXX         XXXX GXXX",
            "XXXXX    XXXXXXXXXXB   XX",
            "XXXXX   XXXXXXXXX    XXXX",
            "XX            W    XXX TX",
            "XXXXXXXXX    XXXXXXXXX  X",
            "XX    B       XXXXXXX   X",
            "XXXXXXXXXXXX          XXX",
            "XXXXXXX F     XX   XXXXXX",
            "XXXXX    XXXXXXX   XXXXXX",
            "XX    XXXXX XXXX       GX",
            "X   XXXXXXX XXX    XXXXXX",
            "X  XXX           XXXXX XX",
            "XF XXXX    XXX    XXX FXX",
            "X XX XXX  XXXXX   B    XX",
            "XGXX XXX  XXXXX  XXXXXXXX",
            "XXXX XXXXXXXXXX    B   XX",
            "X T               XXXXXXX",
            "XXXXXX   XXXXX       TXXX",
            "XXXXXXX   XXXXXXXXXXXXXXX",
            "XXX B   X               O",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
        ]


        # for choosing the level from the list of levels
        self.lvl = 1
        # add levels to the mazes list
        self.levels.append(self.level_1)
        self.levels.append(self.level_2)
        self.levels.append(self.level_3)


        #self.wn = turtle.Screen()
        self.wn = wn
        self.wn.bgcolor("grey")
      #  self.wn.title("The Labyrinth of Gedref")
        self.wn.setup(700, 700)
        self.wn.tracer(0)


        # the player
        self.player = Player()

    ########

        # add a clocks list
        self.clocks = []

        # add walls list
        self.wallsList = []

        # wall coordinate list
        self.walls = []

        # badspell coordinate list
        self.gamespells = []

        # set up the level
        self.setup_maze(self.levels[self.lvl])

        # update the walls list in player object
        self.player.setWallsList(self.walls)

        # need timer to decrement the value displayed in the upper right hand corner
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()

        # keyboard binding
        turtle.listen()

        turtle.onkeypress(self.player.go_left, "Left")
        turtle.onkeypress(self.player.go_right, "Right")
        turtle.onkeypress(self.player.go_up, "Up")
        turtle.onkeypress(self.player.go_down, "Down")


        turtle.onkey(self.menuScreen, 'Escape')



        # change timer display in upper right hand corner
        self.pen.goto(230, 315)
        self.erasable = self.erasableWrite(self.pen, "Timer: " + str(self.player.timer), font=("Arial", 12, "normal"))
        turtle.ontimer(self.clockTick, 1000)
    ########



        # set walls list for collision detection and start moving bad spells
        for spell in self.gamespells:
            spell.setWallsList(self.walls)
        for spell in self.gamespells:
            turtle.ontimer(spell.move, t=250)


        self.healthbar = HealthBar(-300,315)

        won = False

        self.pen.goto(-340, 280)
        self.pen.write("Esc\nto\nexit", font=("Arial", 12, "bold"))

        # main game loop
        # break from the loop if user health is <= 0 or timer <= 0
        while self.player.health > 0 and self.player.timer > 0 and self.game:
            # check for player collision with clock
            # iterate through clock list

            for clock in self.clocks:
                if self.player.is_collision(clock):
                    # add the clock time to the player time
                    self.player.timer += clock.timer
                    print("Player time: ",format(self.player.timer))
                    # destroy the clock
                    clock.destroy()
                    #remove the clock from the clocks list
                    self.clocks.remove(clock)

            for spell in self.gamespells:
                if self.player.is_collision(spell):
                    if spell.type == 'bad':
                        self.player.health -= spell.Health
                        self.healthbar.setwidth(-5)          # 5/200 for health bar equivalent to 0.5/20 for health
                    else:
                        if self.player.health < 20:
                            self.player.health += spell.Health
                            self.healthbar.setwidth(5)
                    print("Player health: ",format(self.player.health))



        ######## hide or show based on visibility of object and difficulty of level
            for w in self.wallsList:
                if self.player.can_see(w,self.lvl):
                    w.show()
                else:
                    w.hideturtle()

            for c in self.clocks:
                if self.player.can_see(c, self.lvl):
                    c.showturtle()
                else:
                    c.hideturtle()

            for spell in self.gamespells:
                if self.player.can_see(spell,self.lvl):
                    spell.showturtle()
                else:
                    spell.hideturtle()


            # if the player has found the opening to a level
            if self.player.is_winner(self.winx, self.winy):
                self.lvl += 1


                # break from the loop if the user has completed the last level
                if self.lvl == len(self.levels):
                    won = True
                    break

                # destroy the walls and clocks if generating a new level
                for wall in self.wallsList:
                    wall.destroy()
                self.walls.clear()
                self.wallsList.clear()

                for clock in self.clocks:
                    clock.destroy()
                self.clocks.clear()

                for spell in self.gamespells:
                    spell.destroy()
                self.gamespells.clear()



                # setup maze, start moving bad spells, and update wall lists for collision detection in player and spells objects
                self.setup_maze(self.levels[self.lvl])
                for spell in self.gamespells:
                    turtle.ontimer(spell.move, t=250)
                for spell in self.gamespells:
                    spell.setWallsList(self.walls)
                self.player.setWallsList(self.walls)
        ########

            # update screen
            self.wn.update()


        # ensure that all ontimer functions are no longer running
    ########
        self.gameover = True
        for spell in self.gamespells:
            spell.gameover = True

        # calculate score
        score = 0
        score = score + 5 * self.player.health
        score = score + 10 * self.player.timer

        if self.game == True:        # if user did not press the escape button
            # user has completed the last level or has died
            self.pen.goto(-150,0)
            self.pen.pencolor("white")
            if self.player.timer <= 0:
                self.pen.write("GAME OVER", font=("Arial", 40, "bold"))
                self.pen.goto(-120, -30)
                self.pen.write("You ran out of time!", font=("Arial", 20, "bold"))
            elif self.player.health <= 0:
                self.pen.write("GAME OVER", font=("Arial", 40, "bold"))
                self.pen.goto(-50, -30)
                self.pen.write("You died!", font=("Arial", 20, "bold"))
            else:
                self.pen.write("YOU WIN!", font=("Arial", 40, "bold"))
                self.pen.goto(-100, -50)
                self.pen.write("Score: " + str(score), font=("Arial", 12, "bold"))
            time.sleep(3)


    ########


    def setup_maze(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "X":
                    # add coordinates to wall list
                    # coordinate pair is a tuple
                    self.walls.append((screen_x, screen_y))

                    ########
                    self.wallsList.append(Wall(screen_x,screen_y))
                    ########

                # check if it is a player
                if character == "P":
                    self.player.goto(screen_x,screen_y)


                ########
                # check if it is a 10 sec clock
                if character == "T":
                    self.clocks.append(Clock(screen_x, screen_y,10))

                # check if it is a 5 sec clock
                if character == "F":
                    self.clocks.append(Clock(screen_x, screen_y, 5))

                # check if it is a 2 sec clock
                if character == "W":
                    self.clocks.append(Clock(screen_x, screen_y, 2))

                # check if bad spell
                if character == "B":
                    self.gamespells.append(Spell(screen_x,screen_y, 'bad'))

                # check if good spell
                if character == "G":
                    self.gamespells.append(Spell(screen_x,screen_y, 'good'))


                if character == "O":
                    self.winx = screen_x
                    self.winy = screen_y

            ########



###### update text for timer in upper right hand corner
    def clockTick(self):
        self.pen.goto(230, 315)
        self.player.timer = self.player.timer - 1
        self.erasable.clear()
        self.erasable = self.erasableWrite(self.pen, "Timer: " + str(self.player.timer), font=("Arial", 12, "normal"), reuse=self.erasable)

        if self.gameover == False:
            turtle.ontimer(self.clockTick, 1000)


    def menuScreen(self):
        self.game = False

######


    def erasableWrite(self, tortoise, name, font, reuse=None):
        eraser = turtle.Turtle() if reuse is None else reuse
        eraser.hideturtle()
        eraser.up()
        eraser.setposition(tortoise.position())
        eraser.color("white")
        eraser.write(name, font=font)
        return eraser



########
class Homescreen(object):
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("The Labyrinth of Gedref")
        self.wn.tracer(0)
        self.gamesong = gamesong
       # self.homescreensong = homescreensong

        turtle.listen()
        turtle.onkey(self.choseMenuItem, 'Return')
        turtle.onkey(self.downOption, 'Down')
        turtle.onkey(self.upOption, 'Up')
        self.howToPlayText = False
        self.start()


    def start(self):

        homescreensong.play(loops=-1)

        #self.homescreensong.play(loops=-1)
       # self.viewInstructs = False
        self.howToPlayText = False
        self.wn.bgcolor("black")
        self.wn.bgpic("labyrinth.gif")
        self.wn.setup(430, 530)
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.homescreen = True

        self.textx = -70

        # keyboard binding
        turtle.listen()
        turtle.onkey(self.choseMenuItem, 'Return')
        turtle.onkey(self.downOption, 'Down')
        turtle.onkey(self.upOption, 'Up')

        # for making the "press enter to start game" text blink on the screen
        self.blink = 0
        self.blink2 = 0
        self.option1 = True
        self.option2 = False

        self.pen.penup()
        self.pen.goto(self.textx,200)
        self.erasable = self.erasableWrite(self.pen, "START GAME", font=("Arial", 16, "bold"))

        self.pen.goto(self.textx,150)
        self.erasable2 = self.erasableWrite(self.pen, "HOW TO PLAY", font = ("Arial", 16, "bold"))

        #self.erasable3
           # = self.erasableWrite(self.pen, "", font=("Arial", 20, "bold"))


        turtle.hideturtle()
        while self.homescreen:
            #print(str(self.option1) + " " + str(self.option2))
          #  print(turtle.isvisible())
            # update screen
            if self.option1 == True:
                if self.blink == 0:
                    self.erasable.clear()
                    self.blink = 1

                elif self.blink == 1:
                    self.pen.goto(self.textx, 200)
                    self.erasable = self.erasableWrite(self.pen, "START GAME", font=("Arial", 16, "bold"), reuse=self.erasable)
                    self.blink = 0
                self.wn.update()
                time.sleep(0.5)

            elif self.option2 == True:
                if self.blink2 == 0:
                   self.erasable2.clear()
                   self.blink2 = 1

                elif self.blink2 == 1:
                   self.pen.goto(self.textx, 150)
                   self.erasable2 = self.erasableWrite(self.pen, "HOW TO PLAY", font=("Arial", 16, "bold"),
                                                      reuse=self.erasable2)
                   self.blink2 = 0
                self.wn.update()
                time.sleep(0.5)

            if self.howToPlayText == True:
                self.erasable.clear()
                self.erasable2.clear()

                header = "Press Esc to return to the main menu"
                d0 = "Solve the maze before it's too late!\n\n"
                d1 = "There are three levels. Move on to the next level by locating "
                d2 = "and exiting the current maze. Collect blue timers to add two\n"
                d3 = "seconds to the clock, red timers to add five seconds, and gold "
                d4 = "timers to add 10. The labyrinth is also enchanted with harmful\n"
                d5 = "spells; avoid them if you want to make it out alive! Replenish "
                d6 = "your health by standing in the midst of a healing spell. Both \n"
                d7 = "good and bad spells move about the maze randomly. As you progress "
                d8 = "through each level, your visibilty of the maze decreases.\n"
                d9 = "Your timer does not reset when you start a new level, so collecting "
                d10 = "timers in an easier level may help you in a more difficult level,\n"
                d11 = "where you may need more time to find the exit.\n"

                t0 = "Helpful tips!\n\n"
                t1 = "**** Spells do not change direction until they have contacted a wall in the maze.\n"
                t2 = "**** You can get a higher score by completing the maze with little damage to your health and plenty of time left on the clock!"

                e0 = "Episode synopsis:\n\n"
                e1 = "Prince Arthur has mercilessly slaughtered a unicorn during a "
                e2 = "hunting expidition. As punishment, The Keeper of the Unicorns\n"
                e3 = "has cursed Camelot with famon and drought. Arthur must prove himself "
                e4 = "worthy of leading Camelot in order to lift the curse.\n"
                e5 = "Sorry for his crime, he obeys the Keeper of the Unicorns "
                e6 = "by traveling to Labyrinth of Gedref, where not only hit wits,\nbut also his courage, will be tested.\n"

                directions = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11
                tips = t1+t2
                episodeSyn = e1+e2+e3+e4+e5+e6


                y = 270
                self.pen.goto(self.textx - 290, y)
                self.pen.write(header, font=("Arial", 12, "normal"))
                self.pen.goto(self.textx-290, y - 90)
                self.pen.write(d0, font=("Arial", 14, "bold"))

                self.pen.goto(self.textx-290, y-160)
                self.pen.write(directions, font=("Arial", 10, "normal"))

                y -= 105

                c1 = Clock(self.textx-250, y-80, 2)
                c2 = Clock(self.textx-250, y-110, 5)
                c3 = Clock(self.textx-250, y-140, 10)
                sp1 = Spell(self.textx-250,y-170,'good')
                sp1 = Spell(self.textx-250,y-200,'bad')

                self.pen.goto(self.textx-230, y-90)
                self.pen.write("Adds two seconds to the clock", font=("Arial", 12, "normal"))
                self.pen.goto(self.textx-230, y-120)
                self.pen.write("Adds five seconds to the clock", font=("Arial", 12, "normal"))
                self.pen.goto(self.textx-230, y-150)
                self.pen.write("Adds 10 seconds to the clock", font=("Arial", 12, "normal"))
                self.pen.goto(self.textx-230, y-180)
                self.pen.write("Healing spell", font=("Arial", 12, "normal"))
                self.pen.goto(self.textx-230, y-210)
                self.pen.write("Harmful spell", font=("Arial", 12, "normal"))


                y -= 50


                self.pen.goto(self.textx - 290, y-270)
                self.pen.write(t0, font=("Arial", 14, "bold"))
                self.pen.goto(self.textx-290, y-260)
                self.pen.write(tips, font=("Arial", 10, "normal"))

                self.pen.goto(self.textx - 290, y-350)
                self.pen.write(e0, font=("Arial", 14, "bold"))
                self.pen.goto(self.textx - 290, y-390)
                self.pen.write(episodeSyn, font=("Arial", 10, "normal"))

                self.howToPlayText = False      # don't draw again
                self.wn.update()

            else:
                self.wn.update()



    def choseMenuItem(self):
        if self.option1 == True:
            self.initiateGame()
           # self.start()
            self.__init__()
        elif self.option2 == True:
            self.howToPlay()

    def menuScreen(self):
        self.wn.clearscreen()
        self.__init__()         # replaced start func


    def howToPlay(self):
        self.wn.clearscreen()
        self.wn.bgcolor("grey")
        self.wn.setup(800,600)
        turtle.onkey(self.menuScreen, 'Escape')
        self.howToPlayText = True
        self.option1 = False
        self.option2 = False

    def downOption(self):
        self.pen.goto(self.textx, 200)
        self.erasable = self.erasableWrite(self.pen, "START GAME", font=("Arial", 16, "bold"), reuse=self.erasable)
        self.option1 = False
        self.option2 = True

    def upOption(self):
        self.pen.goto(self.textx, 150)
        self.erasable2 = self.erasableWrite(self.pen, "HOW TO PLAY", font=("Arial", 16, "bold"), reuse=self.erasable2)
        self.option1 = True
        self.option2 = False

    def initiateGame(self):
        self.homescreen = False
        self.wn.clearscreen()
        homescreensong.stop()
        gamesong.play(loops=-1)

        # start the game
        try:
            game = MazeGame(self.wn)
        except Exception:
            pass

        self.wn.clearscreen()
        gamesong.stop()

    def donothing(self):
        donothing = 0



########


    def erasableWrite(self, tortoise, name, font, reuse = None):
        eraser = turtle.Turtle() if reuse is None else reuse
        eraser.hideturtle()
        eraser.up()
        eraser.setposition(tortoise.position())
        eraser.color("black")
        eraser.write(name, font=font)
        return eraser




########
if __name__ == "__main__":

    try:
        homescreen = Homescreen()
    except Exception:
        pass

    gamesong.stop()
    homescreensong.stop()

########



