import turtle
import random
from organism import *

# turtle specific globals
turtle_diameter = 10

# global variables
screen_size = 600
pred_population = 20
prey_population = 20
organisms = []

# prey general attributes
prey_health, pre_vision, prey_speed, prey_damage = 1, 10, 2, 0
prey_separation_weight, prey_birth_rate, prey_mutation_rate = 0.5, 0.5, 0.5

# predator general attributes
pred_health, pred_vision, pred_speed, pred_damage = 1, 30, 4, 1
pred_separation_weight, pred_birth_rate, pred_mutation_rate = 0.5, 0.5, 0.5

# setup turtle
sim_screen = turtle.Screen()
sim_screen.setup(width=screen_size, height=screen_size)
turtle.hideturtle()  # don't need this?
turtle.speed(10)  # animation speed 1-10 (0 means no animation)
turtle.tracer(0, 0)  # requires update method to be called on screen


def create_organism(identifier, position, destination, health, vision, speed, damage,
                    separation_weight, birth_rate, mutation_rate) -> None:
    """Create a new Organism class object with the given parameters and add it to organisms list"""
    organisms.append(Organism(identifier, position, destination, health, vision, speed, damage,
                              separation_weight, birth_rate, mutation_rate))

    index = len(organisms) - 1
    organisms[index].hide_default()  # hide default arrow
    organisms[index].up()  # don't draw line

    # set color for predator
    if identifier == 1:
        organisms[index].set_color("#de3f3c")  # red

    # set color for prey
    else:
        organisms[index].set_color("#68ed53")  # green


def rand_coords() -> list:
    """Returns a list containing random [x, y] coordinates"""
    return [random.uniform(-screen_size/2, screen_size/2),
            random.uniform(-screen_size/2, screen_size/2)]


def initialize_organisms() -> None:
    """Generate starting Organism objects for prey and predators"""
    # generate initial predator population
    for i in range(pred_population):
        create_organism(1, rand_coords(), rand_coords(), pred_health, pred_vision, pred_speed, pred_damage,
                        pred_separation_weight, pred_birth_rate, pred_mutation_rate)

    # initial prey population
    for i in range(prey_population):
        create_organism(0, rand_coords(), rand_coords(), prey_health, pre_vision, prey_speed, prey_damage,
                        prey_separation_weight, prey_birth_rate, prey_mutation_rate)


def set_target(index):
    """Step 1 of turn order.
    """
    organisms[index].set_dest(organisms)
    pass


def move(index) -> None:
    """Step 2 of turn order.
    Animate movement of the Organism at the given index"""
    # clear shape, move turtle, and draw shape at new location
    organisms[index].clear()
    organisms[index].move()
    organisms[index].draw_dot(turtle_diameter)

    sim_screen.update()  # refresh screen


def battle(index):
    """Step 3 of turn order.
    """
    pass


def conclude_turn(index):
    """Step 4 of turn order.
    """
    # remove an organism from the board if it reaches 0 health NOTE: untested!
    if organisms[index].get_health() <= 0:
        # clear organism animation and remove from list
        organisms[index].clear()
        sim_screen.update()
        organisms.pop(index)


if __name__ == "__main__":
    initialize_organisms()

    # play through infinite turns
    while True:
        for i in range(pred_population + prey_population):
            # step 1
            set_target(i)

            # step 2
            move(i)

            # step 3
            battle(i)

            # step 4
            conclude_turn(i)
