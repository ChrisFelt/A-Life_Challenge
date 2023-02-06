import settings
import simulation_window
import organism


def set_target(index, organisms):
    """Step 1 of turn order.
    """
    # check if within range of target
    if organisms[index].proximity_check(settings.proximity):
        organisms[index].set_dest(organisms, settings.screen_size)
    pass


def move(index, organisms) -> None:
    """Step 2 of turn order.
    Animate movement of the Organism at the given index"""
    # clear shape, move turtle, and draw shape at new location
    organisms[index].clear()
    organisms[index].move(settings.slow_factor)
    organisms[index].draw_dot(settings.turtle_diameter)


def battle(index, organisms):
    """Step 3 of turn order.
    """
    organisms[index].battle(organisms)


def conclude_turn(index, organisms, screen):
    """Step 4 of turn order.
    index: current index of organisms
    index: list of Organism objects
    sim_screen: animation screen the Organism sprite will be drawn on
    """
    # remove an organism from the board if it reaches 0 health NOTE: untested!
    if organisms[index].is_dead():
        # clear organism animation and remove from list
        organisms[index].clear()
        organisms.pop(index)
        return False
    else:
        if organisms[index].is_fertile():
            identifier = organisms[index].get_identifier()
            pos = simulation_window.rand_coords()
            dest = simulation_window.rand_coords()
            simulation_window.create_organism(organisms, screen, identifier, pos, dest, organisms[index].get_attributes())
        return True
