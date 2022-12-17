import unittest
import pytest
from GB_PyTask_1 import task_1, task_2, task_3, task_4, task_5


class TestMethods():

    def test_usual_weekday_number(self):
        """Testing Stage 1. Task 1. Normal weekday number as input."""
        test_func = task_1()
        self.assertEqual(5, "No, Freitag (day 5) is not a weekend. It's a business day, get back to work!")
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
