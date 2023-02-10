import csv


class Statistics:

    def __init__(self, predator_attributes, prey_attributes):
        self._generations = [[predator_attributes["population"], prey_attributes["population"]]]
        self._current_predator = predator_attributes["population"]
        self._current_prey = prey_attributes["population"]

    def add_organism(self, identifier):
        """Increments the population size of the organism type corresponding to the identifier"""
        if identifier == 1:
            self._current_predator += 1
        else:
            self._current_prey += 1

    def remove_organism(self, identifier):
        """Decrements the population size of the organism type corresponding to the identifier"""
        if identifier == 1:
            self._current_predator -= 1
        else:
            self._current_prey -= 1

    def next_generation(self):
        """Stores data for the current generation"""
        self._generations.append([self._current_predator, self._current_prey])

    def log_population(self):
        """Writes the simulation data to a csv file"""
        with open('stats.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self._generations)
