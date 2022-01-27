# Task 4 / 5 / 6 Так и не разобравшись со спискам и промучавшись решать 3 ночи подряд по своему, решить не удалось!

def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Нет такого количества техники на складе")
        except KeyError:
            print("Нет такого типа на складе")
    return wrapper


class Warehouse:
    '''
    unit_of_equip =
    "type_of_equip": {
    "name": {
    "model", "count"
    }
    }
    }
    '''

    unit_of_equip = {}
# Нулевая попытка решить добавление.
    # def add_to(self):
    #     equip_warehouse = Warehouse.unit_of_equip.get(self.type_of_equip)
    #     if self.name in equip_warehouse.keys():
    #         equip_warehouse_name = equip_warehouse[self.name]
    #         if self.model in equip_warehouse_name.keys():
    #             equip_warehouse_model = equip_warehouse_name[self.model]
    #             equip_warehouse_model[self.model] += self.__count
    #         else:
    #             equip_warehouse_name[self.model].setdefailt(self.model)
    #     else:
    #         Warehouse.unit_of_equip[self.type_of_equip].setdefault(self.name)
    # Warehouse.unit_of_equip[self.type_of_equip].setdefault(self.name, {self.model, self.__count})

    @classmethod
    @validate
    def warehouse_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.unit_of_equip[unit_type][unit_name][unit_model]["count"] += unit_count

    @classmethod
    @validate
    def extract(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.unit_of_equip[unit_type][unit_name][unit_model]["count"]
        if current_count < unit_count:
            raise ValueError
        else:
            cls.unit_of_equip[unit_type][unit_name][unit_model]["count"] -= unit_count

    @staticmethod
    def get_all_equip():
        for key, value in Warehouse.unit_of_equip.items():
            print(key, value)


class OfficeEquip:

    def __init__(self, name, model, type_of_equip, count=0):
        self.name = name
        self.model = model
        self.type_of_equip = type_of_equip
        try:
            if type(count) is not int:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Количество должно быть целым числом")
        else:
            self.__count = count
        finally:
            self.update_warehouse()

    def update_warehouse(self):
        equip_warehouse = Warehouse.unit_of_equip.get(self.type_of_equip, {})
        if self.name in equip_warehouse.keys():
            equip_warehouse_name = equip_warehouse[self.name]
            if self.model in equip_warehouse_name.keys():
                equip_warehouse_model = equip_warehouse_name[self.model]
                equip_warehouse_model["count"] += self.__count
            else:
                equip_warehouse_name[self.model] = {"count": self.__count}
        else:
            equip_warehouse[self.name] = {self.model: {"count": self.__count}}

        Warehouse.unit_of_equip[self.type_of_equip] = equip_warehouse


class Printer(OfficeEquip):
    def __init__(self, name, model, count, type_printer):
        super().__init__(name, model, "Printer", count)
        self.type_printer = type_printer


class Scanner(OfficeEquip):
    def __init__(self, name, model, count, color):
        super().__init__(name, model, "Scanner", count)
        self.color = color


class Xerox(OfficeEquip):
    def __init__(self, name, model, count, country):
        super().__init__(name, model, "Xerox", count)
        self.country = country


printer_1 = Printer("hp", "b411", 200, "Lazer")
printer_2 = Printer("hp", "b420", 100, "Jet")
printer_3 = Printer("hp", "b411", 50, "Lazer")

scanner_1 = Scanner("benq", "x125-8", 31, "black")
scanner_2 = Scanner("simens", "bbk630", 5, "grey")
scanner_3 = Scanner("simens", "bbk630JH", 9, "grey")

xerox_1 = Xerox("Xerox", "1/456-color-jet", 300, "USA")
xerox_2 = Xerox("Canon", "407", 125, "UK")

Warehouse.get_all_equip()

Warehouse.warehouse_to(unit_type="Printer", unit_name="hp", unit_model="b411", unit_count=49)
Warehouse.get_all_equip()


Warehouse.extract(unit_type="Xerox", unit_name="Canon", unit_model="407", unit_count=5)
Warehouse.get_all_equip()