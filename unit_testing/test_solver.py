from unittest import TestCase
from unit_testing.Solver import Solver

class TestSolver(TestCase):
    # def test_demo(self):
    #     self.fail()
    def test_negative_discr(self):
        s = Solver();
        self.assertRaises(Exception, s.demo,2,1,2)
