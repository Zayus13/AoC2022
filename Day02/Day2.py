win = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
lose = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}


def a_to_x(c):
    return chr(ord(c) - ord("A") + ord("X"))


def score_per_round(opponent, selection):
    opponent = a_to_x(opponent)
    score = 0
    if win[selection] == opponent:
        score = 6
    elif selection == opponent:
        score = 3
    score = score + (ord(selection) - ord('X') + 1)
    return score


def get_outcome(opponent, outcome):
    if outcome == "Y":
        return score_per_round(opponent, a_to_x(opponent))
    elif outcome == "X":
        return score_per_round(opponent, win[a_to_x(opponent)])
    else:
        return score_per_round(opponent, lose[a_to_x(opponent)])


if __name__ == '__main__':
    with open("day02.txt", "r") as f:
        data = f.readlines()
        result = sum([score_per_round(*line.split()) for line in data])
        result2 = sum([get_outcome(*line.split()) for line in data])
        print(result)
        print(result2)