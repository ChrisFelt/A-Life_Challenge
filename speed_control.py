class SpeedControl:

    def __init__(self, general):
        self._slow_factor = general["slow_factor"]
        self._fast_forward = general["fast_forward"]

    def get_slow_factor(self):
        return self._slow_factor

    def set_fast_forward(self, value):
        self._fast_forward = value

    def get_fast_forward(self):
        return self._fast_forward

    def auto_adjust(self, population):
        """Adjusts slow_factor based on population parameter.
        Lower values -> faster movement speeds"""
        # with population as x and slow_factor as y, best fit line is:
        # y = 1271.2x^0.899
        # additionally adjust by fast-forward factor
        if population > 0:
            self._slow_factor = (1271.2 * population ** -0.899) / self._fast_forward
