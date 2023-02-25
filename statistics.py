import matplotlib.pyplot as plt
import numpy as np
import time


class Statistics:
    """Track interesting statistics for the current simulation session."""
    def __init__(self, predator_attributes, prey_attributes):
        self._predator_pop = []
        self._prey_pop = []
        self._avg_pred_lifespans = []
        self._avg_prey_lifespans = []
        self._predator = {"population": 0,
                          "births": -1 * predator_attributes["population"],
                          "deaths": 0,
                          "generation": 0,
                          "vision": 0,
                          "peripheral": 0,
                          "speed": 0,
                          "damage": 0,
                          "lifespan": 0
                          }
        self._prey = {"population": 0,
                      "births": -1 * prey_attributes["population"],
                      "deaths": 0,
                      "generation": 0,
                      "vision": 0,
                      "peripheral": 0,
                      "speed": 0,
                      "damage": 0,
                      "lifespan": 0
                      }
        self._general = {"turn": 0,
                         "gen_length": 100,
                         "elapsed_time": 0.00,
                         }
        self._start_time = time.time()

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

    def __stopwatch(self):
        """Updates the current elapsed time since start_time"""
        self._general["elapsed_time"] = time.time() - self._start_time

    def get_time_str(self):
        """Return elapsed time as a string truncated to two decimal places"""
        self.__stopwatch()
        return "{:.2f}".format(self._general["elapsed_time"])

    def reset_start_time(self):
        """Resets start time to current time adjusted by elapsed time.
        Use when loading a saved Statistics object!"""
        self._start_time = time.time() - self._general["elapsed_time"]

    def __add_pred_avg(self, keys, data):
        """Recomputes average attribute values for newly added predator"""
        for attribute in keys:
            self._predator[attribute] = (((self._predator["population"] - 1) * self._predator[attribute]) +
                                         data[attribute]) / self._predator["population"]

    def __add_prey_avg(self, keys, data):
        """Recomputes average attribute values for newly added prey"""
        for attribute in keys:
            self._prey[attribute] = (((self._prey["population"] - 1) * self._prey[attribute]) +
                                     data[attribute]) / self._prey["population"]

    def __rm_pred_avg(self, keys, data):
        """Recomputes average attribute values for newly added predator"""
        if self._predator["population"] > 0:
            for attribute in keys:
                self._predator[attribute] = (((self._predator["population"] + 1) * self._predator[attribute]) -
                                             data[attribute]) / self._predator["population"]

    def __rm_prey_avg(self, keys, data):
        """Recomputes average attribute values for newly added prey"""
        if self._prey["population"] > 0:
            for attribute in keys:
                self._prey[attribute] = (((self._prey["population"] - 1) * self._prey[attribute]) +
                                         data[attribute]) / self._prey["population"]

    def add_organism(self, attributes):
        """Increments the population size of the organism type corresponding to the identifier"""
        if attributes["identifier"] == 1:
            self._predator["population"] += 1
            self._predator["births"] += 1  # increment births too
            self.__add_pred_avg(["vision", "peripheral", "speed", "damage", "lifespan"], attributes)
        else:
            self._prey["population"] += 1
            self._prey["births"] += 1
            self.__add_prey_avg(["vision", "peripheral", "speed", "damage", "lifespan"], attributes)

    def remove_organism(self, attributes):
        """Decrements the population size of the organism type corresponding to the identifier"""
        if attributes["identifier"] == 1:
            self._predator["population"] -= 1
            self._predator["deaths"] += 1  # increment deaths too
            self.__rm_pred_avg(["vision", "peripheral", "speed", "damage", "lifespan"], attributes)
        else:
            self._prey["population"] -= 1
            self._prey["deaths"] += 1
            self.__rm_prey_avg(["vision", "peripheral", "speed", "damage", "lifespan"], attributes)

    def next_turn(self):
        """Stores data for the current generation"""
        self._general["turn"] += 1
        if self._general["turn"] % self._general["gen_length"] == 0:
            self._predator_pop.append(self._predator["population"])
            self._prey_pop.append((self._prey["population"]))
            self._avg_pred_lifespans.append(self._predator["lifespan"])
            self._avg_prey_lifespans.append(self._prey["lifespan"])

    def log_population(self):
        """Generates a graph of population data"""
        pred = np.array(self._predator_pop)
        pred_lifespan = np.array(self._avg_pred_lifespans)
        prey = np.array(self._prey_pop)
        prey_lifespan = np.array(self._avg_prey_lifespans)

        fig, (pop, lspan) = plt.subplots(2)
        pop.plot(pred, color='red', label='Predator')
        pop.plot(prey, color='green', label='Prey')
        lspan.plot(pred_lifespan, color='red', linestyle='dashed', label='Predator Lifespan')
        lspan.plot(prey_lifespan, color='green', linestyle='dashed', label='Prey Lifespan')
        pop.set(ylabel="Population Size")
        lspan.set(xlabel="Time (100 turns)", ylabel="Avg Lifespan")
        pop.legend()
        lspan.legend()
        plt.show()
