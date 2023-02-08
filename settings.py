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
                   "lifespan": 10,
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
                   "lifespan": 10,
                   "health": 3,
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

button_height = 2
button_width = 7
button_frame_height = 35

# tkinter widget padding
x_pad = 20
y_pad = 15
x_pad_left = (x_pad, 0)
x_pad_right = (0, x_pad)
x_pad_both = (x_pad, x_pad)
y_pad_top = (y_pad, 0)
y_pad_bot = (0, y_pad)
y_pad_both = (y_pad, y_pad)

