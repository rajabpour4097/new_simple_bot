


class BotState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.fib_levels = None
        self.first_touch = None
        self.second_touch = None
        self.fib0_time = None
        self.fib1_time = None
        # self.current_swing = False
