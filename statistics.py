import matplotlib.pyplot as plt
import numpy as np


class Statistics:

    def __init__(self, predator_attributes, prey_attributes):
        self._predator_pop = []
        self._prey_pop = []
        self._predator = {"population": predator_attributes["population"],
                          "births": 0,
                          "deaths": 0,
                          "generation": 0,
                          }
        self._prey = {"population": prey_attributes["population"],
                      "births": 0,
                      "deaths": 0,
                      "generation": 0,
                      }
        self._general = {"turn": 0,
                         "gen_length": min(1/predator_attributes["birth_rate"], 1/prey_attributes["birth_rate"]),
                         }

    def get_pred_stats(self):
        return self._predator

    def get_prey_stats(self):
        return self._prey

    def get_general_stats(self):
        return self._general

    def get_generation(self, identifier):
        """Given an identifier, returns the corresponding organism's generation"""
        if identifier == 1:
            return self._predator["generation"]
        else:
            return self._prey["generation"]

    def set_generation(self, identifier, generation_num):
        """Given an identifier and generation, updates the corresponding organism's generation"""
        if identifier == 1:
            self._predator["generation"] = generation_num
        else:
            self._prey["generation"] = generation_num

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

    def next_turn(self):
        """Stores data for the current generation"""
        self._general["turn"] += 1
        if self._general["turn"] % self._general["gen_length"] == 0:
            self._predator_pop.append(self._predator["population"])
            self._prey_pop.append((self._prey["population"]))

    def log_population(self):
        """Writes the simulation data to a csv file"""
        pred = np.array(self._predator_pop)
        prey = np.array(self._prey_pop)

        plt.plot(pred, color='red', label='Predator')
        plt.plot(prey, color='green', label='Prey')
        plt.xlabel("Generation")
        plt.ylabel("Population Size")
        plt.legend()
        plt.show()
