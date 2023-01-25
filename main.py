import turtle
import random
from organism import *

# global variables
screen_size = 600
population = 10
predator_prevalence = 3  # every nth organism is a predator when simulation starts
organisms = []

# turtle specific globals
turtle_diameter = 10
speed = 15
slow_factor = 300

# if within a given distance of their target destination, organism changes target
proximity = 10

# prey general attributes
prey_health, prey_speed, prey_damage = 1, 1, 0
prey_separation_weight, prey_birth_rate, prey_mutation_rate = 0.5, 0.5, 0.5

# predator general attributes
pred_health, pred_speed, pred_damage = 1, 1, 1
pred_separation_weight, pred_birth_rate, pred_mutation_rate = 0.5, 0.5, 0.5

# setup turtle
sim_screen = turtle.Screen()
sim_screen.setup(width=screen_size, height=screen_size)
turtle.hideturtle()  # don't need this?
turtle.speed(10)  # animation speed 1-10 (0 means no animation)
turtle.tracer(0, 0)  # requires update method to be called on screen


def new_organism(identifier, position, destination, health, speed, damage,
                 separation_weight, birth_rate, mutation_rate) -> None:
    """Create a new Organism class object with the given parameters and add it to organisms list"""
    organisms.append(Organism(identifier, position, destination, health, speed, damage, separation_weight,
                              birth_rate, mutation_rate))


def rand_coords() -> list:
    """Returns a random list containing [x, y] coordinates"""
    return [random.uniform(-screen_size/2, screen_size/2), random.uniform(-screen_size/2, screen_size/2)]


for i in range(population):

    if i % predator_prevalence == 0:
        # create predator
        new_organism(1, rand_coords(), rand_coords(), pred_health, pred_speed, pred_damage,
                     pred_separation_weight, pred_birth_rate, pred_mutation_rate)

    else:
        # create prey
        new_organism(0, rand_coords(), rand_coords(), prey_health, prey_speed, prey_damage,
                     prey_separation_weight, prey_birth_rate, prey_mutation_rate)

    organisms[i].hide_default()  # hide default arrow
    organisms[i].up()  # don't draw line
    # todo: set colors


def move(index):
    # clear shape, move turtle, and draw shape at new location
    organisms[index].clear()
    organisms[index].move(speed, slow_factor)
    organisms[index].draw_dot(turtle_diameter)

    # check if within range of target
    if organisms[index].proximity_check(proximity):
        organisms[index].set_dest(rand_coords())


while True:
    for i in range(population):
        move(i)
        sim_screen.update()
