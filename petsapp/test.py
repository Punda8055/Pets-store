import unittest
def add_number(num1,num2):
    return num1+num2

class TestAddition(unittest.TestCase):
    def test_posi_number(self):
        result= add_number(5,7)
        self.assertEqual(result,12)

    def test_neg_number(self):
        result= add_number(-5,-7)
        self.assertEqual(result1,-12)

if __name__ == '__main__':
    unittest.main()
        