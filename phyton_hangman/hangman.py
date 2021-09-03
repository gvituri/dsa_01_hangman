import random

class Match():

    match_number = 0
    board_states = {
        0: [" ╒══╗ ",
            "    ║ ",
            "    ║ ",
            "    ║ ",
            "    ║ ",
            "════╩═"],
        1: [" ╒══╗ ",
            " O  ║ ",
            "    ║ ",
            "    ║ ",
            "    ║ ",
            "════╩═"],
        2: [" ╒══╗ ",
            " O  ║ ",
            " |  ║ ",
            "    ║ ",
            "    ║ ",
            "════╩═"],
        3: [" ╒══╗ ",
            " O  ║ ",
            "/|  ║ ",
            "    ║ ",
            "    ║ ",
            "════╩═"],
        4: [" ╒══╗ ",
            " O  ║ ",
            "/|\ ║ ",
            "    ║ ",
            "    ║ ",
            "════╩═"],
        5: [" ╒══╗ ",
            " O  ║ ",
            "/|\ ║ ",
            "/   ║ ",
            "    ║ ",
            "════╩═"],
        6: [" ╒══╗ ",
            " O  ║ ",
            "/|\ ║ ",
            "/ \ ║ ",
            "    ║ ",
            "════╩═"],
    }

    def __init__(self, word):
        self.word = word
        self.board = self.reset_board()

    def reset_board(self):
        return Match.board_states[0]

def import_dictionary():
    with open("dictionary.txt", "rt") as file:
        dictionary = file.readlines()
        return dictionary

def pick_random_word(dictionary):
    return dictionary[random.randint(0, len(dictionary))].strip()

def main():
    dictionary = import_dictionary()
    print(dictionary)
    word = pick_random_word(dictionary)
    print(word)
    match = Match(word)
    for line in match.board:
        print(line)

if __name__ == "__main__":
    main()