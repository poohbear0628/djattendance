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


class UserDictionaryGenerator(generators.Generator):
    """
    Generates a dictionary, which represents a user, at random from a list.
    """

    def __init__(self):
        self.users = [
            {
                'gender': 'B',
                'email': 'jarrton@example.com',
                'firstname': 'Jarrod',
                'lastname': 'Fulton'
            },
            {
                'gender': 'B',
                'email': 'david.lee@example.com',
                'firstname': 'David',
                'lastname': 'Lee'
            },
            {
                'gender': 'S',
                'email': 'itsjojo@example.com',
                'firstname': 'Joanne',
                'lastname': 'Anderson'
            },
            {
                'gender': 'S',
                'email': 'emilyr@example.com',
                'firstname': 'Emily',
                'lastname': 'Rovenskaya'
            },
            {
                'gender': 'S',
                'email': 'cutiepie@example.com',
                'firstname': 'Tracy',
                'lastname': 'Garcia'
            }
        ]

    def generate(self):
        return random.choice(self.users)


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


class FirstNameGenerator(generators.Generator):
    """
    Generates a random first name from a list, either brother or sister.
    """

    def __init__(self, gender=None):
        self.gender = gender
        self.brother = [
            'Abraham', 'Adam', 'Anthony', 'Brian', 'Bill', 'Ben', 'Calvin',
            'David', 'Daniel', 'George', 'Henry', 'Ian', 'Isaac', 'Ivan',
            'Jonathan', 'Jeremy', 'Jacob', 'John', 'Jerry', 'Joseph', 'James',
            'Larry', 'Michael', 'Mark', 'Paul', 'Peter', 'Phillip', 'Stephen',
            'Tony', 'Titus', 'Trevor', 'Timothy', 'Victor', 'Vincent',
            'Winston', 'Walt'
        ]
        self.sister = [
            'Abbie', 'Anna', 'Alice', 'Beth', 'Carrie', 'Christina',
            'Danielle', 'Emma', 'Emily', 'Esther', 'Felicia', 'Grace',
            'Gloria', 'Helen', 'Irene', 'Joanne', 'Joyce', 'Jessica', 'Kathy',
            'Katie', 'Kelly', 'Linda', 'Lydia', 'Mandy', 'Mary', 'Olga',
            'Olivia', 'Priscilla', 'Rebecca', 'Rachel', 'Susan', 'Sarah',
            'Stacey', 'Vanessa', 'Veronica', 'Victoria', 'Vivian', 'Wendy',
            'Yesenia', 'Zoe'
        ]
        # this is a test
        self.testmix = [
            ('B', 'David'), ('B', 'Enoch'), ('B', 'Isaac'), ('B', 'Joseph'),
            ('S', 'Amy'), ('S', 'Irene'), ('S', 'Joanne'), ('S', 'Jolene'),
            ('S', 'Lisa'), ('S', 'Tracy')
        ]
        self.all = self.brother + self.sister

    def generate(self):
        if self.gender == 'B':
            return random.choice(self.brother)
        elif self.gender == 'S':
            return random.choice(self.sister)
        # this is a test
        elif self.gender == 'TG':
            return random.choice(self.testmix)[0]
        elif self.gender == 'TN':
            return random.choice(self.testmix)[1]
        else:
            return random.choice(self.all)


class LastNameGenerator(generators.Generator):
    """
    Generates a random last name from a list.
    """

    def __init__(self):
        self.surname = [
            'Acosta', 'Adulpravitchai', 'Aguirre', 'Ahn',
            'Baker', 'Baltazar', 'Bates', 'Boswell', 'Buchanan', 'Bunakova',
            'Chan', 'Chang', 'Chen', 'Cheng', 'Chiu', 'Choi', 'Chou', 'Chu',
            'Chung', 'Clark', 'Crawford',
            'Danek', 'Davis', 'Deng', 'Depradine', 'Diez', 'du Plooy', 'Duong',
            'Eades', 'Edwin', 'Ellis', 'Escobar', 'Eugenio',
            'Figueroa', 'Flores', 'Folwarski', 'Forrest', 'Freeman', 'Fulton',
            'Gagne', 'Garcia', 'George', 'Graham', 'Gray', 'Guo',
            'Han', 'Herrera', 'Hernandez', 'Hsu', 'Huang', 'Hunter', 'Hwang',
            'Ibe',
            'Jackson', 'Jikia', 'Joewono', 'Jones', 'Jung', 'Juraschek',
            'Kamau', 'Kan', 'Kang', 'Kangas' 'Kim', 'Kuo', 'Kwiatkowski',
            'Lee', 'Lemus', 'Li', 'Limanjaya', 'Lin', 'Liu', 'Lopez', 'Lutz',
            'Marks', 'Marshall', 'Martinez', 'Mendoza', 'Miteiko', 'Miyake',
            'Mok', 'Moon', 'Morgan', 'Mujuni',
            'Nuernberger', 'Nguyen',
            "O'Connor", 'Olmos', 'Olson',
            'Pagunsan', 'Pan', 'Park', 'Peel', 'Penner', 'Portman',
            'Quintanilla', 'Qu',
            'Roberson', 'Roberts', 'Roszol', 'Rovenskaya',
            'Salinas', 'Sanchez', 'Sandlin', 'Shao', 'Shi', 'Smith', 'Song',
            'Stevens', 'Stewart', 'Stone', 'Strong', 'Su', 'Sun',
            'Tai', 'Tan', 'Tang', 'Tashman', 'Therisod', 'Timberlake', 'Tsai',
            'Ung', 'Uy',
            'Valdez', 'Van Der Noord', 'Velasquez', 'Villareal',
            'Waggener', 'Walker', 'Wang', 'White', 'Wong', 'Woodfield', 'Wu',
            'Xu',
            'Yang', 'Yao', 'Yu',
            'Zheng', 'Zhu'
        ]

    def generate(self):
        return random.choice(self.surname)


class UserAutoFixture(AutoFixture):
    field_values = {
        'gender': GenderGenerator(ratio='45B_55S'),
        'email': generators.EmailGenerator(static_domain='example.com'),
        'firstname': FirstNameGenerator(),
        'lastname': LastNameGenerator()
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
