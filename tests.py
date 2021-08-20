from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission

import random

class PlayerBot(Bot):

    def play_round(self):

        if self.round_number == 1:
            yield (pages.Instructions)
            yield (pages.Instructions0)
            yield Submission(pages.Num0,
                {
                    'correct': random.randint(0, 10)
                },
                check_html=False, timeout_happened=True
            )
        elif self.round_number == 2:
            yield (pages.Instructions1)
            yield Submission(pages.Num1,
                {
                    'correct': random.randint(0, 10)
                },
                check_html=False, timeout_happened=True
            )
        elif self.round_number == 3:
            yield (pages.Instructions2)
            yield Submission(pages.Num2,
                {
                    'correct': random.randint(0, 10)
                },
                check_html=False, timeout_happened=True
            )
        elif self.round_number == 4:
            yield (pages.Instructions3)
            yield (pages.Allocation,
                {
                    'compete': random.randint(0, 100)
                }
            )
            yield Submission(pages.Num3,
                {
                    'correct': random.randint(0, 10)
                },
                check_html=False, timeout_happened=True
            )
        yield (pages.Feedback)
