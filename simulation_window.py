import parameters_window
import settings
import organism
import simulation_steps
import turtle
import random
import tkinter

execute_steps = True
interrupt = False


def create_organism(organisms, screen, identifier, position, destination, attributes):
    """Create a new Organism class object with the given parameters and add it to organisms list"""
    organisms.append(organism.Organism(screen, identifier, position, destination, attributes))

    index = len(organisms) - 1
    organisms[index].hide_default()  # hide default arrow
    organisms[index].speed(10)
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


def initialize_organisms(organisms, screen, prey_attributes, pred_attributes):
    """Generate starting Organism objects for prey and predators"""
    # generate initial predator population
    for i in range(pred_attributes["population"]):
        create_organism(organisms, screen, 1, rand_coords(), rand_coords(), pred_attributes)

    # initial prey population
    for i in range(prey_attributes["population"]):
        create_organism(organisms, screen, 0, rand_coords(), rand_coords(), prey_attributes)


def steps(organisms, screen):
    global execute_steps
    # run all steps for each organism in the list
    i = 0
    while i < len(organisms):

        # step 1
        simulation_steps.set_target(i, organisms)

        # step 2
        simulation_steps.move(i, organisms)

        # step 3
        simulation_steps.battle(i, organisms)

        # step 4
        if simulation_steps.conclude_turn(i, organisms, screen):    # if organism hasn't died
            i += 1

    # skip until timer goes off again
    execute_steps = False


def change_to_simulation(canvas, organisms, prey_attributes, pred_attributes):
    """Build simulation screen and run the simulation"""
    global interrupt, execute_steps
    interrupt = False

    # remove any existing widgets
    for child in canvas.winfo_children():
        child.destroy()

    # basic frame canvas
    sim_canvas = tkinter.Canvas(canvas, width=settings.screen_size, height=settings.screen_size)
    sim_canvas.pack(side="top", anchor="nw")

    # setup turtle screen
    sim_screen = turtle.TurtleScreen(sim_canvas)
    sim_screen.tracer(0, 0)  # requires update method to be called on screen

    def quit_simulation():
        global interrupt

        # stop running simulation steps and reset variables
        # may need to check interrupt in each turn step (if steps are executed after next line of code, returns errors)
        interrupt = True
        sim_screen.resetscreen()  # DO NOT USE bye() - cannot restart turtle graphics after bye()
        organisms.clear()

        # swap back to parameters screen
        parameters_window.change_to_parameters(canvas, organisms, settings.prey_attributes, settings.pred_attributes)

    # control buttons frame
    bottom_frame = tkinter.Frame(canvas, width=settings.screen_size, height=settings.button_height)
    bottom_frame.pack(side="bottom", anchor="sw")

    # control buttons
    button = tkinter.Button(bottom_frame, text="Stop", command=quit_simulation)
    button.pack(side="bottom")

    # live stats frame
    side_frame = tkinter.Frame(canvas, width=900)
    side_frame.pack()

    def run_steps():
        """Timer function that sets the global boolean flag for turn_steps()"""
        global execute_steps
        execute_steps = True
        sim_screen.ontimer(run_steps, settings.timer)

    initialize_organisms(organisms, sim_screen, prey_attributes, pred_attributes)
    run_steps()

    # run simulation indefinitely
    while True:
        # exit simulation
        if interrupt:
            break

        # run steps according to timer
        if execute_steps:
            steps(organisms, sim_screen)
        sim_screen.update()
