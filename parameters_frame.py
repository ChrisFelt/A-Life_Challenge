from settings import *
from simulation_frame import *


def change_to_parameters(screen):
    """Build Parameters screen"""
    # remove any existing widgets
    for child in screen.winfo_children():
        child.destroy()

    # global variables
    global prey_population

    # basic frame canvas
    parameters_screen = tkinter.Frame(screen, width=frame_width, height=frame_height)
    parameters_screen.pack()

    # labels for text entry boxes
    prey_nostart_label = tkinter.Label(text="No. Start")
    prey_nostart_label.pack()

    # text entry boxes
    prey_nostart_entry = tkinter.Entry()
    prey_nostart_entry.insert(0, prey_population)
    prey_nostart_entry.pack()  # nostart_entry.get() pulls entry

    def start():
        prey_population = prey_nostart_entry.get()
        change_to_simulation(screen)

    start_button = tkinter.Button(root, text="Start", command=start)
    start_button.pack(side="bottom")
