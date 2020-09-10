from . import messages, ui


class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                ui.display(letter + messages.SPACE, end=messages.SPACE)
            else:
                ui.display(messages.PLACEHOLDER +
                           messages.SPACE, end=messages.SPACE)

    def check_guess(self, guess):
        return guess in self.phrase

    def check_complete(self, guesses):
        return all(letter in guesses for letter in self.phrase)
