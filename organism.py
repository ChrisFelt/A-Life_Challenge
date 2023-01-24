import turtle
import math
import random


class Organism:

    def __init__(self, identifier, position, destination, direction, health, speed, damage,
                 separation_weight, birth_rate, mutation_rate):
        self._sprite = turtle.Turtle()
        self._identifier = identifier  # can set with child class once they're ready
        self._position = position
        self._destination = destination
        self._direction = direction
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

    def set_dest(self, destination):
        self._destination = destination

    def get_dest(self):
        return self._destination

    def set_direction(self, direction):
        self._direction = direction

    def get_direction(self):
        return self._direction

    def update_dest(self):
        """Set random direction to go to with a step size of speed"""
        self._direction = math.radians(random.randint(0, 360))
        self._destination[0] = self._position[0] + (math.sin(self._direction) * self._speed)
        self._destination[1] = self._position[1] + (math.cos(self._direction) * self._speed)

    def get_sprite(self):
        return self._sprite

    def move(self, organisms):
        """Move towards destination"""
        neighbors = self.nearest_neighbors(organisms)
        self._position = self._destination
        self.update_dest()

    def clear(self):
        """Remove circle"""
        pass

    def draw(self):
        """Draw circle on position"""
        pass

    def nearest_neighbors(self, organisms):
        neighbors = []
        for organism in organisms:
            if math.dist(organism.get_pos(), self.get_pos()) < 10 and self is not organism:
                neighbors.append(organism)
        return neighbors

class Predator(Organism):
    pass


class Prey(Organism):
    pass
