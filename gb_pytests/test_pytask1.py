import unittest
from GB_PyTask_1 import *


class TestMethods(unittest.TestCase):

    def test_usual_weekday_number(self):
        """Testing Stage 1. Task 1. Normal weekday number as input."""
        test_day = task_1()

        pass

    def test_wrong_weekday_number(self):
        """Testing Stage 1. Task 1. Wrong weekday number as input (0 or 9)."""
        pass

    def test_char_weekday_number(self):
        """Testing Stage 1. Task 1. String symbol as input ('h' or whatever)."""
        pass

    def test_task_examples(self):
        """Testing Stage 1. Task 3. Giving task examples as input."""
        pass

    def test_normal_quarter_number(self):
        """Testing Stage 1. Task 4. Giving simple integer (1-4) as input."""
        pass

    def test_wrong_quarter_number(self):
        """Testing Stage 1. Task 4. Giving wrong integer (5 or any other) as input."""
        pass

    def test_char_quarter_number(self):
        """Testing Stage 1. Task 4. String symbol as input ('f' or whatever)."""
        pass

    def test_distance_task_examples(self):
        """Testing Stage 1. Task 5. Giving task examples as input."""
        pass

    def test_distance_wrong_char(self):
        """Testing Stage 1. Task 5. String symbol as input ('f' or whatever)."""
        pass

if __name__ == '__main__':
    unittest.main()
