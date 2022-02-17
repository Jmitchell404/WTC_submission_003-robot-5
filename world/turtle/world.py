import sys
# from re import X
# import re
# from tkinter import Y
import turtle
import world
if "ocean" in sys.argv:
    import maze.ocean_floor as obstacles
else:
    import maze.obstacles as obstacles

# position_x = 0
# position_y = 0
# current_direction_index = 0
# min_y, max_y = -200, 200
# min_x, max_x = -100, 100
# current_direction_index = 0
# directions = ['forward', 'right', 'back', 'left']
# # list_of_obstacles = obstacles.get_obstacles()


"""
init the turtle
"""
#screen = turtle.Screen()
rec_bot = turtle.Turtle()
rec_bot.setheading(90)
rec_bot.color('lime')
rec_bot.shape('turtle')
rec_bot.shapesize(0.9)
rec_bot.penup()
# rec_bot = turtle.getscreen()
# rec_bot = turtle.Turtle()

# rec_bot.goto(-100,-200)
# rec_bot.pendown()

# for i in range(2):
#     rec_bot.forward(200)
#     rec_bot.left(90)
#     rec_bot.forward(400)
#     rec_bot.left(90)

# rec_bot.penup()
# rec_bot.goto(0,0)
# rec_bot.left(90)

# import maze.ocean_floor as obs
# obstacle_list = obs.get_obstacles()


    # turtle.mutant_ninja_turtle_robot = turtle.Turtle()
    #turtle_draw_constraints_box()
    #turtle_draw_obstacles(list_of_obst)
    #turtle_reset_and_center()
    #turtle.penup()

if "ocean" not in sys.argv:
    obs = turtle.Turtle()
    obs.penup()
    obs.left(90)
    obs.shape("square")
    obs.shapesize(10)

    for i in obstacles.get_obstacles():
        obs.goto(i[0], i[1])
        obs.stamp()


# draw_obs(obstacle_list)

# # def turtle_draw_constraints_box():
# #     """
# #         func draws the robots constraints box
# #     """
# #     # turtle.Turtle()
# #     # turtle.getscreen()
# #     # turtle.pendown()
# #     bon = turtle.Turtle()
# #     bon.goto(-100,200)
# #     bon.pencolor("red")
# #     bon.pensize(3)
# #     # turtle.pendown()
# #     bon.goto(100,200)
# #     bon.goto(100,-200)
# #     bon.goto(-100,-200)
# #     bon.goto(-100,200)
# #     bon.penup()


# def turtle_reset_and_center():
#     """
#         resets and recenters turtle
#     """
#     rec_bot.home()
    # rec_bot.left(90)


def turtle_turn_left():
    """
        make turle turn left
    """
    rec_bot.left(90)


def turtle_turn_right():
    """
        makes turtle turn right
    """
    rec_bot.right(90)


# # def draw_one_obstacle(x,y):
# #     """
# #         function draws one obstacle in turtle mode
# #     """
# #     # turtle.Turtle()
# #     # turtle.getscreen()
# #     obs = turtle.Turtle()
# #     obs.begin_fill()
# #     # turtle.pendown()
# #     obs.goto(x,y)
# #     obs.shape("square")
# #     obs.stamp()
# #     # obs.pendown()
# #     # obs.goto(x+4,y)
# #     # obs.goto(x+4,y+4)
# #     # obs.goto(x,y+4)
# #     # obs.goto(x,y)
# #     # obs.end_fill()
# #     # obs.penup()


# # def turtle_draw_obstacles(list_of_obst):
# #     """
# #         draws all obstacles one by one and resets turtle
# #     """
# #     for each in list_of_obst:
# #         draw_one_obstacle(each[0], each[1])


# def print_obstacles(list_of_obst):
#     pass
def print_obstacles(list_of_obst):
    pass



def show_position(robot_name, position_x, position_y):
    """
        moves turtle to given posistion
    """

    rec_bot.goto(position_x,position_y)


def is_position_allowed(new_x, new_y, position_x, position_y):
    """
    Checks if the new position will still fall within the max area limit
    """
    global min_x, max_x
    global min_y, max_y
    # area limit vars
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y,obstacles.is_path_blocked(position_x,position_y, new_x, new_y)


def update_position(steps, position_x, position_y, current_direction_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    """

    directions = ['forward', 'right', 'back', 'left']

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    zone_flag, obst_flag = is_position_allowed(new_x, new_y, position_x, position_y)
    if zone_flag and not obst_flag:
        return zone_flag, obst_flag, new_x, new_y
    return zone_flag, obst_flag, position_x, position_y