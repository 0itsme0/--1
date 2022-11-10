class Person:
  def __init__(self, name):
    self.__name = name 
    self.__age = 1
    
  def set_age(self, age):
    if age in range(1, 100)
     self.__age = age
    else:
      print('Недопустимый возраст')
