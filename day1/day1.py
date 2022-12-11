class day1:
    def __init__(self):
        self.highest_calories = []

    def process(self):
        current_total = 0
        with open("input2.txt", "r") as file:
            for line in file.readlines():
                if line.strip()=="":
                    self.highest_calories.append(current_total)
                    current_total = 0
                else:
                    current_total+=int(line.strip())
        self.highest_calories.append(current_total)
        self.highest_calories.sort(reverse=True)
        print(self.highest_calories)
        print(self.highest_calories[0]+self.highest_calories[1]+self.highest_calories[2])


if __name__ == '__main__':
    day1().process()