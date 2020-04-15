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
        sersave = ["a", "r", "r", "i", "v", "e"]
        self.save = self.word_list[:]
        # self.save = ["d", "i", "v", "i", "d", "e"]
        self.save = ["b", "o", "t", "t", "o", "m"]
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
        # print(sorted(self.draft))
        # print(sorted(self.save))

        self.war = dict(Counter(self.save))
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
            # print(f"the word is {self.word}")
            print(f"the word is bottom")
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
                # self.more_unfilled_than_guesses()
                self.is_it_a_letter()
                self.is_letter_in_word()

    # def check_that_letter_occurs_the_right_amt(self):
    #     """ This checks that the letter occurs for the right amount. """
    #     # for letter in

    # def ask_letter(self):
    #     """ This asks the user for letter """
    #     # self.check_num_guesses_left()
    #     self.letter = input("Pick a letter that occurs in the word  ")

    def is_it_a_letter(self):
        """ This checks whether the input is a letter """
        if self.letter not in self.alphabets:
            print("\nSorry, you must choose a letter.")
            # self.ask_letter()
            self.run_game()
        # else:
        # print(self.letter)

    def is_it_first_letter(self):
        """ This checks whether the letter is the first to inputted.  """
        # print("Yea this is the first word!!")
        # if the letter is added for the first time, give it a count
        if self.letter not in self.given_letters:
            # self.word_dict[f"{self.letter}"] = 1
            self.word_dict[self.letter] = 1

    def check_the_num_occurence(self):
        """ This checks the num of occurence of the letter """
        for key, value in self.war.items():
            if key == f"{self.letter}":
                # print("hello value")
                # print(value)
                self.num_letter_occurence = value

    def is_letter_in_word(self):
        """ This checks whether the letter is in the word """
        # if self.letter in self.word:
        # the correct code above
        # ----------------------------------------
        if self.letter in self.save:
            # print(self.given_letters)
            self.check_the_num_occurence()
            self.is_it_first_letter()

            self.check_whether_letter_was_prev_mentioned()
            # print("i ran")
            self.given_letters.append(self.letter)
            # print(self.word_dict)

            self.print_letter_in_word()

            # print(self.letter)
            # self.is_it_first_letter()
            # self.given_letters.append(self.letter)

            # print(self.given_letters)
            # if self.given_letters[-1] == self.letter:
            # else:
            # pass
            # print(self.given_letters)

            # print(self.word_dict)
            self.check_if_player_wins()

        else:
            if self.game_active == False:
                pass
            else:
                self.inputs_wrong_letter()

    def print_letter_in_word(self):
        """ This prints that the letter is the word. and """
        # original code that was working to some extent
        # if (
        #     self.given_letters.count(self.letter) > self.num_letter_occurence
        # ) and self.num_guesses == 1:
        #     pass
        # else:
        #     print(f"\nYes {self.letter} is in the word")

    def check_whether_letter_was_prev_mentioned(self):
        """ This checks whether the letter was previously mentioned """
        if self.letter in self.given_letters:
            # print("This word has been mentioned")

            if self.given_letters.count(self.letter) < self.num_letter_occurence:
                # self.given_letters.append(self.letter)
                self.word_dict[self.letter] += 1
            else:
                self.inputs_wrong_letter()

            # print(self.word_dict)
            # print("this runs")

    def inputs_wrong_letter(self):
        """ This checks whether the wrong letter is inputted. """
        # if self.num_guesses > 2:
        #     print(
        #         f"No, that letter is not in the word. \nYou have {self.num_guesses - 1} guesses left."
        #     )
        # self.given_letters.pop()
        if self.num_guesses > 1:
            if self.num_guesses > 2:
                print(
                    f"No, that letter is not in the word. \nYou have {self.num_guesses - 1} guesses left."
                )
            else:
                print("No, that letter is not in the word. \nYou have 1 guess left.")
            print(f"The letters you have choseen ==> {self.given_letters}")
        # else:
        #     pass
        # print(self.given_letters)
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
            self.game_active = False

    # def more_unfilled_than_guesses(self):
    #     """
    #     this checks if the number of letters to be filled are more than the
    #     guesses left.
    #     """
    #     self.spaces_unfilled = len(self.save) - len(self.given_letters)
    #     print("Spaces unfilled is ")
    #     print(self.spaces_unfilled)
    #     if self.spaces_unfilled > self.num_guesses:
    #         print("GAME OVER :(")
    #         print("You had more spaces to be filled and less guesses.")
    #         self.game_active = False

    def check_if_player_wins(self):
        """ This checks the word guessed is the same with the word COM chose """
        if sorted(self.given_letters) == sorted(self.save):
            # print("\nYou won!!")
            print("\nCongrats, You've won!!")
            self.game_active = False


if __name__ == "__main__":
    hg = Hangman()
    hg.run_game()
