"""
Refer also to books/tests for unit-test example
This class is intended to also serve as example on how to mock models to maintain decoupling
Note: this unit-test is ONLY considered complete when coverage for "classes/models" = 100%
"""

from terms.models import Term
from classes.models import Class

import unittest
import mock


def set_up_data():
    # model1: Class without term, all types tested
    c1 = Class(name='Experience of Christ as Life', code='ECAL', type='1YR')
    c2 = Class(name='God Ordained Way', code='GOW', type='MAIN')
    c3 = Class(name='New Jerusalem', code='NJ', type='2YR')
    c4 = Class(name='Character', code='CHAR', type='AFTN')
    return dict([('c1', c1), ('c2', c2), ('c3', c3), ('c4', c4)])


class ClassesTests(unittest.TestCase):
  def setUp(self):
    pass

  def test_models(self):
    data_dicts = set_up_data()
    self.assertTrue(Class(data_dicts['c1']))
    self.assertTrue(Class(data_dicts['c2']))
    self.assertTrue(Class(data_dicts['c3']))
    self.assertTrue(Class(data_dicts['c4']))

  def test_class_type_choices(self):
    data_dicts = set_up_data()
    self.assertEqual(data_dicts['c1'].type, "1YR")
    self.assertEqual(data_dicts['c2'].type, "MAIN")
    self.assertEqual(data_dicts['c3'].type, "2YR")
    self.assertEqual(data_dicts['c4'].type, "AFTN")

  # when using mock for term model, so any changes to Term module will not interfere this test
  # this is more ideal because unit test for class should not test "Term"
  # purpose of this test: validating the foreign key model integrity
  # notice the mock does not need set_up_data return value, thus making it cleaner
  def test_term_str(self):
    mock_instance = mock.Mock(spec=Term)
    mock_instance.season = "Fall"
    mock_instance.year = 2014
    self.assertEqual(Term._name(mock_instance), "Fall 2014")
    self.assertEqual(Term._code(mock_instance), "Fa14")

  def test_unicode_functions(self):
    data_dicts = set_up_data()
    self.assertEqual('Experience of Christ as Life', data_dicts['c1'].name)
    self.assertEqual('God Ordained Way', data_dicts['c2'].name)
    self.assertEqual('New Jerusalem', data_dicts['c3'].name)
    self.assertEqual('Character', data_dicts['c4'].name)

  def tearDown(self):
    pass
