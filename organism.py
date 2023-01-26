import turtle
import math
import random


class Organism:

    def __init__(self, identifier, position, destination, health, speed, damage,
                 separation_weight, birth_rate, mutation_rate):
        self._sprite = turtle.Turtle()
        self._identifier = identifier  # can set with child class once they're ready
        self._position = position
        self._destination = destination
        self._health = health
        self._speed = speed
        self._damage = damage
        self._separation_weight = separation_weight
        self._birth_rate = birth_rate
        self._mutation_rate = mutation_rate
        self._direction = None

        # set initial direction automatically
        self.__update_direction()

    def get_health(self):
        """Return current health"""
        return self._health

    def set_pos(self, pos_coords):
        """Set new current position"""
        self._position = pos_coords

    def get_pos(self):
        """Return current position"""
        return self._position

    def set_dest(self, dest_coords):
        """Set new destination and update direction"""
        # set new destination
        self._destination[0] = dest_coords[0]
        self._destination[1] = dest_coords[1]

        # update direction
        self.__update_direction()

    def get_dest(self):
        return self._destination

    def get_direction(self):
        return self._direction

    def __update_direction(self):
        """Private method that updates direction given CURRENT position and destination"""
        # atan2(destination y - current y, destination x - current x)
        self._direction = math.atan2(self._destination[1] - self._position[1],
                                     self._destination[0] - self._position[0])

    def proximity_check(self, distance_to_check):
        """Returns True if Organism is within the given distance of the target destination"""
        # find the cartesian distance to target from current position
        x_proximity = (self._destination[0] - self._position[0]) ** 2
        y_proximity = (self._destination[1] - self._position[1]) ** 2
        distance = math.sqrt(x_proximity + y_proximity)

        # return True if less than distance_to_check
        if distance < distance_to_check:
            return True

        else:
            return False

    def nearest_neighbors(self, organisms):
        neighbors = []
        for organism in organisms:
            if math.dist(organism.get_pos(), self.get_pos()) < 10 and self is not organism:
                neighbors.append(organism)
        return neighbors

    # ---------------------------------
    # Turtle commands
    # ---------------------------------

    def hide_default(self):
        """Hide default turtle arrow"""
        self._sprite.hideturtle()

    def up(self):
        """No lines are drawn when turtle moves"""
        self._sprite.up()

    def clear(self):
        """Clear shape"""
        self._sprite.clear()

    def draw_dot(self, diameter):
        """Draw circle on position given diameter"""
        self._sprite.dot(diameter)

    def set_color(self, color):
        """Set turtle color to the given string.
        Accepts color names ("red", "blue", etc.) or RGB hex values ("#FFFFFF")"""
        self._sprite.color(color)

    def move(self, slow_factor):
        """Move organism towards destination"""
        # slow_factor reduces distance moved and makes the animation smoother
        self._position[0] += self._speed / slow_factor * math.cos(self._direction)
        self._position[1] += self._speed / slow_factor * math.sin(self._direction)

        self._sprite.goto(self._position[0], self._position[1])


class Predator(Organism):
    pass


class Prey(Organism):
    pass
