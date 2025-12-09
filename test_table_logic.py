import unittest
from table_logic import generate_table_of_5

class TestTableLogic(unittest.TestCase):
    def test_generate_table_of_5(self):
        expected_output = [
            "5 x 1 = 5",
            "5 x 2 = 10",
            "5 x 3 = 15",
            "5 x 4 = 20",
            "5 x 5 = 25",
            "5 x 6 = 30",
            "5 x 7 = 35",
            "5 x 8 = 40",
            "5 x 9 = 45",
            "5 x 10 = 50"
        ]
        result = generate_table_of_5()
        self.assertEqual(result, expected_output)
        self.assertEqual(len(result), 10)

if __name__ == '__main__':
    unittest.main()
