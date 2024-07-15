#bai tap mot 
'''import torch 
import torch.nn as nn 
data = torch.Tensor([1,2,3])
softmax_function = nn.Softmax(dim=0)
output = softmax-function(data)
assert round(output[0].item(),2)==0.9 
output'''
# bai tap hai 
# bai tap ba
# bai tap bon
# bai tap nam
from abc import ABC, abstractmethod 
class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob
    def get_yob(self):
        return self._yob 
    @abstractmethod 
    def describe (self):
        pass 
class Student(Person):
    def __init__(self, name=str, yob=int, grade=str):
        self._yob=yob
        self._name=name 
        self._grade=grade 
    def describe (self):
        print(f'name={self._name}-yob={self._yob}-grade={self._grade}')
student1= Student(name="studentZ2023",yob=2011,grade="6")
assert student1._yob == 2011
student1.describe() 
#bai tap sáu
from abc import ABC, abstractmethod 
class Person(ABC):
    def __init__(self,name:str,yob:int):
        self._name=name
        self._yob=yob
    def get_yob(self):
        return self._yob 
    @abstractmethod 
    def describe(self):
        pass
class Teacher(Person):
    def __init__(self, name=str,yob=int, subject=str):
        super().__init__(name,yob)
        self._subject=subject 
    def describe(self):
        print(f'name={self._name}-yob={self._yob}-subject={self._subject}')
teacher1=Teacher(name="teacherZ2023",yob=1991,subject="History")
assert teacher1._yob ==1991
teacher1.describe()
# bài tập bảy
from abc import ABC, abstractmethod 
class Person(ABC):
    def __init__(self,name:str,yob:int):
        self._name=name
        self._yob=yob
    def get_yob(self):
        return self._yob 
    @abstractmethod 
    def describe(self):
        pass
class Doctor(Person):
    def __init__(self,name=str,yob=int,specialist=str):
        super().__init__(name,yob)
        self._specialist=specialist
    def describe(self):
        print(f'name={self._name}-yob={self._yob}-specialist={self._specialist}')
doctor1=Doctor(name="doctorZ2023",yob=1981,specialist="Endocrinologists")
assert doctor1._yob ==1981
doctor1.describe()
#bài tập 8
class Ward:
    def __init__(self, name=str):
        self.__name=name
        self.__listPeople=list()
    def add_person(self, person=Person):
        self.__listPeople.append(person)
    def describe(self):
        print(f'Ward Name={self.__name}')
        for p in self.__listPeople:
            p.describe()
    def countDoctor(self):
        counter=0
        for p in self.__listPeople:
            if isinstance(p,Doctor):
                counter+=1
            else:
                return counter
    
ward1=Ward()
student1=Student(name="studentA",yob=2010,grade="7")
teacher1=Teacher(name="teacherA",yob=1969,subject="Math")
teacher2=Teacher(name="teacher2",yob=1995,subject="History")
doctor1=Doctor(name="doctorA",yob=1945,specialist="Endocrinolists")
assert ward1.countDoctor()==1
doctor2=Doctor(name="doctorB",yob=1975,specialists="Cardiologists")
ward1=Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.countDoctor()
# bài tập 9
class Mystack:
    def __init__(self,capacity):
        self.__capacity=capacity
        self.__stack=[]
    def is_full(self):
        return len(self.__stack)==self.__capacity
    def push(self,value):
        if self.is_full():
            raise Exception("Overflow")
        self.__stack.append(value)
stack1=Mystack(capacity=5)
stack1.push(1)
assert stack1.is_full()==False
stack1.push(2)
print(stack1.is_full())
# bài tập 10
class Mystack:
    def __init__(self, capacity):
        self.__capacity=capacity
        self.__stack=[]
    def is_full(self):
        return len(self.__stack)==self.__capacity
    def isEmpty(self):
        return len(self.__stack)==0
    def push(self,value):
        if self.is_full():
            raise Exception("Overflow")
        self.__stack.append(value)
    def top(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.__stack[-1]
stack1=Mystack(capacity=5)
stack1.push(1)
assert stack1.is_full()==False
stack1.push(2)
print(stack1.top())
# bài tập 11
class MyQueue:
    def __init__(self,capacity):
        self.__capacity=capacity
        self.__queue=[]
    def is_full(self):
        return len(self.__queue)==self.__queue
    def enqueue(self,value):
        if self.is_full():
            raise Exception("Overflow")
        self.__queue.append(value)
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full()==False
queue1.enqueue(2)
print(queue1.is_full())
# bài tập 12
class MyQueue:
    def __init__(self,capacity):
        self.__capacity=capacity
        self.__queue=[]
    def isEmpty(self):
        return len(self.__queue)==0
    def is_full(self):
        return len(self.__queue)==self.__capacity
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Underflow")
        return self.__queue.pop(0)
    def enqueue(self,value):
        if self.is_full():
            raise Exception("Overflow")
            self.__queue.append(value)
    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return 
        return self._queue[0] 
queue1=MyQueue(capacity=5)
queue1.enqueue(1) 
assert queue1.is_full()==False
queue1.enqueue(2)
print(queue1.front())
    