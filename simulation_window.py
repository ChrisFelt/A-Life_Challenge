import parameters_window
import settings
import organism
import simulation_steps
import statistics
import turtle
import random
import tkinter
import time

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
        organisms[index].set_color(settings.pred_color)  # red

    # set color for prey
    else:
        organisms[index].set_color(settings.prey_color)  # green


def rand_coords():
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


def steps(organisms, session_stats, screen):
    """Run the turn steps for each organism"""
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
        if simulation_steps.conclude_turn(i, organisms, session_stats, screen):    # if organism hasn't died
            i += 1
    session_stats.next_turn()
    # skip until timer goes off again
    execute_steps = False


def plus_one(one_element_list):
    """Add one to the first element in the list. Great for lazy programmers :-)"""
    one_element_list[0] += 1
    return one_element_list[0]


def change_to_simulation(root, organisms, prey_attributes, pred_attributes):
    """Build simulation screen and run the simulation"""
    global interrupt, execute_steps, pause_simulation
    interrupt = False
    execute_steps = True
    pause_simulation = False
    current_row = [0]

    # track current session statistics
    session_stats = statistics.Statistics(pred_attributes, prey_attributes)

    # remove any existing widgets
    for child in root.winfo_children():
        child.destroy()

    root.config(pady=0, width=settings.screen_size*2)

    # -----------------------------------------------------------------------------
    # control buttons frame
    # -----------------------------------------------------------------------------
    button_frame = tkinter.Frame(root,
                                 width=settings.screen_size,
                                 height=settings.button_height,
                                 pady=settings.y_pad)
    button_frame.pack(side="bottom", anchor="sw")

    # -------------------------------
    # animation speed slider
    # -------------------------------
    def update_speed(event):
        """Update the simulation speed to reflect slider value"""
        # todo: figure out what event parameter contains
        print("Speed set to: " + str(speed_slider.get()) + ".")

    # speed slider
    speed_slider = tkinter.Scale(button_frame,
                                 command=update_speed,
                                 from_=1,
                                 to=50,
                                 label="Simulation Speed",
                                 showvalue=False,  # turn off current value display
                                 orient="horizontal",
                                 length=200,  # horizontal length of slider in pixels
                                 width=15)  # slider height in pixels
    speed_slider.pack(side="left", padx=(10, 100))

    # -------------------------------
    # pause button
    # -------------------------------
    def pause():
        """Pause simulation"""
        global interrupt
        global pause_simulation

        # toggle pause
        if not pause_simulation:
            pause_simulation = True
        else:
            pause_simulation = False

        # toggle button text
        if pause_text.get() == "Pause":
            pause_text.set("Resume")
        else:
            pause_text.set("Pause")

    # create pause button in button frame
    pause_text = tkinter.StringVar()
    pause_button = tkinter.Button(button_frame,
                                  textvariable=pause_text,
                                  command=pause,
                                  height=settings.button_height,
                                  width=settings.button_width)
    pause_button.pack(side="left")
    pause_text.set("Pause")

    # -------------------------------
    # save button
    # -------------------------------
    def save():
        """Save current simulation"""
        parameters_window.popup(root, "Error.\n\nSave feature not yet enabled.")

    # create save button
    save_button = tkinter.Button(button_frame,
                                 text="Save",
                                 command=save,
                                 height=settings.button_height,
                                 width=settings.button_width)
    save_button.pack(side="left")

    # -------------------------------
    # load button
    # -------------------------------
    def load():
        """Save current simulation"""
        parameters_window.popup(root, "Error.\n\nLoad feature not yet enabled.")

    # add load button to button frame
    load_button = tkinter.Button(button_frame,
                                 text="Load",
                                 command=load,
                                 height=settings.button_height,
                                 width=settings.button_width)
    load_button.pack(side="left")

    # -------------------------------
    # stop button
    # -------------------------------
    def quit_simulation():
        """Stop turtle animation and simulation turns, then switch to parameters window"""
        global interrupt

        # stop running simulation steps and reset variables
        # may need to check interrupt in each turn step (if steps are executed after next line of code, returns errors)
        interrupt = True
        sim_screen.resetscreen()  # DO NOT USE bye() - cannot restart turtle graphics after bye()
        organisms.clear()
        session_stats.log_population()

        # swap back to parameters window
        parameters_window.change_to_parameters(root, organisms, settings.prey_attributes, settings.pred_attributes)

    # add stop button to button frame
    stop_button = tkinter.Button(button_frame,
                                 text="Stop",
                                 command=quit_simulation,
                                 height=settings.button_height,
                                 width=settings.button_width)
    stop_button.pack(side="left", anchor="e", padx=(50, 0))

    # -----------------------------------------------------------------------------
    # sim screen frame
    # -----------------------------------------------------------------------------
    # basic canvas for screen
    sim_canvas = tkinter.Canvas(root,
                                width=settings.screen_size,
                                height=settings.screen_size,
                                highlightbackground="black",
                                highlightthickness=1)
    sim_canvas.pack(side="left", anchor="ne", padx=settings.x_pad//4, pady=settings.y_pad//3)

    # setup turtle screen
    sim_screen = turtle.TurtleScreen(sim_canvas)
    sim_screen.tracer(0, 0)  # requires update method to be called on screen

    # -----------------------------------------------------------------------------
    # live stats frame
    # -----------------------------------------------------------------------------
    side_frame = tkinter.Frame(root,
                               width=settings.screen_size//2,
                               highlightbackground="black",
                               highlightthickness=1)
    side_frame.pack(side="left", anchor="nw", padx=settings.x_pad//4, pady=settings.y_pad//3)

    # -------------------------------
    # window title
    # -------------------------------
    elapsed_time_label = tkinter.Label(side_frame,
                                       text="Session Statistics",
                                       font='Calibri 12 underline',
                                       height=2)
    elapsed_time_label.grid(row=plus_one(current_row),
                            column=0,
                            padx=settings.x_pad_right)

    # -------------------------------
    # total population
    # -------------------------------
    # population label
    tot_pop_label = tkinter.Label(side_frame, text="Total Population:")
    tot_pop_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show total population
    tot_pop_text = tkinter.StringVar(value=str(int(settings.prey_attributes["population"]) +
                                     int(settings.pred_attributes["population"])))
    tot_pop = tkinter.Label(side_frame, textvariable=tot_pop_text)
    tot_pop.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # turn number
    # -------------------------------
    # label
    turn_number_label = tkinter.Label(side_frame, text="Turn Number:")
    turn_number_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show turn number
    turn_number_text = tkinter.StringVar(value="0")
    turn_number = tkinter.Label(side_frame, textvariable=turn_number_text)
    turn_number.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # elapsed time
    # -------------------------------
    # label
    elapsed_time_label = tkinter.Label(side_frame, text="Time Elapsed:")
    elapsed_time_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show time
    start_time = time.time()
    # limit time display to two decimal places
    elapsed_time_text = tkinter.StringVar(value="{:.2f}".format(time.time() - start_time))
    elapsed_time = tkinter.Label(side_frame, textvariable=elapsed_time_text)
    elapsed_time.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # prey label
    # -------------------------------
    # prey label
    prey_label = tkinter.Label(side_frame, text="Prey", font='Calibri 11 underline')
    prey_label.grid(row=plus_one(current_row), column=0, sticky="w", pady=settings.y_pad_top)

    # -------------------------------
    # prey population
    # -------------------------------
    # prey population label
    prey_pop_label = tkinter.Label(side_frame, text="Population:")
    prey_pop_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show prey population
    prey_pop_text = tkinter.StringVar(value=settings.prey_attributes["population"])
    prey_pop = tkinter.Label(side_frame, textvariable=prey_pop_text)
    prey_pop.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # prey births
    # -------------------------------
    # prey births label
    prey_births_label = tkinter.Label(side_frame, text="Births:")
    prey_births_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show prey births
    prey_births_text = tkinter.StringVar(value="0")
    prey_births = tkinter.Label(side_frame, textvariable=prey_births_text)
    prey_births.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # prey deaths
    # -------------------------------
    # prey deaths label
    prey_deaths_label = tkinter.Label(side_frame, text="Deaths:")
    prey_deaths_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show prey deaths
    prey_deaths_text = tkinter.StringVar(value="0")
    prey_deaths = tkinter.Label(side_frame, textvariable=prey_deaths_text)
    prey_deaths.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # predator label
    # -------------------------------
    # predator label
    pred_label = tkinter.Label(side_frame, text="Predators", font='Calibri 11 underline')
    pred_label.grid(row=plus_one(current_row), column=0, sticky="w", pady=settings.y_pad_top)

    # -------------------------------
    # predator population
    # -------------------------------
    # predator population label
    pred_pop_label = tkinter.Label(side_frame, text="Population:")
    pred_pop_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show prey population
    pred_pop_text = tkinter.StringVar(value=settings.pred_attributes["population"])
    pred_pop = tkinter.Label(side_frame, textvariable=pred_pop_text)
    pred_pop.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # pred births
    # -------------------------------
    # predator births label
    pred_births_label = tkinter.Label(side_frame, text="Births:")
    pred_births_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show pred births
    pred_births_text = tkinter.StringVar(value="0")
    pred_births = tkinter.Label(side_frame, textvariable=pred_births_text)
    pred_births.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # pred deaths
    # -------------------------------
    # predator deaths label
    pred_deaths_label = tkinter.Label(side_frame, text="Deaths:")
    pred_deaths_label.grid(row=plus_one(current_row), column=0, sticky="w")

    # show pred deaths
    pred_deaths_text = tkinter.StringVar(value="0")
    pred_deaths = tkinter.Label(side_frame, textvariable=pred_deaths_text)
    pred_deaths.grid(row=current_row[0], column=1, sticky="w")

    # -------------------------------
    # blank row
    # -------------------------------
    # blank
    blank_row_label = tkinter.Label(side_frame, text="")
    blank_row_label.grid(row=plus_one(current_row), column=1, sticky="w", padx=settings.x_pad_right_super)

    def update_stats_frame(stats_object):
        """Update the values in the statistics frame"""
        pred_stats = stats_object.get_pred_stats()
        prey_stats = stats_object.get_prey_stats()
        general_stats = stats_object.get_general_stats()

        # update total population
        tot_pop_text.set(str(prey_stats["population"] + pred_stats["population"]))

        # update prey stats
        prey_pop_text.set(str(prey_stats["population"]))
        prey_births_text.set(str(prey_stats["births"]))
        prey_deaths_text.set(str(prey_stats["deaths"]))

        # update predator stats
        pred_pop_text.set(str(pred_stats["population"]))
        pred_births_text.set(str(pred_stats["births"]))
        pred_deaths_text.set(str(pred_stats["deaths"]))

        # update turn number
        turn_number_text.set(str(general_stats["turn"]))

        # update elapsed time
        elapsed_time_text.set("{:.2f}".format(time.time() - start_time))

    # -----------------------------------------------------------------------------
    # run simulation
    # -----------------------------------------------------------------------------
    def run_steps():
        """Timer function that sets the global boolean flag for steps()"""
        global execute_steps
        execute_steps = True
        sim_screen.ontimer(run_steps, settings.timer)

    initialize_organisms(organisms, sim_screen, prey_attributes, pred_attributes)
    run_steps()

    # run simulation indefinitely
    while True:
        # exit simulation when stop button pressed
        if interrupt:
            break

        # unless paused, run steps
        if not pause_simulation:

            if execute_steps:
                steps(organisms, session_stats, sim_screen)

            update_stats_frame(session_stats)

        # still need to update the screen even if paused
        # otherwise, program locks up
        sim_screen.update()
