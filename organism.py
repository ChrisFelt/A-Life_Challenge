import turtle
import math
import random
import numpy as np


def rand_dest(screen_size) -> list:
    """Returns a list containing random [x, y] coordinates"""
    return [random.uniform(-screen_size / 2, screen_size / 2),
            random.uniform(-screen_size / 2, screen_size / 2)]


class Organism:

    def __init__(self, identifier, position, destination, attributes):
        self._sprite = turtle.Turtle()
        self._identifier = identifier  # can set with child class once they're ready
        self._position = position
        self._destination = destination
        self._health = attributes["health"]
        self._vision = attributes["vision"]
        self._peripheral = attributes["peripheral"]
        self._speed = attributes["speed"]
        self._damage = attributes["damage"]
        self._separation_weight = attributes["separation_weight"]
        self._birth_rate = attributes["birth_rate"]
        self._mutation_rate = attributes["mutation_rate"]
        self._direction = self.__update_direction()  # set initial direction automatically

    def get_health(self):
        """Return current health"""
        return self._health

    def decrement_health(self, damage):
        """Decrement current health"""
        self._health -= damage

    def get_identifier(self):
        """Return organism identifier"""
        return self._identifier

    def set_pos(self, pos_coords):
        """Set new current position"""
        self._position = pos_coords

    def get_pos(self):
        """Return current position"""
        return self._position

    def get_dest(self):
        """Return current destination"""
        return self._destination

    def get_direction(self):
        """Return current direction"""
        return self._direction

    def set_dest(self, organisms, screen_size):
        """Set new destination and update direction"""
        neighbors = self.__nearest_neighbors(organisms)
        if not neighbors:
            # set random destination
            self._destination = rand_dest(screen_size)
        else:
            vector = self.__apply_behaviors(neighbors)
            # set new destination
            self._destination[0] = self._position[0] + vector[0]
            self._destination[1] = self._position[1] + vector[1]
            for coord in self._destination:
                if coord > screen_size / 2:
                    coord = screen_size / 2
                elif coord < -screen_size / 2:
                    coord = -screen_size / 2
        self._direction = self.__update_direction()

    def battle(self, organisms):
        """For neighbors of the opposing type, attack, reducing health by the damage value"""
        neighbors = self.__nearest_neighbors(organisms)
        for neighbor in neighbors:
            if self._identifier != neighbor.get_identifier():
                neighbor.decrement_health(self._damage)

    def is_fertile(self):
        if random.uniform(0, 1) < self._birth_rate:
            return True
        else:
            return False

    def reproduce(self):
        """Returns a new organism object with the attributes of the parent(self)"""
        attributes = {"health": self._health,
                      "vision": self._vision,
                      "peripheral": math.pi / 4,
                      "speed": self._speed,
                      "damage": self._damage,
                      "separation_weight": self._separation_weight,
                      "birth_rate": self._birth_rate,
                      "mutation_rate": self._mutation_rate
                      }
        return Organism(self._identifier, self._position, self._destination, attributes)

    def proximity_check(self, distance_to_check):
        """Returns True if Organism is within the given distance of the target destination"""
        # find the cartesian distance to target from current position
        distance = math.dist(self._position, self._destination)
        # return True if less than distance_to_check
        if distance < distance_to_check:
            return True
        else:
            return False

    def __apply_behaviors(self, neighbors):
        """A private method that returns the resultant movement vector based on behaviors"""
        vector = np.array([0, 0])
        for neighbor in neighbors:
            if self._identifier == 1 and neighbor.get_identifier() == 0:
                vector = np.add(vector, self.__hunt(neighbor))
            elif self._identifier == 0 and neighbor.get_identifier() == 0:
                vector = np.add(vector, self.__flock(neighbor))
            elif self._identifier == 0 and neighbor.get_identifier() == 1:
                vector = np.add(vector, self.__flee(neighbor))
            else:
                vector = np.add(vector, self.__separate(neighbor))
        return vector

    def __hunt(self, other):
        """Predators move toward neighboring prey"""
        direction = self.__direction_towards(other)
        return np.array([math.cos(direction) * self._speed, math.sin(direction) * self._speed])

    def __flock(self, other):
        """Prey move toward neighboring prey keeping separation"""
        if math.dist(other.get_pos(), self._position) > self._speed * self._separation_weight:
            direction = self.__direction_towards(other)
            return np.array([math.sin(direction) * self._speed, math.cos(direction) * self._speed])
        else:
            return np.array([0, 0])

    def __flee(self, other):
        """Prey move away from neighboring predators"""
        direction = self.__direction_towards(other) + math.pi
        return np.array([math.cos(direction) * self._speed, math.sin(direction) * self._speed])

    def __separate(self, other):
        """Predators keep minimum distance away from neighboring predators"""
        if math.dist(other.get_pos(), self._position) < self._speed * self._separation_weight:
            direction = self.__direction_towards(other) + math.pi
            return np.array([math.cos(direction) * self._speed, math.sin(direction) * self._speed])
        else:
            return np.array([0, 0])

    def __direction_towards(self, other):
        """Private method that returns a direction given CURRENT position and destination"""
        # atan2(destination y - current y, destination x - current x)
        return math.atan2(other.get_pos()[1] - self._position[1],
                          other.get_pos()[0] - self._position[0])

    def __update_direction(self):
        """Private method that returns a direction given CURRENT position and destination"""
        # atan2(destination y - current y, destination x - current x)
        return math.atan2(self._destination[1] - self._position[1],
                          self._destination[0] - self._position[0])

    def __nearest_neighbors(self, organisms):
        """Private method that returns a list of neighbors that are within vision"""
        neighbors = []
        vision_min = self._direction - self._peripheral
        vision_max = self._direction + self._peripheral
        for organism in organisms:
            if self is not organism and vision_min < self.__direction_towards(organism) < vision_max:
                if math.dist(self.get_pos(), organism.get_pos()) < self._vision:
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
