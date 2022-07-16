# All the classes are an example if encapsulation we bind same type of properties and attribues in one class
class ineuronCourses:
    
    # private variable
    __courses = {}

    @classmethod
    def _show_courses(cls)-> dict:
        return cls.__courses

    def add_course(self,course_name,course_price):
        ineuronCourses.__courses[course_name] = course_price
        print("New Course Added")
    
    def show_details(self):
        print("Hello this is an ineuroncourses class object!!")