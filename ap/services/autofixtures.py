

from accounts.models import User, TrainingAssistant, Trainee
from aputils.models import Address
from autofixture import generators, register, AutoFixture
from houses.models import House, Bunk
from teams.models import Team
from terms.models import Term
from services.models import Service
import datetime

import random

def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"

""" accounts.autofixtures

Uses django-autofixture to generate random testing data.
(https://github.com/gregmuellegger/django-autofixture/)

Create test data using the loadtestdata command, for example:
$ django-admin.py loadtestdata accounts.User:50 accounts.TrainingAssistant:5 accounts.Trainee:50

(note: generate Users before generating TAs and Trainees)
"""

print 'random', random

class FirstNameGenerator(generators.Generator):

    gender_ratios = ['B', 'S']
    """ Generates a first name, either male or female """

    def __init__(self, gender=None):
        self.gender = gender
        self.male = ['Abraham', 'Adam', 'Anthony', 'Brian', 'Bill', 'Ben', 'Calvin', 'David', 'Daniel',
                     'George', 'Henry', 'Isaac', 'Ian', 'Jonathan', 'Jeremy', 'Jacob', 'John', 'Jerry',
                     'Joseph', 'James', 'Larry', 'Michael', 'Mark', 'Paul', 'Peter', 'Phillip', 'Stephen', 
                     'Tony', 'Titus', 'Trevor', 'Timothy', 'Victor', 'Vincent', 'Winston', 'Walt']
        self.female = ['Abbie', 'Anna', 'Alice', 'Beth', 'Carrie', 'Christina' 'Danielle', 'Emma', 
                       'Emily', 'Esther', 'Felicia', 'Grace', 'Gloria', 'Helen', 'Irene', 'Joanne', 
                       'Joyce', 'Jessica', 'Kathy', 'Katie', 'Kelly', 'Linda', 'Lydia', 'Mandy', 'Mary', 
                       'Olivia', 'Priscilla', 'Rebecca', 'Rachel', 'Susan', 'Sarah', 'Stacey', 'Vivian']
        self.all = self.male + self.female

    def generate(self):
        import random

        gender = random.choice(self.gender_ratios)
        # print '!!!!!!!!!!!!!!!!111', self.gender, self.all
        if gender == 'B':
            return random.choice(self.male)
        elif gender == 'S':
            return random.choice(self.female)
        else:
            # print 'got here', self.all, random, random.choice
            return random.choice(self.all)


class LastNameGenerator(generators.Generator):
    """ Generates a last name """

    def __init__(self):
        self.surname = ['Smith', 'Walker', 'Conroy', 'Stevens', 'Jones', 'Armstrong', 'Johnson',
                        'White', 'Stone', 'Strong', 'Olson', 'Lee', 'Forrest', 'Baker', 'Portman',
                        'Davis', 'Clark', 'Brown', 'Roberts', 'Ellis', 'Jackson', 'Marshall',
                        'Wang', 'Chen', 'Chou', 'Tang', 'Huang', 'Liu', 'Shih', 'Su', 'Song', 'Yang',
                        'Chan', 'Tsai', 'Wong', 'Hsu', 'Cheng', 'Chang', 'Wu', 'Lin', 'Yu', 'Yao', 
                        'Kang', 'Park', 'Kim', 'Choi', 'Ahn', 'Mujuni']

    def generate(self):
        import random
        return random.choice(self.surname)




class ServiceNameGenerator(generators.Generator):
    """
    Generates a random, generic, monosyllabic Asian name.
    AUTHOR'S NOTE: This class is not critical for autofixtures, but was created
    to generate gender-neutral names.  The name bank was created by combing
    through the Fall 2013 roster and choosing all the monosyllabic Asian last
    names.
    """

    # according to datetime.date.today()
    weekdays = ['Mon','Tues', 'Wed', 'Thurs', 
                'Fri', 'Sat', "LD"]

    names = [
        "Bathroom Cleaning", "Supper Cleanup", "Dinner Cleanup", "Sack lunch", 
        "Chairs", "Chairs", "Dinner Prep", "Lunch Prep", 
        "Breakfast Prep"
    ]

    def generate(self):
        import random
        return '%s (%s)' % (random.choice(self.names), random.choice(self.weekdays))


class ServiceAutoFixture(AutoFixture):

    field_values = {
        'name' : ServiceNameGenerator(),
    }


