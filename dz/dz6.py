from time import sleep
#Task 1
class TrafficLight:

    def __init__(self, color1, color2, color3):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def svet(self):

        if self.color1 == 'красный':
            print(self.color1)
            sleep(2)
        else:
            return print('неправильный порядок цветов')

        if self.color2 == 'желтый':
            print(self.color2)
            sleep(2)
        else:
            return print('неправильный порядок цветов')
        if self.color3 == 'красный':
            print(self.color3)
            sleep(2)
        else:
            return print('неправильный порядок цветов')

#Task 2
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def result(self):
        weight = int(input('введите массу: '))
        thickness = int(input('введите толщину: '))
        print(
            f'Масса асфальта для {self._length * self._width} м.кв. = {(self._length * self._width * weight * (thickness / 100)) / 100} тонн ')


#Task 3
class Worker:
    def __init__(self,name,surname, position, wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

#Task 4
class Car:
    def __init__(self,speed,color, name,is_police=True):
        self.name = name
        self.speed = speed
        self.is_police = is_police
        self.color = color

    def go(self):
        pass
    def stop(self):
        pass
    def turn(self):
        pass
    def show_speed(self):
        pass

#Task5
class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки.{self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки.{self.title}')

class TownCar(Car):
    def show_speed(self):
        if self.speed >60 and self.is_police == True:
            print("Все ок это полицаи едут")
        else:
            print("Превышение скорости TownCar")
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости WorkCar")
        else:
            print('Vse oki4i!')
class PoliceCar(Car):
    pass


if __name__ == '__main__':
#Task1
    a = TrafficLight('красный', 'желтый','зеленый1')
    a.svet()
#Task2
    a = Road(20,30)
    a.result()
#Task3
    woo = Position("Alex",'Moldov','Top',20000,30000)
    print(woo.get_full_name())
    print(woo.get_total_income())
#Task4
    car1 = TownCar(65,'Red','TopCar',True)
    car1.show_speed()
    car2 = WorkCar(40,'Red','TopCar',False)
    car2.show_speed()
#Task5
    a = Pen('Красной ручки')
    a1 = Pencil('Черного карандаша')
    a2 = Handle('Бесцветного маркера')
    a.draw()
    a1.draw()
    a2.draw()