import csv


class Statistics:

    def __init__(self, predator_attributes, prey_attributes):
        self._generations = [[predator_attributes["population"], prey_attributes["population"]]]
        self._predator = {"population": predator_attributes["population"],
                          "births": 0,
                          "deaths": 0,
                          }
        self._prey = {"population": prey_attributes["population"],
                      "births": 0,
                      "deaths": 0,
                      }
        self._general = {"turn": 0,
                         }

    def get_pred_stats(self):
        return self._predator

    def get_prey_stats(self):
        return self._prey

    def get_general_stats(self):
        return self._general

    def add_organism(self, identifier):
        """Increments the population size of the organism type corresponding to the identifier"""
        if identifier == 1:
            self._predator["population"] += 1
            self._predator["births"] += 1  # increment births too
        else:
            self._prey["population"] += 1
            self._prey["births"] += 1

    def remove_organism(self, identifier):
        """Decrements the population size of the organism type corresponding to the identifier"""
        if identifier == 1:
            self._predator["population"] -= 1
            self._predator["deaths"] += 1  # increment deaths too
        else:
            self._prey["population"] -= 1
            self._prey["deaths"] += 1

    def next_generation(self):
        """Stores data for the current generation"""
        self._generations.append([self._predator["population"], self._prey["population"]])
        self._general["turn"] += 1  # todo: resolve "generations" vs. "turns"

    def log_population(self):
        """Writes the simulation data to a csv file"""
        with open('stats.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self._generations)
