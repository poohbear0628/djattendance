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

class AsianNameGenerator(generators.Generator):
    """
    Generates a random, generic, monosyllabic Asian name.
    """

    names = [
        "Ahn", "Baek", "Bai", "Bang", "Bong", "Chai", "Chang", "Chao", "Chen",
        "Chern", "Cheung", "Chi", "Chiang", "Chiu", "Choi", "Chou", "Chiu",
        "Chu", "Chuah", "Chuang", "Co", "Ding", "Duong", "Feng", "Fok", "Han",
        "Harm", "He", "Hsieh", "Hsiung", "Hsu", "Hu", "Hua", "Huang", "Hung",
        "Hwang", "Jahng", "Jeng", "Jiao", "Jiang", "Jin", "Jou", "Jung", "Kan",
        "Kao", "Kim", "Kor", "Kuo", "Lan", "Lee", "Leung", "Li", "Liang",
        "Lie", "Lim", "Lin", "Liou", "Liu", "Loke", "Lu", "Luo", "Luor", "Mai",
        "Mok", "Pan", "Park", "Peng", "Perng", "Po", "Qin", "Qu", "Ser",
        "Shao", "Shi", "Tai", "Tak", "Tan", "Tien", "Tsai", "Tsang", "Ung",
        "Wang", "Wei", "Wong", "Wu", "Xie", "Xu", "Xue", "Yan", "Yang", "Yao",
        "Ye", "Yen", "Young", "Yu", "Zhan", "Zheng", "Zhou", "Zhu", "Zou"
    ]

    def generate(self):
        return random.choice(self.names)


class UserAutoFixture(AutoFixture):
    gender_ratios = [(generators.StaticGenerator("B"), 45),
                     (generators.StaticGenerator("S"), 55)]
    field_values = {
        'email': generators.EmailGenerator(static_domain='example.com'),
        'firstname': AsianNameGenerator(),
        'lastname': AsianNameGenerator(),
        'middlename': generators.StaticGenerator(''),
        'nickname': generators.StaticGenerator(''),
        'maidenname': generators.StaticGenerator(''),
        'gender': generators.WeightedGenerator(choices=gender_ratios)
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
