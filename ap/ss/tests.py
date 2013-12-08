from django.test import TestCase

from accounts.models import User
from ss.autofixtures import UserAutoFixture
import sys


class AutofixtureTests(TestCase):

    def test_autofixture(self):
        """
        This is a test case for using autofixtures in a test.
        """
        # Open this file for the testing output.
        sys.stdout = open('test-autofixture.txt', 'w')
        fixture = UserAutoFixture(User)
        users = fixture.create(25)
        for user in users:
            print "******* USER " + user.email + " *******"
            print "FIRST NAME: " + user.firstname
            print "LAST NAME: " + user.lastname
            print "MIDDLE NAME: " + user.middlename
            print "NICKNAME: " + user.nickname
            print "MAIDEN NAME: " + user.maidenname
            print "GENDER: " + user.gender
            #print "DATE OF BIRTH: " + user.date_of_birth.strftime('%Y/%m/%d')
            #print "AGE: " + str(user.age)