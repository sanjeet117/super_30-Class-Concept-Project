class User:

    # Class variable
    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

        # Increase total users whenever a new object is created
        User.total_users += 1

    # Instance Method
    def display_user_info(self):
        print("\n--------- User Information ------------")
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(f"User_ID : {self.user_id}")

    # Class Method
    @classmethod
    def get_total_users(cls):
        return cls.total_users

    # Static Method
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


class Student(User):

    def __init__(self, name, email, user_id, course_name):
        super().__init__(name, email, user_id)

        self.course_name = course_name
        self.completed_assignment = []

    # Instance Method
    def assign_course(self, course_name):
        self.course_name = course_name
        print(f"{self.name} is assigned to {course_name} course.")

    # Instance Method
    def submit_assignment(self, assignment_name):
        self.completed_assignment.append(assignment_name)
        print(f"{self.name} submitted assignment: {assignment_name}")

    # Instance Method
    def display_student_info(self):
        print("\n========== Student Information ==========")
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(f"User_ID : {self.user_id}")
        print(f"Course Name : {self.course_name}")
        print(f"Completed Assignment : {self.completed_assignment}")


class Mentor(User):

    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)

        self.expertise = expertise
        self.student_assigned = 0

    # Instance Method
    def assign_student(self):
        self.student_assigned += 1
        print(f"Student assigned to mentor {self.name}")

    # Instance Method
    def display_mentor_info(self):
        print("\n========== Mentor Information ==========")
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(f"User Id : {self.user_id}")
        print(f"Expertise : {self.expertise}")
        print(f"Students Assigned : {self.student_assigned}")


if __name__ == "__main__":

    # Create Student objects
    student1 = Student("Sanjeet", "sanjeet@gmail.com", "S101", "Super30")
    student2 = Student("Rahul", "rahul@gmail.com", "R102", "Python")

    # Create Mentor object
    mentor1 = Mentor("Amit", "amit@gmail.com", "M101", "Python and ML")

    # Assign course
    student1.assign_course("Generative AI")

    # Submit assignments
    student1.submit_assignment("Python OOP Assignment")
    student1.submit_assignment("Logging Assignment")

    student2.submit_assignment("Python Function Assignment")

    # Assign students to mentor
    mentor1.assign_student()
    mentor1.assign_student()

    # Display Student Information
    student1.display_student_info()
    student2.display_student_info()

    # Display Mentor Information
    mentor1.display_mentor_info()

    # Static Method
    print("\n========== Email Validation ==========")
    print(User.validate_email("sanjeet@gmail.com"))
    print(User.validate_email("sanjeetgmail.com"))

    # Class Method
    print("\n========== Total Users ==========")
    print(f"Total Users: {User.get_total_users()}")