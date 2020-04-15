# this is the hangman game
import csv
import string
from random import choice
from collections import Counter, defaultdict


class Hangman:
    """ This manages the hangman game class. """

    def __init__(self):
        """ This initializes the hangman class. """

        self.game_active = True
        self.alphabets = list(string.ascii_lowercase)

        self.words = []

        # This reads from a file to get the six lettered words
        with open("words.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                if len(line["word"]) == 6:
                    self.words.append(line["word"])
        self.word = choice(self.words)
        self.num_guesses = 6
        print("This is HANGMAN.")
        print("You are to guess the letters to a six lettered word.")
        print("You have 6 attempts at guessing the wrong letter.")
        print("Goodluck.")
        self.given_letters = []
        self.word_list = []
        self.word_dict = defaultdict(int)
        for letter in self.word:
            self.word_list.append(letter)

        # save = ["f", "a", "l", "l", "e", "n"]
        # sersave = ["a", "r", "r", "i", "v", "e"]
        # self.word_list = self.word_list[:]
        # self.word_list = ["d", "i", "v", "i", "d", "e"]
        # self.word_list = ["b", "o", "t", "t", "o", "m"]
        # l_word = "r"
        # print("\nThis is the counter dict below")
        # print(dict(Counter(self.word_list)))

        # sade = dict(Counter(self.word_list))
        # print(Counter(self.word_list))
        # print(Counter(save)["l"])

        # ---------------------------------------------------
        # this code knows the num of times a letter occured in a word
        # and paste the letters back in a list
        # ---------------------------------------------------
        # self.draft = []
        # for key, value in Counter(self.word_list).items():
        #     # print(key)
        #     while value > 0:
        #         if value > 1:
        #             self.draft.append(key)
        #         value -= 1
        #     self.draft.append(key)
        # print("\nThis is the draft_list below")
        # print(self.draft)
        # print(sorted(self.draft))
        # print(sorted(self.word_list))

        self.word_counter_dict = dict(Counter(self.word_list))
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
        # and paste the letters back in a listb
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
            # print(f"the word is {self.word}")
            self.letter = input("Pick a letter that occurs in the word  ").lower()

            if self.letter == "exit":
                sure = input("Are you sure you want to Quit?. y/n  ").lower()
                if sure == "y":
                    self.game_active = False
                elif sure == "n":
                    print("\n")
                    hg.run_game()
                else:
                    print("\nChoose y/n")

            else:
                self.is_it_a_letter()
                self.is_letter_in_word()

    def is_it_a_letter(self):
        """ This checks whether the input is a letter """
        if self.letter not in self.alphabets:
            print("\nSorry, you must choose a letter.")
            self.run_game()

    def is_it_first_letter(self):
        """ This checks whether the letter is the first to inputted.  """
        # print("Yea this is the first word!!")
        # if the letter is added for the first time, give it a count
        if self.letter not in self.given_letters:
            self.word_dict[self.letter] = 1

    def check_the_num_occurence(self):
        """ This checks the num of occurence of the letter """
        for key, value in self.word_counter_dict.items():
            if key == f"{self.letter}":
                # print(value)
                self.num_letter_occurence = value

    def is_letter_in_word(self):
        """ This checks whether the letter is in the word """
        if self.letter in self.word_list:
            self.check_the_num_occurence()
            self.is_it_first_letter()

            self.check_whether_letter_was_prev_mentioned()
            self.given_letters.append(self.letter)

            self.print_letter_in_word()

            self.check_if_player_wins()

        else:
            if self.game_active == False:
                pass
            else:
                self.inputs_wrong_letter()

    def print_letter_in_word(self):
        """ This prints that the letter is the word. """
        if (self.letter in self.word_list) and (
            (self.given_letters.count(self.letter) < self.num_letter_occurence)
            or (self.given_letters.count(self.letter) == self.num_letter_occurence)
        ):
            print(f"\nYes {self.letter} is in the word.")
            print(f"The letters you have chosen ==> {self.given_letters}")

    def check_whether_letter_was_prev_mentioned(self):
        """ This checks whether the letter was previously mentioned """
        if self.letter in self.given_letters:
            # print("This word has been mentioned")

            if self.given_letters.count(self.letter) < self.num_letter_occurence:
                self.word_dict[self.letter] += 1
            else:
                self.inputs_wrong_letter()

    def inputs_wrong_letter(self):
        """ This checks whether the wrong letter is inputted. """
        if self.num_guesses > 1 and self.game_active == True:
            if self.num_guesses > 2 and self.game_active == True:
                print(
                    f"\nNo, that letter is not in the word. \nYou have {self.num_guesses - 1} attempts at guessing the wrong letter left."
                )
            else:
                print(
                    "\nNo, that letter is not in the word. \nYou have 1 attempt at guessing the wrong letter left."
                )
            print(f"The letters you have choseen ==> {self.given_letters}")

        self.num_guesses -= 1
        self.check_num_guesses_left()

        if self.game_active == False:
            pass
        else:
            self.run_game()

    def check_num_guesses_left(self):
        """ This checks if the number of guesses is less than zero """
        if self.num_guesses == 0:
            print("\nGAME OVER :(")
            print("You are out of guesses.")
            print(f"The word was {self.word.upper()}.")
            self.game_active = False

    def check_if_player_wins(self):
        """ This checks the word guessed is the same with the word COM chose """
        if sorted(self.given_letters) == sorted(self.word_list):
            print("\nCongrats, You've won!!")
            print(f"The word was {self.word.upper()}.")
            self.game_active = False


if __name__ == "__main__":
    hg = Hangman()
    hg.run_game()
