import turtle
import random

sim_screen = turtle.Screen()
sim_screen.setup(width=600, height=600)
turtle.hideturtle()  # don't need this?
turtle.speed(10)  # animation speed 1-10 (0 means no animation)
turtle.tracer(0, 0)  # requires update method to be called on screen

population = 3
organisms = []
cur_x = []
cur_y = []
# tar_x = []
# tar_y = []

for i in range(population):
    organisms.append(turtle.Turtle())
    cur_x.append(random.uniform(-200, 200))
    cur_y.append(random.uniform(-200, 200))
    # tar_x.append(random.uniform(-200, 200))
    # tar_y.append(random.uniform(-200, 200))

    organisms[i].hideturtle()  # hide default arrow
    organisms[i].up()  # don't draw line


def move_ne(index):
    organisms[index].clear()
    cur_x[index] = 0.005 + cur_x[index]
    cur_y[index] = 0.005 + cur_y[index]
    organisms[index].goto(cur_y[index], cur_x[index])
    organisms[i].dot(10)  # draw a dot at current location


while True:
    for i in range(population):
        move_ne(i)
        sim_screen.update()
