import unittest
from main import generate_table_of_3

class TestMain(unittest.TestCase):
    def test_generate_table_of_3(self):
        expected_output = [
            "Multiplication Table of 3:",
            "3 x 1 = 3",
            "3 x 2 = 6",
            "3 x 3 = 9",
            "3 x 4 = 12",
            "3 x 5 = 15",
            "3 x 6 = 18",
            "3 x 7 = 21",
            "3 x 8 = 24",
            "3 x 9 = 27",
            "3 x 10 = 30"
        ]
        self.assertEqual(generate_table_of_3(), expected_output)

if __name__ == '__main__':
    unittest.main()
