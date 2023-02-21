import math

# turtle specific globals
screen_size = 600
timer = int(1000 // 30)

turtle_settings = {"diameter": 10,
                   "speed": 10,
                   "slow_factor": 30,
                   }

# if within a given distance of their target destination, organism changes target
proximity = 40

# tkinter frame parameters
button_height = 2
button_width = 7
button_frame_height = 35

# tkinter widget padding
x_pad = 20
y_pad = 15
x_pad_left = (x_pad, 0)
x_pad_left_super = (x_pad*10, 0)
x_pad_right = (0, x_pad)
x_pad_right_super = (0, x_pad*10)
x_pad_both = (x_pad, x_pad)
y_pad_top = (y_pad, 0)
y_pad_bot = (0, y_pad)
y_pad_both = (y_pad, y_pad)

# prey and predator colors
prey_color = "#68ed53"
pred_color = "#de3f3c"

# prey and predator general attributes
# *NOTE: these initial values show up as the DEFAULT in the parameters screen
prey_attributes = {"population": 80,
                   "generation": 0,
                   "lifespan": 4,
                   "health": 1,
                   "vision": 10,
                   "peripheral": math.pi / 4,
                   "speed": 10,
                   "damage": 0,
                   "separation_weight": 0.5,
                   "birth_rate": 0.002,
                   "mutation_rate": 0.25
                   }

pred_attributes = {"population": 20,
                   "generation": 0,
                   "lifespan": 5,
                   "health": 2,
                   "vision": 30,
                   "peripheral": math.pi / 2,
                   "speed": 12,
                   "damage": 1,
                   "separation_weight": 0.5,
                   "birth_rate": 0.01,
                   "mutation_rate": 0.25
                   }
