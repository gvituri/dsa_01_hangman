import random

class Match():

    hang_states = {
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
        self.hidden_word = self.hide_word()
        self.played_leters = ""
        self.hang = self.reset_hang()

    def pick_random_word(self, dictionary):
        return list(dictionary[random.randint(0, (len(dictionary) - 1))].strip())

    def hide_word(self):
        hidden_word = ""
        for leter in range(len(self.word)):
            hidden_word += "_"
        return list(hidden_word)

    def reset_hang(self):
        return 0

    def start_game(self):
        while True:
            self.display_hang()
            self.display_hidden_word()
            self.display_played_leters()
            player_guess = self.ask_for_leter()
            self.played_leters += player_guess
            self.check_guess(player_guess)
        '''#game loop
        #call corresponding method
            #unvail leter
            #add body part
        #test if game is over
            #game is over on win
                #anounce victory
                #ask for rematch
            #game is over on death
                #anouce defeat
                #ask for remtch'''

    def display_hang(self):
        for line in Match.hang_states[self.hang]:
            print(line)

    def display_hidden_word(self):
        print("".join(self.hidden_word))

    def display_played_leters(self):
        print("Played leters:")
        for i in range(len(self.played_leters)):
            print("%s" % (str(self.played_leters[i])), end=" ")
        print()

    def ask_for_leter(self):
        while True:
            try:
                player_guess = input("Enter your leter guess: ").lower()
                if not self.validate_input(player_guess):
                    raise
                break
            except:
                print("ERROR! Invalid input.")

        return player_guess

    def validate_input(self, player_input):
        if len(player_input) == 1 and ord(player_input) in range(97, 123) \
                and player_input not in self.played_leters:
            return True
        return False

    def check_guess(self, player_guess):
        try:
            self.word.index(player_guess)
            self.right_guess(player_guess)
        except ValueError:
            self.wrong_guess(player_guess)

    def right_guess(self, player_guess):
        print("Correct Guess!")
        while True:
            try:
                char_index = self.word.index(player_guess)
                self.word[char_index] = "*"
                self.hidden_word[char_index] = player_guess
            except ValueError:
                break

    def wrong_guess(self, player_guess):
        print("Wrong Guess!")
        self.hang += 1

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