import tkinter
import turtle

# turtle specific globals
screen_size = 600
turtle_diameter = 10
slow_factor = 200  # controls global animation speed

# global variables
pred_population = 3
prey_population = 7
organisms = []

# if within a given distance of their target destination, organism changes target
proximity = 10

# prey general attributes
prey_health, prey_vision, prey_speed, prey_damage = 1, 10, 10, 0
prey_separation_weight, prey_birth_rate, prey_mutation_rate = 0.5, 0.5, 0.5

# predator general attributes
pred_health, pred_vision, pred_speed, pred_damage = 1, 10, 10, 1
pred_separation_weight, pred_birth_rate, pred_mutation_rate = 0.5, 0.5, 0.5

# tkinter frame parameters
frame_height = screen_size + 10
frame_width = screen_size + 200

root = tkinter.Tk()
