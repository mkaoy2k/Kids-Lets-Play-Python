import datetime

# 定義人員類別
class Person:

    # 類別變數初值
    head_count = 0

    # 人員物件實體化 函式
    def __init__(self, last, first, dob):
        self.last_name = last
        self.first_name = first
        dob_yyyy, dob_mm, dob_dd = dob.split('-')
        self.birth_date = datetime.date(int(dob_yyyy),
                                        int(dob_mm),
                                        int(dob_dd))
        # 實體化一次加一個人
        Person.head_count += 1

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

    # 退選課程 函式
    def remove_course(self, course):
        if course in self.courses:
            self.courses.pop(course)

    # 列印所選的課程及分數 函式
    def print_courses(self):
        print(self.fullname)
        for course, score in self.courses.items():
            print(f'--> {course}: {score}')

# 定義教員類別
class Teacher(Person):

    # 教員物件實體化 函式
    def __init__(self, last, first, dob, class_id, members=None, courses=None):
        super().__init__(last, first, dob)
        self.class_id = class_id

        # 若不是班導師，學生列表為空
        if members is None:
            self.class_members = []
        else:
            self.class_members = members

        if courses is None:
            self.teaching_courses = []
        else:
            self.teaching_courses = courses

    # 加入班上學生 函式
    def add_member(self, member):
        if member not in self.class_members:
            self.class_members.append(member)

    # 移除班上學生 函式
    def remove_member(self, member):
        if member in self.class_members:
            self.employees.remove(member)

    # 列印班上學生 函式
    def print_members(self):
        print(f'{self.class_id}班導師 {self.fullname} 的學生名單:')
        for member in self.class_members:
            print('-->', member.fullname)
        print()

    # 加入授課課程 函式
    def add_course(self, course):
        if course not in self.teaching_courses:
            self.teaching_courses.append(course)

    # 移除授課課程 函式
    def remove_course(self, course):
        if course in self.teaching_courses:
            self.teaching_courses.remove(course)

    # 列印授課課程 函式
    def print_courses(self):
        print(f'{self.fullname} 授課列表: {self.teaching_courses}\n')

# 定義職員類別
class Staff(Person):

    # 職員物件實體化 函式
    def __init__(self, last, first, dob, title, jobs=None):
        super().__init__(last, first, dob)
        self.title = title

        if jobs is None:
            self.jobs = []
        else:
            self.jobs = jobs
