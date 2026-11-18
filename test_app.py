import unittest
from app import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Mythri", "101", [80, 90, 70])

    def test_total(self):
        self.assertEqual(self.student.total(), 240)

    def test_average(self):
        self.assertEqual(self.student.average(), 80)

    def test_grade(self):
        self.assertEqual(self.student.grade(), "A")


if __name__ == "__main__":
    unittest.main()