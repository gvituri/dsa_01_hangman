import random

class Match():

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

    def __init__(self, dictionary):
        self.word = self.pick_random_word(dictionary)
        self.board = self.reset_board()

    def reset_board(self):
        return Match.board_states[0]

    def pick_random_word(self, dictionary):
        return dictionary[random.randint(0, (len(dictionary) - 1))].strip()

    def start_game(self):
        #game loop
        #display hang
        #display hidden word
        #ask for input
        #validate input
        #test input against word
        #call corresponding method
            #unvail leter
            #add body part
        #test if game is over
            #game is over on win
                #anounce victory
                #ask for rematch
            #game is over on death
                #anouce defeat
                #ask for rematch

def import_dictionary():
    with open("dictionary.txt", "rt") as file:
        dictionary = file.readlines()
        return dictionary

def main():
    dictionary = import_dictionary()
    print(dictionary)
    print(len(dictionary))
    match = Match(dictionary)
    match.start_game()

if __name__ == "__main__":
    main()