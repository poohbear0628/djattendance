import random

from .models import User, TrainingAssistant, Trainee
from autofixture import generators, register, AutoFixture

""" accounts.autofixtures

Uses django-autofixture to generate random testing data.
(https://github.com/gregmuellegger/django-autofixture/)

Create test data using the loadtestdata command, for example:
$ django-admin.py loadtestdata accounts.User:50 accounts.TrainingAssistant:5 accounts.Trainee:50

(note: generate Users before generating TAs and Trainees)
"""


class GenderGenerator(generators.Generator):
    """
    Generates a random gender from a list.
    """

    def __init__(self, ratio=None):
        self.ratio = ratio
        self.genders = ['B', 'S']
        self.ratio_45B_55S = [
            'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
            'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
            'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
            'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
            'B', 'B', 'B', 'B', 'B',  # 45 percent brothers
            'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
            'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
            'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
            'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
            'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
            'S', 'S', 'S', 'S', 'S'  # 55 percent sisters
        ]

    def generate(self):
        if self.ratio == '45B 55S':
            return random.choice(self.ratio_45B_55S)
        else:
            return random.choice(self.genders)


class UserAutoFixture(AutoFixture):
    field_values = {
        'gender': GenderGenerator(ratio='45B_55S'),
        'email': generators.EmailGenerator(static_domain='example.com'),
        'firstname': generators.FirstNameGenerator(),
        'lastname': generators.LastNameGenerator()
    }

register(User, UserAutoFixture)


class TraineeAutoFixture(AutoFixture):
    field_values = {
    }

register(Trainee, TraineeAutoFixture)


class TrainingAssistantAutoFixture(AutoFixture):
    field_values = {
    }

register(TrainingAssistant, TrainingAssistantAutoFixture)
