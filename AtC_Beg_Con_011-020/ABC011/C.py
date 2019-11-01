from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        print("Hello")

# 抽象クラスを継承
class Cat(Animal):
    def sound(self):
        # 継承元のsoundを呼び出す
        super(Cat, self).sound()
        print("Meow")

if __name__ == "__main__":
    Cat().sound()