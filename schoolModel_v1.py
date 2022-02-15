import datetime

# 定義人員類別
class Person:

    # 人員物件實體化 函式
    def __init__(self, last, first, dob):
        self.last_name = last
        self.first_name = first
        dob_yyyy, dob_mm, dob_dd = dob.split('-')
        self.birth_date = datetime.date(int(dob_yyyy),
                                        int(dob_mm),
                                        int(dob_dd))
    # 定義 email 屬性

    @property
    def email(self):
        return f'{self.last_name}{self.first_name}@school.edu.tw'

    # 定義 fullname 全名 屬性
    @property
    def fullname(self):
        return f'{self.last_name} {self.first_name}'

    # 定義 email 屬性
    @fullname.setter
    def fullname(self, name):
        last, first = name.split(' ')
        self.last_name = last
        self.first_name = first

# 定義學員類別
class Student(Person):

    # 學員物件實體化 函式
    def __init__(self, last, first, dob, class_id, courses=None):
        super().__init__(last, first, dob)
        self.class_id = class_id
        if courses is None:
            self.courses = {}
        else:
            self.courses = courses

    # 加入班級別 函式
    def add_classId(self, class_id):
        self.class_id = class_id

    # 加入課程和分數 函式，課程不在就新增
    def add_course(self, course, score=0):
        self.courses.update({course: score})

    # 退選課程教 函式
    def remove_course(self, course):
        if course in self.courses:
            self.courses.pop(course)

    # 列印所選的課程及分數 函式
    def print_courses(self):
        print(self.fullname)
        for course in self.courses:
            print(f'--> {course}: {self.courses[course]}')
