from settings import *

def set_target(index):
    """Step 1 of turn order.
    """
    # check if within range of target
    if organisms[index].proximity_check(proximity):
        organisms[index].set_dest(organisms, screen_size)
    pass


def move(index, screen) -> None:
    """Step 2 of turn order.
    Animate movement of the Organism at the given index"""
    # clear shape, move turtle, and draw shape at new location
    organisms[index].clear()
    organisms[index].move(slow_factor)
    organisms[index].draw_dot(turtle_diameter)

    screen.update()  # refresh screen


def battle(index):
    """Step 3 of turn order.
    """
    pass


def conclude_turn(index, screen):
    """Step 4 of turn order.
    """
    # remove an organism from the board if it reaches 0 health NOTE: untested!
    if organisms[index].get_health() <= 0:
        # clear organism animation and remove from list
        organisms[index].clear()
        screen.update()
        organisms.pop(index)