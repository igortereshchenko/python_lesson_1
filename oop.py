class Human:

    def __init__(self, name, age):

        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age



class Worker(Human):

    def __init__(self, name, age, work):

        self.work = work
        self.name = name
        self.setAge(age)


    def info(self):
        print('Name', self.name, 'Age',self.getAge(), 'Work', self.work)



igor = Worker(age=32, name='Igor', work='IT')

igor.info()