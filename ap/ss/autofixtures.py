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


class UserAutoFixture(AutoFixture):
    choices = [(generators.StaticGenerator("B"), 45),
               (generators.StaticGenerator("S"), 55)]
    field_values = {
        'gender': generators.WeightedGenerator(choices=choices),
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
