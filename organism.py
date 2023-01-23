import turtle


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

    def set_pos(self):
        pass

    def get_pos(self):
        pass

    def set_dest(self):
        pass

    def get_dest(self):
        pass

    def get_sprite(self):
        return self._sprite

    def move(self):
        """Move towards destination"""
        pass

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
