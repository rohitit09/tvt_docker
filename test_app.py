import unittest
import app

class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(app.sum_values(10, 5,6), 21)
        self.assertEqual(app.sum_values(1,2,15), 18)
        self.assertEqual(app.sum_values(2,3,13), 5)

    def test_main(self):
        a,b,c=1,2,'a'
        self.assertEqual(app.main(a,b,c), 'All inputs must be numeric')

if __name__ == '__main__':
    unittest.main()