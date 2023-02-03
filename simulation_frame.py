import settings
import organism
import simulation_steps
import turtle
import random


def create_organism(organisms, identifier, position, destination, attributes):
    """Create a new Organism class object with the given parameters and add it to organisms list"""
    organisms.append(organism.Organism(identifier, position, destination, attributes))

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
    return [random.uniform(-settings.screen_size/2, settings.screen_size/2),
            random.uniform(-settings.screen_size/2, settings.screen_size/2)]


def initialize_organisms(organisms, prey_attributes, pred_attributes):
    """Generate starting Organism objects for prey and predators"""
    # generate initial predator population
    for i in range(pred_attributes["population"]):
        create_organism(organisms, 1, rand_coords(), rand_coords(), pred_attributes)

    # initial prey population
    for i in range(prey_attributes["population"]):
        create_organism(organisms, 0, rand_coords(), rand_coords(), prey_attributes)


def change_to_simulation(screen, organisms, prey_attributes, pred_attributes):

    # setup turtle
    sim_screen = turtle.Screen()
    sim_screen.setup(width=settings.screen_size, height=settings.screen_size)
    turtle.hideturtle()  # don't need this?
    turtle.speed(10)  # animation speed 1-10 (0 means no animation)
    turtle.tracer(0, 0)  # requires update method to be called on screen

    initialize_organisms(organisms, prey_attributes, pred_attributes)

    # play through infinite turns
    while True:
        for i in range(len(organisms)):
            # step 1
            simulation_steps.set_target(i, organisms)

            # step 2
            simulation_steps.move(i, organisms, sim_screen)

            # step 3
            simulation_steps.battle(i, organisms)

            # step 4
            simulation_steps.conclude_turn(i, organisms, sim_screen)
