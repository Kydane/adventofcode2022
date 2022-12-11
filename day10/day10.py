class day10:
    def __init__(self):
        self.cycle = 1
        self.x = 1
        self.signal_strength = 0
        self.current_row = []
        self.signal_checks = [20, 60, 100, 140, 180, 220]

    def read_input(self):
        commands = []
        with open("input.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('noop'):
                    commands.append(('noop',))
                if line.startswith('addx'):
                    commands.append(('addx', int(line.split(' ')[1].strip())))
        return commands

    def process_input(self, command):
        if command[0] == "noop":
            self.cycle = self.cycle+1
            self.draw_pixel()
        if command[0] == 'addx':
            self.cycle = self.cycle+1
            self.check_signal_strength()
            self.draw_pixel()
            self.cycle = self.cycle+1
            self.draw_pixel()
            self.x = (self.x + command[1])
        self.check_signal_strength()

    def check_signal_strength(self):
        if self.cycle in self.signal_checks:
            new_strength = self.cycle * self.x
            self.signal_strength = self.signal_strength + new_strength
            # Answer to Part 1
            print("X: " + str(self.x) + " ::: Cycle: " + str(self.cycle) + " ::: " + "Signal_Strength: " + str(new_strength) + " ::: Total Strength: "+str(self.signal_strength) )

    def draw_pixel(self, ):
        if self.x == len(self.current_row) or self.x+1 == len(self.current_row) or self.x-1 == len(self.current_row):
            self.current_row.append("#")
        else:
            self.current_row.append(".")

        if len(self.current_row) == 40:
            # Answer to Part 2
            # print("".join(self.current_row))
            self.current_row = []

    def process(self):
        for command in self.read_input():
            self.process_input(command)


if __name__ == '__main__':
    day10().process()

