class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"


def main():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter subject {i+1} marks: "))
        marks.append(mark)

    student = Student(name, roll, marks)

    print("\n--- Student Result ---")
    print("Name:", student.name)
    print("Roll Number:", student.roll_no)
    print("Total:", student.total())
    print("Average:", student.average())
    print("Grade:", student.grade())


if __name__ == "__main__":
    main()