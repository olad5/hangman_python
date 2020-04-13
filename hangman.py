# this is the hangman game
import csv
from random import choice
from collections import Counter


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
        word_list = []
        word_dict = {}
        for letter in self.word:
            word_list.append(letter)
            # word_dict[f'{letter}'] =

        # print(word_list)
        # print(set(word_list))

        # self.ask_letter()
        num_l = 0
        save = ["f", "a", "l", "l", "e", "n"]
        save = ["a", "r", "r", "i", "v", "e"]
        save = ["d", "i", "v", "i", "d", "e"]
        save = word_list[:]
        # l_word = "r"

        yes = save.count("l")
        print(Counter(save))
        # print(Counter(save)["l"])

        # ---------------------------------------------------
        # this code knows the num of times a letter occur in a word
        # and paste the letters back in a list
        # ---------------------------------------------------
        draft = []
        for key, value in Counter(save).items():
            while value > 0:
                if value > 1:
                    draft.append(key)
                value -= 1
            draft.append(key)
            # stop here
            # if value > 1:
            #     while value > 0:
            #         draft.append(key)
            #         value -= 2
            # draft.append(key)
            # stop here
        print(draft)
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

    def is_letter_in_word(self):
        """ This checks whether the letter is in the word """
        if self.letter in self.word:
            print("Yes, that letter is in the word")
            # self.ask_letter()
            # self.is_it_a_letter()
            # self.is_letter_in_word()
            # print(self.word)

            l = self.letter
            self.given_letters.append(l)
            print(self.given_letters)
            self.run_game()

        else:
            print(
                f"No, that letter is not in the word. \nYou have {self.num_guesses - 1} guesses left"
            )
            self.num_guesses -= 1
            self.check_num_guesses_left()
            self.run_game()

    def check_num_guesses_left(self):
        """ This checks if the number of guesses is less than zero """
        if self.num_guesses == 0:
            self.game_active = False


if __name__ == "__main__":
    hg = Hangman()
    hg.run_game()
