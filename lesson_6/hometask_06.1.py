# task_1

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        while True:
            print("\033[31m {}" .format(self.__color[0]))
            sleep(7)
            print("\033[31m {}" .format(self.__color[0]), "\033[33m {}" .format(self.__color[1]))
            sleep(3)
            print("\033[32m {}" .format(self.__color[2]))
            sleep(5)
            print("\033[33m {}" .format(self.__color[1]))
            sleep(3)

color_1 = TrafficLight()
color_1.running()

