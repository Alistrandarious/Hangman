from Hangman import *
from ImportWords import *

import unittest

class HangManTests(unittest.TestCase):

    def name_test(self):
        self.assertIsNotNone(self.WelcomeScreen.greetings(), "Ali")

    def help_test(self):
        self.assertIsNotNone(WelcomeScreen.greetings(), "0")



# Python - m unittest tests all tests in the area that I am looking. be sure to quit with quit() in the terminal. -v is
# verbose. Python is more talkative. Discover runs anything that starts with test in the filename. use pytest.
