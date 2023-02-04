# turtle specific globals
screen_size = 600
turtle_diameter = 10
slow_factor = 20  # controls global animation speed
timer = 1000 // slow_factor

# if within a given distance of their target destination, organism changes target
proximity = 10

# prey and predator general attributes
# *NOTE: these initial values show up as the DEFAULT in the parameters screen
prey_attributes = {"population": 70,
                   "health": 1,
                   "vision": 10,
                   "speed": 10,
                   "damage": 1,
                   "separation_weight": 0.5,
                   "birth_rate": 0.5,
                   "mutation_rate": 0.5
                   }

pred_attributes = {"population": 30,
                   "health": 1,
                   "vision": 10,
                   "speed": 10,
                   "damage": 2,
                   "separation_weight": 0.5,
                   "birth_rate": 0.5,
                   "mutation_rate": 0.5
                   }

# tkinter frame parameters
frame_height = screen_size + 10
frame_width = screen_size + 200
