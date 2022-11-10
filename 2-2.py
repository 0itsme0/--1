def set_age(self, value)
  if value in range(1, 100):
    self.__age = value
  else:
    print('Недопустимый возраст')
