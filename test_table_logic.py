import unittest
from table_logic import generate_table_of_10

class TestTableLogic(unittest.TestCase):

    def test_generate_table_of_10(self):
        expected_output = [
            "10 x 1 = 10",
            "10 x 2 = 20",
            "10 x 3 = 30",
            "10 x 4 = 40",
            "10 x 5 = 50",
            "10 x 6 = 60",
            "10 x 7 = 70",
            "10 x 8 = 80",
            "10 x 9 = 90",
            "10 x 10 = 100"
        ]
        result = generate_table_of_10()
        self.assertEqual(result, expected_output)
        self.assertEqual(len(result), 10)

if __name__ == '__main__':
    unittest.main()
