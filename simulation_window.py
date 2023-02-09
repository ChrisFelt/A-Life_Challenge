import parameters_window
import settings
import organism
import simulation_steps
import turtle
import random
import tkinter

execute_steps = True
interrupt = False
pause_simulation = False


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


def change_to_simulation(root, organisms, prey_attributes, pred_attributes):
    """Build simulation screen and run the simulation"""
    global interrupt, execute_steps, pause_simulation
    interrupt = False
    pause_simulation = False

    # remove any existing widgets
    for child in root.winfo_children():
        child.destroy()

    root.config(pady=0)

    # basic canvas for screen
    sim_canvas = tkinter.Canvas(root,
                                width=settings.screen_size,
                                height=settings.screen_size,
                                highlightbackground="black",
                                highlightthickness=1)
    sim_canvas.pack(side="top", anchor="nw", padx=settings.x_pad//4, pady=settings.y_pad//3)

    # setup turtle screen
    sim_screen = turtle.TurtleScreen(sim_canvas)
    sim_screen.tracer(0, 0)  # requires update method to be called on screen

    # control buttons frame
    button_frame = tkinter.Frame(root,
                                 width=settings.screen_size,
                                 height=settings.button_height,
                                 pady=settings.y_pad)
    button_frame.pack(side="bottom")

    def pause():
        """Pause simulation"""
        global interrupt
        global pause_simulation

        # toggle pause todo: fix with turtle.ontimer()
        #if not pause_simulation:
        #    pause_simulation = True
        #else:
        #    pause_simulation = False

        # toggle button text
        if pause_text.get() == "Pause":
            pause_text.set("Resume")
        else:
            pause_text.set("Pause")

    pause_text = tkinter.StringVar()
    pause_button = tkinter.Button(button_frame,
                                  textvariable=pause_text,
                                  command=pause,
                                  height=settings.button_height,
                                  width=settings.button_width)
    pause_button.pack(side="left")
    pause_text.set("Pause")

    def quit_simulation():
        global interrupt

        # stop running simulation steps and reset variables
        # may need to check interrupt in each turn step (if steps are executed after next line of code, returns errors)
        interrupt = True
        sim_screen.resetscreen()  # DO NOT USE bye() - cannot restart turtle graphics after bye()
        organisms.clear()

        # swap back to parameters screen
        parameters_window.change_to_parameters(root, organisms, settings.prey_attributes, settings.pred_attributes)

    # stop button
    stop_button = tkinter.Button(button_frame,
                                 text="Stop",
                                 command=quit_simulation,
                                 height=settings.button_height,
                                 width=settings.button_width)
    stop_button.pack(side="left")

    def save():
        """Save current simulation"""
        parameters_window.popup(root, "Error.\n\nSave feature not yet enabled.")

    save_button = tkinter.Button(button_frame,
                                 text="Save",
                                 command=save,
                                 height=settings.button_height,
                                 width=settings.button_width)
    save_button.pack(side="left")

    def load():
        """Save current simulation"""
        parameters_window.popup(root, "Error.\n\nLoad feature not yet enabled.")

    load_button = tkinter.Button(button_frame,
                                 text="Load",
                                 command=load,
                                 height=settings.button_height,
                                 width=settings.button_width)
    load_button.pack(side="left")

    # animation speed slider
    def update_speed(event):
        # todo: figure out what event parameter contains
        print("Speed set to: " + str(speed_slider.get()) + ".")

    # speed slider
    speed_slider = tkinter.Scale(button_frame,
                                 command=update_speed,
                                 from_=1,
                                 to=50,
                                 label="Animation Speed",
                                 orient="horizontal")
    speed_slider.pack()

    # live stats frame
    side_frame = tkinter.Frame(root, width=settings.screen_size*2)
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
