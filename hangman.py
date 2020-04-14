# this is the hangman game
import csv
from random import choice
from collections import Counter, defaultdict


class Hangman:
    """ This manages the hangman game class. """

    def __init__(self):
        """ This initializes the hangman class. """

        self.game_active = True

        self.alphabets = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        self.words = []

        with open("/home/oladipo/python_work/hangman_python/words.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                if len(line["word"]) == 6:
                    self.words.append(line["word"])

        # print(words)
        self.word = choice(self.words)
        # print(word)
        # print("c h o s e n")
        # print("_ _ _ _ _ _")
        self.num_guesses = 6
        print("This is hangman.")
        self.given_letters = []
        self.word_list = []
        # self.word_dict = {}
        self.word_dict = defaultdict(int)
        for letter in self.word:
            self.word_list.append(letter)
            # word_dict[f'{letter}'] =

        # print(word_list)
        # print(set(word_list))

        # self.ask_letter()
        save = ["f", "a", "l", "l", "e", "n"]
        save = ["a", "r", "r", "i", "v", "e"]
        self.save = self.word_list[:]
        self.save = ["d", "i", "v", "i", "d", "e"]
        # l_word = "r"

        print("\nThis is the counter dict below")
        print(dict(Counter(self.save)))

        # sade = dict(Counter(self.save))
        # print(Counter(self.save))
        # print(Counter(save)["l"])

        # ---------------------------------------------------
        # this code knows the num of times a letter occur in a word
        # and paste the letters back in a list
        # ---------------------------------------------------
        self.draft = []
        for key, value in Counter(self.save).items():
            # print(key)
            while value > 0:
                if value > 1:
                    self.draft.append(key)
                value -= 1
            self.draft.append(key)
            # stop here
            # if value > 1:
            #     while value > 0:
            #         draft.append(key)
            #         value -= 2
            # draft.append(key)
            # stop here
        print("\nThis is the draft_list below")
        print(self.draft)

        war = dict(Counter(self.save))
        # print(war)
        # ----------------------------------------------------------
        # this is for line 31 of the spec
        # for key, value in war.items():
        #     if key == "v":
        #         print("hello value")
        #         print(value)

        # this is for line 31 of the spec
        # ----------------------------------------------------------
        # for l in save:
        # l_word = l
        # for m in save:
        #     if m == l_word:
        #         # print(f"{m} occurs here")

        #         num_l += 1
        # ---------------------------------------------------
        # this code knows the num of times a letter occur in a word
        # and paste the letters back in a list
        # ---------------------------------------------------

        # ---------------------------------------------------
        # this shows the num of times the letter 'r' is in save
        # ---------------------------------------------------
        # l_word = "r"
        # for l in save:
        #     if l == l_word:
        #         num_l += 1
        # ---------------------------------------------------
        # this shows the num of times the letter 'r' is in save
        # ---------------------------------------------------

        # print(num_l)

    # def

    def run_game(self):
        """ Starts the main lopp for the game """
        while self.game_active:
            print("\nEnter 'exit' to quit anytime. ")
            print(f"the word is {self.word}")
            self.letter = input("Pick a letter that occurs in the word  ")

            if self.letter == "exit":
                sure = input("Are you sure you want to Quit?. y/n  ")
                if sure.lower() == "y":
                    self.game_active = False
                elif sure.lower() == "n":
                    print("\n")
                    rps.run_game()
                else:
                    print("\nChoose y/n")

            else:
                # self.ask_letter()
                self.is_it_a_letter()
                self.is_letter_in_word()

    def check_that_letter_occurs_the_right_amt(self):
        """ This checks that the letter occurs for the right amount. """
        # for letter in

    # def ask_letter(self):
    #     """ This asks the user for letter """
    #     # self.check_num_guesses_left()
    #     self.letter = input("Pick a letter that occurs in the word  ")

    def is_it_a_letter(self):
        """ This checks whether the input is a letter """
        if self.letter not in self.alphabets:
            print("\nSorry, you must chose a letter.")
            # self.ask_letter()
            # self.is_it_a_letter()
            self.run_game()
        # else:
        # print(self.letter)

    def is_it_first_letter(self):
        """ This checks whether the letter is the first to inputted.  """
        # if len(self.given_letters) = 0

    def is_letter_in_word(self):
        """ This checks whether the letter is in the word """
        if self.letter in self.word:
            self.check_whether_letter_was_prev_mentioned()
            # print("ok i see")
            # print("Yes, that letter is in the word")

            # self.check_whether_letter_was_prev_mentioned()
            # self.run_game()

            # print("oremi")
            self.given_letters.append(self.letter)
            print(self.letter)
            self.word_dict[f"{self.letter}"] = 1
            # if
            print(self.given_letters)
            print(self.word_dict)
            # self.run_game()

        else:
            print(
                f"No, that letter is not in the word. \nYou have {self.num_guesses - 1} guesses left"
            )
            self.num_guesses -= 1
            self.check_num_guesses_left()
            self.run_game()

    def check_whether_letter_was_prev_mentioned(self):
        """ This checks whether the letter was previously mentioned """
        if self.letter in self.given_letters:
            print("This word has been mentioned")
            # self.word_dict[f"{self.letter}"] += 1
            self.word_dict[self.letter] += 1
            print(self.word_dict)
            print("this runs")

    def check_num_guesses_left(self):
        """ This checks if the number of guesses is less than zero """
        if self.num_guesses == 0:
            self.game_active = False


if __name__ == "__main__":
    hg = Hangman()
    hg.run_game()
