import random

from . import messages, phrase, ui


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            phrase.Phrase("hi there"),
            phrase.Phrase("hello there"),
            phrase.Phrase("howdy there"),
            phrase.Phrase("whats up there"),
            phrase.Phrase("hey there"),
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [messages.SPACE]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        ui.display(messages.WELCOME)

    def start(self):
        self.welcome()
        while self.is_not_won():
            self.ask_for_guess()
        self.game_over()

        self.again()

    def is_not_won(self):
        return self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False

    def ask_for_guess(self):
        ui.display(messages.NUMBER_MISSED + str(self.missed))
        self.active_phrase.display(self.guesses)
        try:
            user_guess = self.get_guess()
        except ValueError as error:
            ui.display(error)
        else:
            self.guesses.append(user_guess)

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1

    def again(self):
        if ui.prompt(messages.PLAY_AGAIN).lower() == messages.NO:
            ui.display(messages.FAREWELL)
        else:
            self.__init__()
            self.start()

    def get_guess(self):
        guess = ui.prompt(messages.GUESS).lower()
        if not guess.isalpha():
            raise ValueError(messages.ONLY_LETTERS)
        if len(guess) != 1:
            raise ValueError(messages.ONLY_ONE_LETTER)
        return guess

    def game_over(self):
        if self.missed == 5:
            ui.display(messages.LOST)
        else:
            ui.display(messages.WON)
