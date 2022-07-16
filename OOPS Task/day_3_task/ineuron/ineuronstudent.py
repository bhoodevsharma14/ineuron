# module implementation
from .ineuroncourses import ineuronCourses

# All the classes are an example if encapsulation we bind same type of properties and attribues in one class
class ineuronStudent(ineuronCourses):

    def __init__(self,name):
        self.student_name = name
        # protected variable
        self._student_purchased_courses = {}

    def buy_course(self):
        print("Please Select a course:-")
        courses = ineuronCourses._show_courses()
        for course,price in courses.items():
            print(f"Course Name: {course}, Course Price: {price} ")
        while True:
            course_to_buy = input("\nPlease enter the name of course you want to buy or zero(0) to exit:-")
            if course_to_buy == '0':
                break
            if course_to_buy in courses.keys():
                self._student_purchased_courses[course_to_buy] = courses[course_to_buy]
                break
            else:
                print("Please Enter A Valid Input!!")
    
    def show_courses(self):
        if self._student_purchased_courses:
            print("Here are the courses you have purchased:")
            for course,price in self._student_purchased_courses.items():
                print(f"Course Name: {course}, Course Price: {price} ")

    # over-riding show_details method of ineuronCourses
    def show_details(self):
        print("Hello this is an ineuronStudent Class Object!!!")
