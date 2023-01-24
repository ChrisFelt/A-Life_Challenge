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

    def set_pos(self, position):
        self._position = position

    def get_pos(self):
        return self._position

    def set_dest(self):
        """Set random direction to go to with a step size of speed"""
        direction = math.radians(random.randint(0, 360))
        self._destination[0] = self._position[0] + (math.sin(direction) * self._speed)
        self._destination[1] = self._position[1] + (math.cos(direction) * self._speed)

    def get_dest(self):
        return self._destination

    def get_sprite(self):
        return self._sprite

    def move(self):
        """Move towards destination"""
        self._position = self._destination
        self.set_dest()

    def clear(self):
        """Remove circle"""
        pass

    def draw(self):
        """Draw circle on position"""
        pass


class Predator(Organism):
    pass


class Prey(Organism):
    pass