register(Service, ServiceAutoFixture)

# class UserAutoFixture(AutoFixture):
#     # This sets the ratios of the genders
#     gender_ratios = [(generators.StaticGenerator("B"), 45),
#                      (generators.StaticGenerator("S"), 55)]
#     # Arbitrarily have each trainee aged 20 years old
#     birthdate = datetime.date.today() - datetime.timedelta(365 * 20)
#     field_values = {
#         'email': generators.EmailGenerator(static_domain='ftta.org'),
#         'firstname': FirstNameGenerator(),
#         'lastname': LastNameGenerator(),
#         'middlename': generators.StaticGenerator(''),
#         'nickname': generators.StaticGenerator(''),
#         'maidenname': generators.StaticGenerator(''),
#         'gender': generators.WeightedGenerator(choices=gender_ratios),
#         'date_of_birth': birthdate,
#     }


class UserAutoFixture(AutoFixture):
    # This sets the ratios of the genders
    gender_ratios = [(generators.StaticGenerator("B"), 45),
                     (generators.StaticGenerator("S"), 55)]

    field_values = {
        'email' : generators.EmailGenerator(static_domain='example.com'),
        'firstname' : FirstNameGenerator(),
        'lastname' : LastNameGenerator(),
        'gender': generators.WeightedGenerator(choices=gender_ratios),
    }


register(User, UserAutoFixture)


class CampusTeamGenerator(generators.Generator):
    """
    Generates a campus team.
    """

    def generate(self):
        team = Team()
        team.name, team.type = 'CalStateLA Team', 'CAMPUS'
        return team


class ChildrensTeamGenerator(generators.Generator):
    """
    Generates a children's team.
    """

    def generate(self):
        team = Team()
        team.name, team.type = 'Children\'s Team', 'CHILD'
        return team


class CommunityTeamGenerator(generators.Generator):
    """
    Generates a community team.
    """

    def generate(self):
        team = Team()
        team.name, team.type = 'Anaheim Community Team', 'COM'
        return team


class YPTeamGenerator(generators.Generator):
    """
    Generates a YP team.
    """

    def generate(self):
        team = Team()
        team.name, team.type = 'Anaheim YP Team', 'YP'
        return team


class InternetTeamGenerator(generators.Generator):
    """
    Generates an Internet team.
    """

    def generate(self):
        team = Team()
        team.name, team.type = 'I-DCP Team', 'I'
        return team


# class TeamAutoFixture(AutoFixture):

#     teams = [('CalStateLA Team', 'CAMPUS'), ('Children\'s Team', 'CHILD'), ('Anaheim Community Team', 'COM'), 
#             ('Anaheim YP Team', 'YP'), ('I-DCP Team', 'I')]

#     field_values = {
#         'email' : generators.EmailGenerator(static_domain='example.com'),
#         'firstname' : FirstNameGenerator(),
#         'lastname' : LastNameGenerator(),
#         'gender': generators.WeightedGenerator(choices=gender_ratios),
#     }


# register(User, UserAutoFixture)


class TraineeAutoFixture(AutoFixture):
    # This sets the ratios of the trainee types ('R' is for regular trainees,
    # C' is for commuter trainees, and 'S' is for long term short term
    # trainees)
    trainee_type_ratios = [(generators.StaticGenerator('R'), 70),
                           (generators.StaticGenerator('C'), 30)]
    team_ratios = [(CampusTeamGenerator(), 29),
                   (ChildrensTeamGenerator(), 6),
                   (CommunityTeamGenerator(), 15),
                   (YPTeamGenerator(), 27),
                   (InternetTeamGenerator(), 3)]
    # Generate dummy fields for trainees
    term, date_begin, date_end, ta, mentor, house, bunk, address, spouse = \
        Term(), datetime.date.today(), datetime.date.today(), \
        None, None, House(), Bunk(), Address(), None

    generate_fk = ['account', 'team',]
    field_values = {
        'account': UserAutoFixture().create_one(True),
        'type': generators.WeightedGenerator(choices=trainee_type_ratios),
        'date_begin': date_begin,
        'date_end': date_end,
        'ta': ta,
        'mentor': mentor,
        'team': generators.WeightedGenerator(choices=team_ratios).create_one(True),
        'house': house,
        'bunk': bunk,
        'address': address,
        'spouse': spouse
    }

register(Trainee, TraineeAutoFixture)


