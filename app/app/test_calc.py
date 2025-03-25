from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error"""
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


    def test_divide_numbers(self):
        """Test that two numbers are divided"""
        res = calc.divide(10, 2)
        self.assertEqual(res, 5)


    def test_multiply_numbers(self):
        """Test that two numbers are multiplied together"""
        res = calc.multiply(3, 4)
        self.assertEqual(res, 12)



    # def test_subtract_numbers(self):
    #     """Test that two numbers are subtracted"""
    #     res = calc.subtract(10, 5)
    #     self.assertEqual(res, 5)

    
    # def test_subtract_numbers(self):
    #     """Test that two numbers are subtracted"""
    #     res = calc.subtract(10, 5)
    #     self.assertEqual(res, 5)