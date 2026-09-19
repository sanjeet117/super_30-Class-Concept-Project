class Course:
    course_count = 0  # class variable
    def __init__(self,course_name,instructor,duration,price):
        self.course_name = course_name 
        self.instructor = instructor 
        self.duration = duration 
        self.price = price 

        Course.course_count += 1

    def show_course_details(self):
        print('\n------Course Details -------')
        print(f'Course Name: {self.course_name}')
        print(f'Instructor: {self.instructor}')
        print(f'duration: {self.duration}')
        print(f'Price: {self.price}')

    def calculate_discount(self,discount_percentage):
        discount_amount = self.price * discount_percentage /100 
        final_price = self.price - discount_amount 
        return final_price 

    @classmethod 
    def get_course_count(cls):
        return cls.course_count 

class PremiumCourse(Course):
    def __init__(self,course_name,instructor,duration,price,mentor_support,live_session):
        super(). __init__(course_name,instructor,duration,price)
        self.mentor_support = mentor_support 
        self.live_session = live_session 

    def show_course_details(self):
        print('\n ------ Premium Course Details --------')
        print(f'Course_Name : {self.course_name}')
        print(f'Insturctor : {self.instructor}')
        print(f'Duration : {self.duration}')
        print(f'Price : {self.price}')
        print(f'Mentor_Support : {self.mentor_support}')
        print(f'Live Session : {self.live_session}')

if __name__ == '__main__':
    # Create course Object
    course1 = Course('Pthon Prgramming','Rahul Sharma','8 Weeks',5000)
    course2 = Course('Data Analytics','Amit Mishra','6 Weeks',4000) 
    course3 = Course('Power BI','Neha Singh','6 Week',3500)

    #create Premium Course Object 
    premium_course1 = PremiumCourse('Generative AI','Raj Singh','12 Weeks',15000, 'Available','yes')
    premium_course2 = PremiumCourse('Machine Learning','Priya Pandey','4 Weeks',10000,'Available','yes')

    # Display Course Object
    course1.show_course_details()
    course2.show_course_details()
    course3.show_course_details() 

    premium_course1.show_course_details()
    premium_course2.show_course_details()

    #Calculate discount()
    print('\n -------- Discount Calculation ----------')
    final_price = course1.calculate_discount(10)

    print(f'original Price: {course1.price}') 
    print(f'After 10% discount: {final_price}')

    final_price = premium_course1.calculate_discount(20) 
    print(f'\n Original Price : {premium_course1.price}')
    print(f'After 20% discount : {final_price}') 

    #Display Course Count 
    print('\n =======Display Course Count===========')
    print(f"Total Courses Created: {Course.get_course_count()}")







        


