from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = """"
Christoph Huber
University of Innsbruck

Email: christoph.huber@uibk.ac.at
Web: chr-huber.com
"""

doc = """
Numeracy task: adding sets of five two-digit numbers
with three stages to measure competitiveness

References:
Balafoutas, L., Fornwagner, H., & Sutter, M. (2018). Closing the gender gap in competitiveness through priming. Nature communications, 9(1), 1-6.
Niederle, M., & Vesterlund, L. (2007). Do women shy away from competition? Do men compete too much?. The Quarterly Journal of Economics, 122(3), 1067-1101.
Saccardo, S., Pietrasz, A., & Gneezy, U. (2018). On the size of the gender difference in competitiveness. Management Science, 64(4), 1541-1554.

"""


class Constants(BaseConstants):
    name_in_url = 'num'
    players_per_group = None
    num_rounds = 4

    timeout = [
        60,
        180,
        180,
        180
    ]


class Subsession(BaseSubsession):

    def creating_session(self):

        for p in self.get_players():

            if self.round_number is 1:
                if 'info_treatment' in p.participant.vars.keys():
                    p.info_treatment = p.participant.vars['info_treatment']
                else:
                    p.info_treatment = 'none'


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    info_treatment = models.StringField()

    trials = models.IntegerField()
    correct = models.IntegerField()

    compete = models.FloatField()

    def save_performance(self):
        self.participant.vars['performance'] = self.correct

    def save_competitiveness(self):
        self.participant.vars['competitiveness'] = self.compete

    def num_history(self):
        if self.subsession.round_number == 1:
            round = [1]
            performance = [self.correct]
            compete = [self.compete]
        else:
            round, performance, compete = list(zip(*self.participant.vars['num_history']))
            round = round  + (self.subsession.round_number,)
            performance = performance  + (self.correct,)
            compete = compete  + (self.compete,)
        self.participant.vars['num_history'] = list(zip(round, performance, compete))
