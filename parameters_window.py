import tkinter
import settings
import simulation_window


def change_to_parameters(canvas, organisms, prey_attributes, pred_attributes):
    """Build Parameters screen"""
    # remove any existing widgets
    for child in canvas.winfo_children():
        child.destroy()

    # -----------------------------------------------------------------------------
    # prey frame
    # -----------------------------------------------------------------------------
    prey_frame = tkinter.Frame(canvas,
                               width=settings.screen_size,
                               height=settings.screen_size/2,
                               highlightbackground="#68ed53",
                               highlightthickness=2)
    prey_frame.pack(side="top")

    prey_nostart_label = tkinter.Label(prey_frame, text="Prey Parameters", font=('Calibri 12 underline'), height=2)
    prey_nostart_label.grid(row=0, column=0)

    # -------------------------------
    # labels for text entry boxes
    # -------------------------------
    # population
    prey_nostart_label = tkinter.Label(prey_frame, text="Population")
    prey_nostart_label.grid(row=1, column=0, sticky="w", padx=settings.x_pad_left)

    # health
    prey_health_label = tkinter.Label(prey_frame, text="Health")
    prey_health_label.grid(row=1, column=1, sticky="w")

    # speed
    prey_speed_label = tkinter.Label(prey_frame, text="Speed")
    prey_speed_label.grid(row=1, column=2, sticky="w")

    # damage
    prey_damage_label = tkinter.Label(prey_frame, text="Damage")
    prey_damage_label.grid(row=3, column=0, sticky="w", padx=settings.x_pad_left, pady=settings.y_pad_top)

    # birth rate
    prey_birth_rate_label = tkinter.Label(prey_frame, text="Birth Rate")
    prey_birth_rate_label.grid(row=3, column=1, sticky="w", pady=settings.y_pad_top)

    # mutation rate
    prey_mutation_rate_label = tkinter.Label(prey_frame, text="Mutation Rate")
    prey_mutation_rate_label.grid(row=3, column=2, sticky="w", pady=settings.y_pad_top)

    # -------------------------------
    # text entry boxes
    # -------------------------------
    # population
    prey_population_entry = tkinter.Entry(prey_frame)
    prey_population_entry.insert(0, prey_attributes["population"])
    prey_population_entry.grid(row=2, column=0, padx=settings.x_pad_both)

    # health
    prey_health_entry = tkinter.Entry(prey_frame)
    prey_health_entry.insert(0, prey_attributes["health"])
    prey_health_entry.grid(row=2, column=1, padx=settings.x_pad_right)

    # speed
    prey_speed_entry = tkinter.Entry(prey_frame)
    prey_speed_entry.insert(0, prey_attributes["speed"])
    prey_speed_entry.grid(row=2, column=2, padx=settings.x_pad_right)

    # damage
    prey_damage_entry = tkinter.Entry(prey_frame)
    prey_damage_entry.insert(0, prey_attributes["damage"])
    prey_damage_entry.grid(row=4, column=0, padx=settings.x_pad_both, pady=settings.y_pad_bot)

    # birth rate
    prey_birth_rate_entry = tkinter.Entry(prey_frame)
    prey_birth_rate_entry.insert(0, prey_attributes["birth_rate"])
    prey_birth_rate_entry.grid(row=4, column=1, padx=settings.x_pad_right, pady=settings.y_pad_bot)

    # mutation rate
    prey_mutation_rate_entry = tkinter.Entry(prey_frame)
    prey_mutation_rate_entry.insert(0, prey_attributes["mutation_rate"])
    prey_mutation_rate_entry.grid(row=4, column=2, padx=settings.x_pad_right, pady=settings.y_pad_bot)

    def start():
        # grab input from entry fields
        try:
            prey_attributes["population"] = int(prey_population_entry.get())

        except ValueError:
            # todo: create popup window to notify user of error
            # todo: use flag to avoid executing subsequent lines
            print("Error. Please enter an integer.")

        # swap screens
        simulation_window.change_to_simulation(canvas, organisms, prey_attributes, pred_attributes)

    button_frame = tkinter.Frame(canvas, width=settings.screen_size, height=settings.button_height)
    button_frame.pack(side="top", anchor="sw")

    start_button = tkinter.Button(button_frame, text="Start", command=start)
    start_button.pack(side="bottom")
