class Chef:
    def make_salad(self):
        print('Chef: salad')

    def make_fries(self):
        print('fries')

class JapaneseChef(Chef):
    def make_sushi(self):
        print('sushi')
    def make_salad(self):
        print('Japanese Chef: salad')

class ItalianChef(Chef):
    def make_pizza(self):
        print('pizza')


chef = Chef()
japaneseChef = JapaneseChef()
italianChef = ItalianChef()

chef.make_fries()
japaneseChef.make_sushi()
italianChef.make_pizza()
japaneseChef.make_salad()