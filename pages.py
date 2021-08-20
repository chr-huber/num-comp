from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils.translation import ugettext as _


class Instructions(Page):

    def is_displayed(self):
        return self.round_number == 1

class Instructions0(Page):

    def is_displayed(self):
        return self.round_number == 1

class Instructions1(Page):

    def is_displayed(self):
        return self.round_number == 2

class Instructions2(Page):

    def is_displayed(self):
        return self.round_number == 3

class Instructions3(Page):

    def is_displayed(self):
        return self.round_number == 4


class Num0(Page):

    def is_displayed(self):
        return self.round_number == 1

    timeout_seconds = Constants.timeout[0]

    form_model = 'player'
    form_fields = {'trials',
                   'correct'}

    def vars_for_template(self):
        page = self.subsession.round_number

        return {
            'page': page,
            'header': _("Trial round")
        }

    def before_next_page(self):
        self.player.num_history()


class Num1(Page):

    def is_displayed(self):
        return self.round_number == 2

    timeout_seconds = Constants.timeout[1]

    form_model = 'player'
    form_fields = {'trials',
                   'correct'}

    def vars_for_template(self):
        page = self.subsession.round_number

        return {
            'page': page,
            'header': _("Stage 1")
        }

    def before_next_page(self):
        self.player.save_performance()
        self.player.num_history()


class Num2(Page):

    def is_displayed(self):
        return self.round_number == 3

    timeout_seconds = Constants.timeout[2]

    form_model = 'player'
    form_fields = {'trials',
                   'correct'}

    def vars_for_template(self):
        page = self.subsession.round_number

        return {
            'page': page,
            'header': _("Stage 2")
        }

    def before_next_page(self):
        self.player.num_history()


class Num3(Page):

    def is_displayed(self):
        return self.round_number == 4

    timeout_seconds = Constants.timeout[3]

    form_model = 'player'
    form_fields = {'trials',
                   'correct'}

    def vars_for_template(self):
        page = self.subsession.round_number

        return {
            'page': page,
            'header': _("Stage 3")
        }

    def before_next_page(self):
        self.player.save_competitiveness()
        self.player.num_history()


class Allocation(Page):

    def is_displayed(self):
        return self.round_number == 4

    form_model = 'player'
    form_fields = {'compete'}


class Feedback(Page):

    def vars_for_template(self):

        page = self.subsession.round_number

        return {
            'page': page,
            'correct': self.player.correct,
            'num_history': self.player.participant.vars['num_history']
        }


page_sequence = [
    Instructions,
    Instructions0,
    Num0,
    Instructions1,
    Num1,
    Instructions2,
    Num2,
    Instructions3,
    Allocation,
    Num3,
    Feedback
]
