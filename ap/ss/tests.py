from django.test import TestCase

from accounts.models import User, Trainee
from ss.autofixtures import TraineeAutoFixture, UserAutoFixture
import sys


class AutofixtureTests(TestCase):

    def test_autofixture(self):
        """
        This is a test case for using autofixtures in a test.
        """
        # Open this file for the testing output.
        sys.stdout = open('test-autofixture.txt', 'w')
        user_fixture, trainee_fixture = UserAutoFixture(User), \
            TraineeAutoFixture(Trainee)
        users, trainees = user_fixture.create(25), trainee_fixture.create(25)
        for user in users:
            print '******* USER ' + user.email + ' *******'
            print 'NAME: ' + user.lastname + ', ' + user.firstname
            print 'GENDER: ' + user.gender
            print 'DATE OF BIRTH: ' + user.date_of_birth.strftime('%Y/%m/%d')
        for trainee in trainees:
            print '******* TRAINEE ' + 'trainee' + ' *******'
            print 'TYPE: ' + trainee.type
            print 'DATES: ' + trainee.date_begin.strftime('%Y/%m/%d') + \
                ' to ' + trainee.date_end.strftime('%Y/%m/%d')
            print 'TEAM: ' + trainee.team.name + ' (' + trainee.team.type + ')'