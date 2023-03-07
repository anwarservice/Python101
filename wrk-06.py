class Robot:
    '''แสดง  robot, และ name.'''
    #A class variable, counting the number of robots
    population = 0
    def __init__(self,name):
        '''กำหนดข้อมูลเบื้องต้น Initializes the data.'''
        self.name = name
        print('(Initialize {0})'.format(self.name))
        # นับเพิ่มจำนวน Robot เมื่อมีการสร้าง object เพิ่ม 
        Robot.population += 1
    def __del__(self):
        '''เมื่อมีการลบทิ้ง '''
        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:  #เหลือ Robot ตัวสุดท้าย
            print('{0} was the last one.'.format(self.name))
        else:    #แสดงจำนวน Robot ที่เหลือทั้งหมด
            print('There are still {0:d} robots working.'.format(Robot.population))
    def sayHi(self):
        '''แสดงทักทาย.
        Yeah, they can do that.'''
        print('Greetings, my master call me {0}.'.format(self.name))
    def howMany():
        '''แสดงจำนวน Robot ที่มี '''
        print('We have {0:d} robots.'.format(Robot.population)) 
    howMany = staticmethod(howMany)

class SchoolMember:
        '''Represents any school member.'''
        def __init__(self, name, age):
                self.name = name
                self.age = age
                print('(Initialized SchoolMember: %s)' % self.name)
        def tell(self):
                '''Tell my details.'''
                print('Name:"%s" Age:"%s"' % (self.name, self.age))
class Teacher(SchoolMember):
        '''Represents a teacher.'''
        def __init__(self, name, age, salary):
                SchoolMember.__init__(self, name, age)
                self.salary = salary
                print ('(Initialized Teacher: %s)' % self.name)
        def tell(self):
                SchoolMember.tell(self)
                print ('Salary: "%d"' % self.salary)
class Student(SchoolMember):
        '''Represents a student.'''
        def __init__(self, name, age, marks):
                SchoolMember.__init__(self, name, age)
                self.marks = marks
                print ('(Initialized Student: %s)' % self.name)
        def tell(self):
                SchoolMember.tell(self)
                print ('Marks: "%d"' % self.marks)
t = Teacher('Mr Donrofad Sohhad', 40, 30000)   # สืบทอด Inheritance จาก Class SchoolMember
# สร้าง object ครู
print('---------------Member---------------------\n')
# สร้าง object นักเรียน
s = Student('Anwar', 15, 75)  #ชื่อ  อายุ   คะแนน

print('---------------All Member-----------------\n')
members = [t, s]
for member in members:
        member.tell() # works for both Teachers and Students
        
print('----------------Robot----------------------n')        
droid1 = Robot('R2-D2')
droid1.sayHi()
droid1.howMany()

droid2 = Robot('C-3P1')