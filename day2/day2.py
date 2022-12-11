class day2:
    def part1(self):
        total_score = 0
        with open("input2.txt", "r") as file:
            for line in file.readlines():
                current_game = line.split(" ")
                for i in range(0,len(current_game)):
                    current_game[i] = current_game[i].strip()

                game_score = self.calculate_game_score(current_game)
                tool_score = self.calculate_tool_score(current_game)

                total_score += game_score + tool_score
        print(total_score)

    def part2(self):
        total_score = 0
        with open("input2.txt", "r") as file:
            for line in file.readlines():
                current_game = line.split(" ")
                for i in range(0, len(current_game)):
                    current_game[i] = current_game[i].strip()
                current_game[1] = self.calculate_best_tool(current_game)
                game_score = self.calculate_game_score(current_game, translate_tool=False)
                tool_score = self.calculate_tool_score(current_game, translate_tool=False)

                total_score += game_score + tool_score
        print(total_score)

    def calculate_game_score(self, current_game, translate_tool=True):
        enemy = current_game[0]
        mine = self.translate_tool(current_game[1]) if translate_tool else current_game[1]
        if mine == enemy:
            return 3

        if (mine == "A" and enemy == "C") or (mine == "B" and enemy == "A") or (mine == "C" and enemy == "B"):
            return 6
        return 0


    def calculate_tool_score(self, current_game, translate_tool=True):
        tool = self.translate_tool(current_game[1]) if translate_tool else current_game[1]
        if tool == "A":
            return 1
        if tool == "B":
            return 2
        if tool == "C":
            return 3
        raise RuntimeError("Could not translate tool")

    def translate_tool(self, tool):
        if tool == "X":
            return "A"
        if tool == "Y":
            return "B"
        if tool == "Z":
            return "C"
        raise RuntimeError("Unable to translate tool")

    def calculate_best_tool(self, current_game):
        enemy = current_game[0]
        mine = current_game[1]
        if mine == "X":
            return self.find_tool(enemy, False)
        if mine == "Y":
            return enemy
        if mine == "Z":
            return self.find_tool(enemy, True)

    def find_tool(self, enemy, win):
        if enemy == "A":
            return "B" if win else "C"
        if enemy == "B":
            return "C" if win else "A"
        if enemy == "C":
            return "A" if win else "B"


if __name__ == '__main__':
    day2().part2()