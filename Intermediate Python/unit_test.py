import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):

    def test_return_type_is_integer(self):
        self.assertIsInstance(add_numbers(2, 3), int)

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(2, -3), -1)



if __name__ == '__main__':
    unittest.main(verbosity=2)