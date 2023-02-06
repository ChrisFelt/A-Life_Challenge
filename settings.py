import math

# turtle specific globals
screen_size = 600
turtle_diameter = 10

slow_factor = 30  # controls global animation speed
timer = int(1000 // slow_factor)

# if within a given distance of their target destination, organism changes target
proximity = 10

# prey and predator general attributes
# *NOTE: these initial values show up as the DEFAULT in the parameters screen
prey_attributes = {"population": 70,
                   "health": 1,
                   "vision": 10,
                   "peripheral": math.pi / 4,
                   "speed": 10,
                   "damage": 1,
                   "separation_weight": 0.5,
                   "birth_rate": 0.001,
                   "mutation_rate": 0.5
                   }

pred_attributes = {"population": 30,
                   "health": 1,
                   "vision": 10,
                   "peripheral": math.pi / 2,
                   "speed": 10,
                   "damage": 2,
                   "separation_weight": 0.5,
                   "birth_rate": 0.001,
                   "mutation_rate": 0.5
                   }

# tkinter frame parameters
frame_height = screen_size + 10
frame_width = screen_size + 300
