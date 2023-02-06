import tkinter
import settings
import simulation_window


def change_to_parameters(canvas, organisms, prey_attributes, pred_attributes):
    """Build Parameters screen"""
    # remove any existing widgets
    for child in canvas.winfo_children():
        child.destroy()

    # basic frame canvas
    param_screen = tkinter.Frame(canvas, width=settings.screen_size, height=settings.screen_size)
    param_screen.pack()

    # labels for text entry boxes
    prey_nostart_label = tkinter.Label(canvas, text="No. Start")
    prey_nostart_label.pack()

    # text entry boxes
    prey_nostart_entry = tkinter.Entry(canvas)
    prey_nostart_entry.insert(0, prey_attributes["population"])
    prey_nostart_entry.pack()

    def start():
        # grab input from entry fields
        try:
            prey_attributes["population"] = int(prey_nostart_entry.get())

        except ValueError:
            # todo: create popup window to notify user of error
            # todo: use flag to avoid executing subsequent lines
            print("Error. Please enter an integer.")

        # swap screens
        simulation_window.change_to_simulation(canvas, organisms, prey_attributes, pred_attributes)

    start_button = tkinter.Button(canvas, text="Start", command=start)
    start_button.pack(side="bottom")
