# task_2
#  Вариант с предоставленными данными
class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation(self, thickness):
        result = (float(self.__length) * float(self.__width)) * (25 * thickness)
        return result

road = Road(25.1, 16.9)
print(f"Для укладки дороги по указанным параметрам, потребуется",
      round(road.calculation(float(input(f'Введите толщину асфальта в см: ')))/1000, 2), "тонн асфальта")

#  Вариант с input
#
# class Road:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def calculation(self):
#         result = (float(self.__length) * float(self.__width)) * (25 * 5)
#         return result
#
# road = Road(float(input("Введите длинну асфальта в метрах: ")), float(input("Введите ширину асфальта в метрах: ")))
# print(f"Для укладки дороги по указанным параметрам, потребуется", round(road.calculation()/1000, 2), "тонн асфальта")