#classes and functions
import turtle 
import math


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0
        
    def go_up(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        if(move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        if(move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)


    def go_left(self):
        move_to_x=player.xcor()-24
        move_to_y=player.ycor()
        if(move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)


    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        if(move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)
            
    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        
        distance=math.sqrt((a**2)+(b**2))
        return distance < 5
        
# Class Treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

# Creating Level Lists
global levels
levels= [""]
level_1 = [
"BBBBBBBBBBBBBBBBBBBBBBBBB",
"BP BBBBBBBBBBBBBBBBBBBBBB",
"B  BBBBBB        BBBBBBBB",
"B T   TBB   BB        BBB",
"BBBB   BB   BB   BB   BBB",
"BBBB   BB   BB   BB   BBB",
"BBBB   BB   BB   BBBBBBBB",
"BBBB        BB         BB",
"BBBBBB   BBBBBBBBBBB   BB",
"BBBBBB   BBBBBBBBBBB   BB",
"BBBBBB         BBBBB   BB",
"B   BBBB   BBBBBBBBB   BB",
"B   BBBB   BBBBBBBBBBBBBB",
"B   BBBB             BBBB",
"B          BBBBBBBBBBBBBB",
"BBBBBBBBB  BBBBBBBBBBBBBB",
"BBBB                 BBBB",
"BBBBBBBBBBBBBBBB   BBBBBB",
"BBBBBBBBBBBBBBBB   BBBBBB",
"BB   BBBBBBBBBBB   BBBBBB",
"BB   BBB           BBBBBB",
"BB   BBBBBBBBB     BBBBBB",
"BB                 BBBBBB",
"BBBBBBBBB   BBBBBBBBBBBBB",
"BBBBBBBBB         BBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBB"
]

level_2 = [
"BBBBBBBBBBBBBBBBBBBBBBBBB",
"BP  T           BB   TBBB",
"BB    BBBBBBBBB  BBB   BB",
"BB       BBBBBB  BBB   BB",
"BB  BBB     BBB        BB",
"BB  BBBBBBBBBBBBBBBB  BBB",
"BB          BBBB      BBB",
"BBBBBBBBBB  BBB   BBBBBBB",
"BBBBBBBBB    BB  BBBBBBBB",
"BB         BBBBBBB     BB",
"BB  BBBBBBBBBBBBB   BBBBB",
"BB                  BBBBB",
"BBBBBBB   BBBBBBBBBBBBBBB",
"BB   BBB  BBBB          B",
"BB        BBBBBBB  BBB  B",
"BBBB  BB           BBB  B",
"BBBB  BBBBBB  BBBBBBBB  B",
"B     BBB               B",
"BBB   BBBB  BBBBBBBBBBBBB",
"BBB   BBBB  BBBBBBBB   BB",
"BB                    BBB",
"BB  BBBBBBBBBBBBB   BBBBB",
"BB  BB              BB  B",
"BB  BB    BBBBBBBBBBBB  B",
"BB                     BB",
"BBBBBBBBBBBBBBBBBBBBBBBBB"
]


# List of Treasures
treasures = []

# Add maze to maze list
levels.append(level_1)
levels.append(level_2)

# Create level Setup Function
def setup_maze(level):
   
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == 'B':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == 'P':
                player.goto(screen_x, screen_y)

            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))

# Creating Pen object
pen = Pen()
player = Player()
walls = []

