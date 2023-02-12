import tkinter
import settings
import simulation_window


def popup(root, message):
    """Display a message as a popup notification above the root window"""
    popup_win = tkinter.Toplevel(root)

    display_message = tkinter.Label(popup_win, text=message)
    display_message.pack(padx=settings.x_pad_both, pady=settings.y_pad_both)
    close_win = tkinter.Button(popup_win,
                               text="OK",
                               command=popup_win.destroy,
                               height=settings.button_height,
                               width=settings.button_width)
    close_win.pack()


def change_to_parameters(root, organisms, prey_attributes, pred_attributes):
    """Build Parameters screen"""
    # remove any existing widgets
    for child in root.winfo_children():
        child.destroy()

    root.config(pady=settings.y_pad)

    # -----------------------------------------------------------------------------
    # PREY frame
    # -----------------------------------------------------------------------------
    prey_frame = tkinter.Frame(root,
                               width=settings.screen_size,
                               height=settings.screen_size/2,
                               highlightbackground=settings.prey_color,
                               highlightthickness=2)
    prey_frame.pack(side="top", anchor="n")

    prey_nostart_label = tkinter.Label(prey_frame,
                                       text="Prey Parameters",
                                       font='Calibri 12 underline',
                                       height=2)
    prey_nostart_label.grid(row=0, column=0, sticky="w", padx=settings.x_pad_left)

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

    # -----------------------------------------------------------------------------
    # pad frame
    # -----------------------------------------------------------------------------
    pad_frame_1 = tkinter.Frame(root, height=settings.button_frame_height)
    pad_frame_1.pack(side="top")

    # -----------------------------------------------------------------------------
    # PREDATOR frame
    # -----------------------------------------------------------------------------
    pred_frame = tkinter.Frame(root,
                               width=settings.screen_size,
                               height=settings.screen_size / 2,
                               highlightbackground=settings.pred_color,
                               highlightthickness=2)
    pred_frame.pack(side="top", anchor="n")

    pred_nostart_label = tkinter.Label(pred_frame,
                                       text="Predator Parameters",
                                       font='Calibri 12 underline',
                                       height=2)
    pred_nostart_label.grid(row=0, column=0, sticky="w", padx=settings.x_pad_left)

    # -------------------------------
    # labels for text entry boxes
    # -------------------------------
    # population
    pred_nostart_label = tkinter.Label(pred_frame, text="Population")
    pred_nostart_label.grid(row=1, column=0, sticky="w", padx=settings.x_pad_left)

    # health
    pred_health_label = tkinter.Label(pred_frame, text="Health")
    pred_health_label.grid(row=1, column=1, sticky="w")

    # speed
    pred_speed_label = tkinter.Label(pred_frame, text="Speed")
    pred_speed_label.grid(row=1, column=2, sticky="w")

    # damage
    pred_damage_label = tkinter.Label(pred_frame, text="Damage")
    pred_damage_label.grid(row=3, column=0, sticky="w", padx=settings.x_pad_left, pady=settings.y_pad_top)

    # birth rate
    pred_birth_rate_label = tkinter.Label(pred_frame, text="Birth Rate")
    pred_birth_rate_label.grid(row=3, column=1, sticky="w", pady=settings.y_pad_top)

    # mutation rate
    pred_mutation_rate_label = tkinter.Label(pred_frame, text="Mutation Rate")
    pred_mutation_rate_label.grid(row=3, column=2, sticky="w", pady=settings.y_pad_top)

    # -------------------------------
    # text entry boxes
    # -------------------------------
    # population
    pred_population_entry = tkinter.Entry(pred_frame)
    pred_population_entry.insert(0, pred_attributes["population"])
    pred_population_entry.grid(row=2, column=0, padx=settings.x_pad_both)

    # health
    pred_health_entry = tkinter.Entry(pred_frame)
    pred_health_entry.insert(0, pred_attributes["health"])
    pred_health_entry.grid(row=2, column=1, padx=settings.x_pad_right)

    # speed
    pred_speed_entry = tkinter.Entry(pred_frame)
    pred_speed_entry.insert(0, pred_attributes["speed"])
    pred_speed_entry.grid(row=2, column=2, padx=settings.x_pad_right)

    # damage
    pred_damage_entry = tkinter.Entry(pred_frame)
    pred_damage_entry.insert(0, pred_attributes["damage"])
    pred_damage_entry.grid(row=4, column=0, padx=settings.x_pad_both, pady=settings.y_pad_bot)

    # birth rate
    pred_birth_rate_entry = tkinter.Entry(pred_frame)
    pred_birth_rate_entry.insert(0, pred_attributes["birth_rate"])
    pred_birth_rate_entry.grid(row=4, column=1, padx=settings.x_pad_right, pady=settings.y_pad_bot)

    # mutation rate
    pred_mutation_rate_entry = tkinter.Entry(pred_frame)
    pred_mutation_rate_entry.insert(0, pred_attributes["mutation_rate"])
    pred_mutation_rate_entry.grid(row=4, column=2, padx=settings.x_pad_right, pady=settings.y_pad_bot)

    # -----------------------------------------------------------------------------
    # pad frame
    # -----------------------------------------------------------------------------
    pad_frame_1 = tkinter.Frame(root, height=settings.button_frame_height//2)
    pad_frame_1.pack(side="top", anchor="n")

    # -----------------------------------------------------------------------------
    # button frame
    # -----------------------------------------------------------------------------
    # create button frame
    button_frame = tkinter.Frame(root, width=settings.screen_size, height=settings.button_frame_height)
    button_frame.pack(side="top")

    # ------------------------------
    # start button
    # ------------------------------
    def start():
        """Get data from input fields and start simulation"""
        int_error = " error.\n\nPlease enter an integer."
        float_error = " error.\n\nPlease enter a float."

        # --------------------------------------
        # grab input from PREY entry fields todo: error check negative numbers
        # --------------------------------------
        # population
        try:
            prey_attributes["population"] = int(prey_population_entry.get())

        except ValueError:
            popup(root, "Prey population" + int_error)
            return

        # health
        try:
            prey_attributes["health"] = int(prey_health_entry.get())

        except ValueError:
            popup(root, "Prey health" + int_error)
            return

        # speed
        try:
            prey_attributes["speed"] = int(prey_speed_entry.get())

        except ValueError:
            popup(root, "Prey speed" + int_error)
            return

        # damage
        try:
            prey_attributes["damage"] = int(prey_damage_entry.get())

        except ValueError:
            popup(root, "Prey damage" + int_error)
            return

        # birth rate
        temp_birth_rate = prey_attributes["birth_rate"]
        try:
            prey_attributes["birth_rate"] = float(prey_birth_rate_entry.get())

        except ValueError:
            popup(root, "Prey birth rate" + float_error)
            return

        # check if birth rate is too high
        if prey_attributes["birth_rate"] > 0.01:
            prey_attributes["birth_rate"] = temp_birth_rate  # reset birth rate to previous
            popup(root, "Error.\n\nPrey birth rate must be <= 0.01.")
            return

        # population
        try:
            prey_attributes["mutation_rate"] = float(prey_mutation_rate_entry.get())

        except ValueError:
            popup(root, "Prey mutation rate" + float_error)
            return

        # --------------------------------------
        # grab input from PREDATOR entry fields
        # --------------------------------------
        # population
        try:
            pred_attributes["population"] = int(pred_population_entry.get())

        except ValueError:
            popup(root, "Predator population" + int_error)
            return

        # health
        try:
            pred_attributes["health"] = int(pred_health_entry.get())

        except ValueError:
            popup(root, "Predator health" + int_error)
            return

        # speed
        try:
            pred_attributes["speed"] = int(pred_speed_entry.get())

        except ValueError:
            popup(root, "Predator speed" + int_error)
            return

        # damage
        try:
            pred_attributes["damage"] = int(pred_damage_entry.get())

        except ValueError:
            popup(root, "Predator damage" + int_error)
            return

        # birth rate
        temp_birth_rate = pred_attributes["birth_rate"]
        try:
            pred_attributes["birth_rate"] = float(pred_birth_rate_entry.get())

        except ValueError:
            popup(root, "Predator birth rate" + float_error)
            return

        # check if birth rate is too high
        if pred_attributes["birth_rate"] > 0.01:
            pred_attributes["birth_rate"] = temp_birth_rate  # reset birth rate to previous
            popup(root, "Error.\n\nPredator birth rate must be <= 0.01.")
            return

        # population
        try:
            pred_attributes["mutation_rate"] = float(pred_mutation_rate_entry.get())

        except ValueError:
            popup(root, "Predator mutation rate" + float_error)
            return

        # ------------------------------
        # change to simulation screen
        # ------------------------------
        simulation_window.change_to_simulation(root, organisms, prey_attributes, pred_attributes)

    start_button = tkinter.Button(button_frame,
                                  text="Start",
                                  command=start,
                                  height=settings.button_height,
                                  width=settings.button_width)
    start_button.pack(side="left")

    # ------------------------------
    # load button
    # ------------------------------
    def load():
        """Load simulation from save file"""
        popup(root, "Error.\n\nLoad feature not yet enabled.")

    load_button = tkinter.Button(button_frame,
                                 text="Load",
                                 command=load,
                                 height=settings.button_height,
                                 width=settings.button_width)
    load_button.pack(side="left")
