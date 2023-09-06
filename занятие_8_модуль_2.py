# создаем класс людей 
class Human:
    # создаем статичные атрибуты класса - общте для всех экземпляров 
    name = 'Иван'
    color_of_hair = 'черный'
    height = 190

# cоздаем экземпляры класса
human_1 = Human()
human_2 = Human()
# обраащемся к атрибутам класса
print(human_1.name, human_2.name)

class Human:
    # инициализируем атрибуты для экземпляров класса
    def __init__(self, name, height, color_of_hair):
        self.name = name 
        self.height = height 
        self.color_of_hair = color_of_hair
        self.mental_health = 'normal'

human_1 = Human('Андрей', 190, 'рыжий')
human_2 = Human('Иван', 170, 'каштановый')
# print(human_1.name, human_2.name)
# human_2.name = 'Андрей'
# print(human_2.name)
# выводим магические методы - init тоже один из них
print(dir(Human))