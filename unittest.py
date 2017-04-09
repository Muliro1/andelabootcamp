import unittest
from loancalculator import loan_calculator


class loancalculator(unittest.Testcase):
    def test_month(self):
        self.assertEquals(loancalculator(100000, 12, 12), 112000)
        
