import settings


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


def conclude_turn(index, organisms):
    """Step 4 of turn order.
    """
    # remove an organism from the board if it reaches 0 health NOTE: untested!
    if organisms[index].get_health() <= 0:
        # clear organism animation and remove from list
        organisms[index].clear()
        organisms.pop(index)
        return False
    else:
        return True
