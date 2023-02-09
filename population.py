import csv


class Population:

    def __init__(self, predator_attributes, prey_attributes):
        self._generations = [[predator_attributes["population"], prey_attributes["population"]]]
        self._current_predator = predator_attributes["population"]
        self._current_prey = prey_attributes["population"]

    def add_organism(self, identifier):
        if identifier == 1:
            self._current_predator += 1
        else:
            self._current_prey += 1

    def remove_organism(self, identifier):
        if identifier == 1:
            self._current_predator -= 1
        else:
            self._current_prey -= 1

    def next_generation(self):
        self._generations.append([self._current_predator, self._current_prey])

    def log_population(self):
        with open('pop.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self._generations)
