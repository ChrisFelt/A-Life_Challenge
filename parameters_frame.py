import tkinter
import settings
import simulation_frame


def change_to_parameters(screen, organisms, prey_attributes, pred_attributes):
    """Build Parameters screen"""
    # remove any existing widgets
    for child in screen.winfo_children():
        child.destroy()

    # basic frame canvas
    parameters_screen = tkinter.Frame(screen, width=settings.frame_width, height=settings.frame_height)
    parameters_screen.pack()

    # labels for text entry boxes
    prey_nostart_label = tkinter.Label(text="No. Start")
    prey_nostart_label.pack()

    # text entry boxes
    prey_nostart_entry = tkinter.Entry()
    prey_nostart_entry.insert(0, prey_attributes["population"])
    prey_nostart_entry.pack()

    def start():
        # grab input from entry fields
        prey_attributes["population"] = int(prey_nostart_entry.get())

        # swap screens
        simulation_frame.change_to_simulation(screen, organisms, prey_attributes, pred_attributes)

    start_button = tkinter.Button(screen, text="Start", command=start)
    start_button.pack(side="bottom")
