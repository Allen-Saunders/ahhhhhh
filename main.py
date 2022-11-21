from abc import ABC, abstractmethod

class parent(ABC):

  @abstractmethod
  def fun1(self):
    pass

  def fun2(self):  
    print("this is a parent class")

class child(parent):

  def fun1(self):
    print("This is an child class")

obj=child()
obj.fun1()
obj.fun2()
