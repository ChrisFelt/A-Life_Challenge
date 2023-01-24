import turtle
import random
from organism import *

# global variables
screen_size = 600
population = 3
organisms = []

sim_screen = turtle.Screen()
sim_screen.setup(width=screen_size, height=screen_size)
turtle.hideturtle()  # don't need this?
turtle.speed(10)  # animation speed 1-10 (0 means no animation)
turtle.tracer(0, 0)  # requires update method to be called on screen

# prey general attributes
prey_health, prey_speed, prey_damage = 1, 1, 0
prey_separation_weight, prey_birth_rate, prey_mutation_rate = 0.5, 0.5, 0.5

# predator general attributes
pred_health, pred_speed, pred_damage = 1, 1, 1
pred_separation_weight, pred_birth_rate, pred_mutation_rate = 0.5, 0.5, 0.5


def new_organism(identifier, position, destination, health, speed, damage,
                 separation_weight, birth_rate, mutation_rate) -> None:
    """Create a new Organism class object with the given parameters and add it to organisms list"""
    organisms.append(Organism(identifier, position, destination, health, speed, damage, separation_weight,
                              birth_rate, mutation_rate))


def rand_coords() -> list:
    """Returns a random list containing [x, y] coordinates"""
    return [random.uniform(-screen_size, screen_size), random.uniform(-screen_size, screen_size)]


for i in range(population):

    if i % 2 == 0:
        # create prey
        new_organism(0, rand_coords, rand_coords, prey_health, prey_speed, prey_damage,
                     prey_separation_weight, prey_birth_rate, prey_mutation_rate)

    else:
        # create predator
        new_organism(0, rand_coords, rand_coords, pred_health, pred_speed, pred_damage,
                     pred_separation_weight, pred_birth_rate, pred_mutation_rate)

    organisms[i].get_sprite().hideturtle()  # hide default arrow
    organisms[i].get_sprite().up()  # don't draw line
    # todo: set colors


def move(index):
    organisms[index].get_sprite().clear()
    # todo: complete move method in Organism


while True:
    for i in range(population):
        move(i)
        sim_screen.update()
