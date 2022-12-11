from string import ascii_lowercase, ascii_uppercase

class day3:
    def __init__(self):
        self.priority_lookup = {}
        self.build_priority_lookup()
    def build_priority_lookup(self):
        priority = 1
        for c in ascii_lowercase:
            self.priority_lookup[c] = priority
            priority+=1
        for c in ascii_uppercase:
            self.priority_lookup[c] = priority
            priority+=1

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def part1(self):
        total_score = 0
        with open("input.txt", "r") as file:
            for rucksack in file.readlines():
                total_score+=self.priority_lookup[str("".join(list(set(self.intersection(rucksack[0:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):].strip())))))]
        print(total_score)

    def intersection_of_3(self, lst1, lst2, lst3):
        lst3 = [value for value in lst1 if value in lst2 and value in lst3]
        return lst3
    def part2(self):
        total_score = 0
        group_sacks = []
        with open("input.txt", "r") as file:
            for rucksack in file.readlines():
                group_sacks.append(rucksack)
                if len(group_sacks) == 3:
                    total_score += self.priority_lookup[str("".join(list(set(self.intersection_of_3(group_sacks[0], group_sacks[1], group_sacks[2].strip())))))]
                    group_sacks = []

        print(total_score)


if __name__ == '__main__':
    day3().part2()
