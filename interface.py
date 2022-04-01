from abc import ABC, abstractclassmethod


class Interface(ABC):
# Interface All Method Are Abstract Methods Or Else Abstract Class

    @abstractclassmethod
    def run(self):
        pass

    @abstractclassmethod
    def swim(self):
        pass

class Abstract(Interface):

    def run(self):
        print('I CAN RUN')


# obj = Abstract()
# obj = Abstract() -> Can't instantiate abstract class Abstract with abstract method swim

class ActualClass(Abstract):

    def swim(self):
        print('I CAN SWIM')

actual = ActualClass()
actual.run()
actual.swim()