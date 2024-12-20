class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points
        self.grades = {}

    def add_student_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_name(self):
        return self.name

    def get_total_points(self):
        return self.total_points

    def get_student_grade(self, student_id):
        return self.grades.get(student_id, "N/A")


class Course:
    def __init__(self):
        self.roster = []
        self.grade_items = []

    def add_student(self, student):
        self.roster.append(student)

    def add_grade_item(self, grade_item):
        self.grade_items.append(grade_item)

    def add_student_grade(self, grade_item_name, student_id, grade):
        if not any(student.get_student_id() == student_id for student in self.roster):
            raise StudentNotFoundError(f"Exception: Student ({student_id}) not found")
        
        for grade_item in self.grade_items:
            if grade_item.get_name() == grade_item_name:
                grade_item.add_student_grade(student_id, grade)
                return
        raise GradeItemNotFoundError(f"Exception: Grade Item ({grade_item_name}) not found")

    def print_student_grades(self, student_id):
        if not any(student.get_student_id() == student_id for student in self.roster):
            raise StudentNotFoundError(f"Exception: Student ({student_id}) not found")
        
        print(f"Grades for Student ID {student_id}:")
        for grade_item in self.grade_items:
            print(f"{grade_item.get_name()}: {grade_item.get_student_grade(student_id)}")

    def print_roster(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty")
        
        print("Class Roster:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} (ID: {student.get_student_id()})")

    def print_class_grades(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty")

        print("Class Grades:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} (ID: {student.get_student_id()}):")
            for grade_item in self.grade_items:
                print(f"  {grade_item.get_name()}: {grade_item.get_student_grade(student.get_student_id())}")


class EmptyRosterError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


class GradeItemNotFoundError(Exception):
    pass


def main():
    course = Course()
    while True:
        print("\nGradebook Menu:")
        print("1. Add a student to the course")
        print("2. Add a grade item to the course")
        print("3. Add a student’s grade to a specified grade item")
        print("4. Print out a student’s grades for each grade item")
        print("5. Print out the class roster")
        print("6. Print out the grades for all students in the class")
        print("7. Exit")
        choice = input(":> ").strip()

        if choice == "1":
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            try:
                student_id = int(input("Enter student ID: ").strip())
                course.add_student(Student(first_name, last_name, student_id))
                print(f"Student {first_name} {last_name} (ID: {student_id}) added.")
            except ValueError:
                print("Error: Student ID must be numeric.")

        elif choice == "2":
            name = input("Enter grade item name: ").strip()
            try:
                total_points = int(input("Enter total points: ").strip())
                course.add_grade_item(GradeItem(name, total_points))
                print(f"Grade item '{name}' with total points {total_points} added.")
            except ValueError:
                print("Error: Total points must be numeric.")

        elif choice == "3":
            grade_item_name = input("Enter grade item name: ").strip()
            try:
                student_id = int(input("Enter student ID: ").strip())
                grade = int(input("Enter grade: ").strip())
                course.add_student_grade(grade_item_name, student_id, grade)
                print(f"Grade {grade} added for Student ID {student_id} in '{grade_item_name}'.")
            except ValueError:
                print("Error: Grade and Student ID must be numeric.")
            except (StudentNotFoundError, GradeItemNotFoundError) as e:
                print(e)

        elif choice == "4":
            try:
                student_id = int(input("Enter student ID: ").strip())
                course.print_student_grades(student_id)
            except ValueError:
                print("Error: Student ID must be numeric.")
            except StudentNotFoundError as e:
                print(e)

        elif choice == "5":
            try:
                course.print_roster()
            except EmptyRosterError as e:
                print(e)

        elif choice == "6":
            try:
                course.print_class_grades()
            except EmptyRosterError as e:
                print(e)

        elif choice == "7":
            print("Exiting Gradebook.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
