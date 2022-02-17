import random
import turtle
import sys
import time
import world.turtle.world as world
# import maze.obstacles as obsticals
import robot as robot
X = robot.position_x
Y = robot.position_y
direction =robot.current_direction_index

scr = turtle.getscreen()
scr.bgcolor("black")
scr.title("Ocean Floor")
scr.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.shapesize(1)
        self.penup()
        self.speed(0)

class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)


pen = Pen()
end = End()

floors = [""]
walls = []
finish = []

floor_1 = [
"xxxxxxxxxxxgxxxxxxxxxxxx",
"xxx            xx      x",
"xxx xxxxxxxxxx xx  xxx x",
"xxx xxx    xxx     xxx x",
"x   xxx xx xxxxxxx xxx x",
"x xxx   xx xx      xxx x",
"x xxxxxxxx xxxxxxxxxxx x",
"x     xxxx    xxxxx    x",
"xxxxx xxxxxxx x  xx    g",
"x xxx xxxxxxx x   x xxxx",
"x xx  xxxxxxx xxx x xxxx",
"x xx          xx xx xxxx",
"x xx  xxxxxx      x xxxx",
"x xxx xxxx     xxxx    x",
"x     xxxxxx xxxxxxxxx x",
"x xxxxxxxxxx    xxxxxx x",
"g     xxxxxxxxxx       x",
"xxx xxxxx      xx xxxxxx",
"xxx xxxxx xxxx xx xxxxxx",
"xxx xxxxx x    xx    xxx",
"xxx    x  x xxxxxxxx xxx",
"xx  xx x xx          xxx",
"x   x    xx xxxxxxxxxxxx",
"xxxxxxxxxxxgxxxxxxxxxxxx"
]

floors.append(floor_1)

def setup_maze(floors):
    for y in range (len(floors)):
        for x in range(len(floors[y])):
            character = floors[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "x":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            
            if character == "g":
                end.goto(screen_x,screen_y)
                end.stamp()
                finish.append((screen_x,screen_y))
            # if character == "p":
            #     player.goto(screen_x,screen_y)

setup_maze(floors[1])

# player = Player()
def mazerun(arg):
    end_x = 0
    end_y = 0
    print("starting maze run..")
    
    if arg == "top":
        end_x = -24
        end_y = 288
    elif arg == "right":
        end_x =264
        end_y =96
    elif arg == "left":
        end_x =-288
        end_y =-96
    elif arg == "bottom":
        end_x =-24
        end_y =-264
    else:
        end_x = -24
        end_y = 288

    while (robot.position_x,robot.position_y) != (end_x,end_y):
        spiritUp()
        spiritLeft()
        spiritDown()
        spiritRight()
        
# Y == Up and Down
# X == Left and Right

def spiritDown():
    global X,Y,direction
    if direction == 2:
        # x_walls = round(world.rec_bot.xcor(),0)
        # y_walls = round(world.rec_bot.xcor(),0)
        if  (X,Y) in finish:
            print("finished")
        if (X + 24, Y) in walls:
            if (X, Y - 24) not in walls:
                world.rec_bot.forward(24)
                Y = Y -24
                print("wall on left clear front")
            else:
                direction = 3
                world.rec_bot.right(90)
                print("front blocked")
        else:
            X = X + 24
            direction = 1
            world.rec_bot.left(90)
            world.rec_bot.forward(24)
            print("left clear")

def spiritLeft():
    global X,Y,direction
    if direction == 3:
        # x_walls = round(world.rec_bot.xcor(),0)
        # y_walls = round(world.rec_bot.xcor(),0)
        if  (X,Y) in finish:
            print("finished")
        if (X,Y + 24) in walls:
            if (X + 24, Y) not in walls:
                X = X -24
                world.rec_bot.forward (24)
                print("wall on left clear front")
            else:
                direction = 0
                world.rec_bot.right(90)
                print("left clear")
        else:
            direction = 2
            Y = Y -24
            world.rec_bot.left(90)
            world.rec_bot.forward(24)
            print("left clear")

def spiritUp():
    global X,Y,direction
    if direction == 0:
        # x_walls = round(world.rec_bot.xcor(),0)
        # y_walls = round(world.rec_bot.xcor(),0)
        if  (X, Y) in finish:
            print("finished")
        elif (X - 24, Y) in walls:
            if (X, Y + 24) not in walls:
                Y =Y +24
                world.rec_bot.forward (24)
                print("wall on left clear front")
            else:
                direction = 1
                world.rec_bot.right(90)
                print("front bloked")
        else:
            direction = 3
            X = X -24
            world.rec_bot.left(90)
            world.rec_bot.forward(24)
            print("left open")

def spiritRight():
    global X,Y,direction
    if direction == 1:
        # x_walls = round(world.rec_bot.xcor(),0)
        # y_walls = round(world.rec_bot.xcor(),0)
        if  (X, Y) in finish:
            print("finished")
        if (X, Y - 24) in walls:
            if (X - 24, Y) not in walls:
                X =X +24
                world.rec_bot.forward (24)
                print("wall on left clear front")
            else:
                direction = 2
                world.rec_bot.right(90)
                print("front blocked")
        else:
            direction = 0
            Y = Y +24
            world.rec_bot.left(90)
            world.rec_bot.forward(24)
            print("left open")



# while True:
#         world.spiritDown()
#         world.spiritLeft()
#         world.spiritUp()
#         world.spiritRight()

        # time.sleep(0.02)
        # break
# global list_of_obstacles
# list_of_obstacles = []


# def get_obstacles():
#     """
#         function randomly creates list with turlpe that has (x,y) coordinate - positions of obstacels
#         :return list_of_obstacles: a list with obstacels in the form (x,y) 
#     """
#     global list_of_obstacles

#     list_of_obstacles = [(random.randint(-100,100),random.randint(-200,200))\
#                     for i in range(0,random.randint(1,10))]

#     return list_of_obstacles


def is_position_blocked(x,y):
    """
        function checks if given position is blocked with an obstacle
        :param x: x coordinate
        :param y: y coordinate
        :return True/False : False if position is not blocked, true if it is
    """
    # global list_of_obstacles
    
    for each in walls:
        if x in range(each[0]-10, each[0]+10) and y in range(each[1]-10, each[1]+10):
            return True

    return False


# def check_greater(value1, value2):
#     """
#         returns smallest value first
#     """
#     if value1 > value2:
#         return value2, value1

#     return value1, value2


# def is_path_blocked(x1,y1, x2, y2):
#     """
#         return true if path is blocked
#         return false if path is not blocked
#     """
#     if y1 == y2:
#         x1, x2 = check_greater(x1, x2)
#         for x in range(x1, x2):
#             if is_position_blocked(x, y1):
#                 return True
#     else:
#         y1, y2 = check_greater(y1, y2)
#         for y in range(y1, y2):
#             if is_position_blocked(x1, y):
#                 return True
#     return False


# def show_obst():
#     """
#         returns list of created obst.
#     """
#     global list_of_obstacles

#     return list_of_obstacles