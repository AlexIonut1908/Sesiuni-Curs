from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        print('HAM HAM')

    def sleep(self):
        print('zzzzzzz')

class Cat(Animal):
    def sound(self):
        print('MIAU MIAU')

    def sleep(self):
        print('prrrrrrrr')

dog = Dog()
dog.sound()
dog.sleep()

cat = Cat()
cat.sound()
cat.sleep()