# task_5

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    ''' Ручка '''

    def draw(self):
        print(f'Запуск отрисовки. Тип: {self.title}. В руках используется ручка')


class Pencil(Stationery):
    '''Карандаш'''

    def draw(self):
        print(f'Запуск отрисовки. Тип: {self.title}. В руках используется карнадаш')


class Marker(Stationery):
    '''Маркер'''

    def draw(self):
        print(f'Запуск отрисовки. Тип: {self.title}. В руках используется маркер')



first = Stationery("на принтере")
first.draw()

second = Pen("ручка")
second.draw()

third = Pencil("карандаш")
third.draw()

fouth = Marker("маркер")
fouth.draw()