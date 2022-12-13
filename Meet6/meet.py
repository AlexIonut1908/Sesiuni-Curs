class Car:
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    def __init__(self, model_param, color):
        self.model = model_param
        self.color = color

    def getFields(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.color)

    def accelerate(self):
        print('Vruum Vruum!')

    def stop(self):
        print('STOP!')


# car1 = Car('Logan', 'negru')
# car2 = Car('Duster', 'rosu')
# car1.getFields()
# car2.getFields()
#
# # print(car1.model)
# # print(car2.model)
#
# car1.accelerate()
# car2.stop()