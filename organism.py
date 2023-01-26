import turtle
import math
import random
import numpy as np


class Organism:

    def __init__(self, identifier, position, destination, health, vision, speed, damage,
                 separation_weight, birth_rate, mutation_rate):
        self._sprite = turtle.Turtle()
        self._identifier = identifier  # can set with child class once they're ready
        self._position = position
        self._destination = destination
        self._health = health
        self._vision = vision
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

    def get_identifier(self):
        """Return organism identifier"""
        return self._identifier

    def set_pos(self, pos_coords):
        """Set new current position"""
        self._position = pos_coords

    def get_pos(self):
        """Return current position"""
        return self._position

    def __hunt(self, other):
        """Predators move toward neighboring prey"""
        return np.array([other.get_pos[0] - self._position[0], other.get_pos[1] - self._position[1]])

    def __flock(self, other):
        """Prey move toward neighboring prey keeping separation"""
        return np.array([(other.get_pos[0] - self._position[0])/2, (other.get_pos[1] - self._position[1])/2])

    def set_dest(self, organisms):
        """Set new destination and update direction"""
        # identify neighbors
        vector = np.array([0, 0])
        neighbors = self.__nearest_neighbors(organisms)
        if not neighbors:
            vector += np.array([random.randint(-1 * self._speed, self._speed), random.randint(-1 * self._speed, self._speed)])
        else:
            for neighbor in neighbors:
                if self._identifier == 1 and neighbor.get_identifier == 0:
                    vector += self.__hunt(neighbor)
                elif self._identifier == 0 and neighbor.get_identifier == 0:
                    vector += self.__flock(neighbor)
        # set new destination
        self._destination[0] = self._position[0] + vector[0]
        self._destination[1] = self._position[1] + vector[1]

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

    def __nearest_neighbors(self, organisms):
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

    def move(self):
        """Move organism towards destination"""
        # slow_factor reduces distance moved and makes the animation smoother
        self._position[0] = self._destination[0]
        self._position[1] = self._destination[1]

        self._sprite.goto(self._position[0], self._position[1])


class Predator(Organism):
    pass


class Prey(Organism):
    pass
