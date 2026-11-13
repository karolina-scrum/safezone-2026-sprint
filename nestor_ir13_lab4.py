class Chainsaw:

    def __init__(self, name="Невідомо", power=0, chain_speed=0,
                 manufacturer="Невідомо", weight=0.0):
        self.__name = name
        self.__power = power
        self.__chain_speed = chain_speed
        self.manufacturer = manufacturer
        self.weight = weight

        print(f"Створено бензопилу {self.__name}.")

# Геттери
    def get_name(self):
        self.weight = 3.8
        return self.__name


    def get_power(self):
        return self.__power

    def get_chain_speed(self):
        return self.__chain_speed

# Сеттери
    def set_name(self, name):
        self.__name = name

    def set_power(self, power):
        if power > 0:
            self.__power = power
        else:
            print("Потужність має бути більшою за нуль!")

    def set_chain_speed(self, chain_speed):
        if chain_speed > 0:
            self.__chain_speed = chain_speed
        else:
            print("Кількість обертів має бути більшою за нуль!")


    def __str__(self):
        return (f"Бензопила {self.__name}, потужність {self.__power} Вт, "
                f"обертів ланцюга {self.__chain_speed} за хв")

    def __repr__(self):
        return (f"Chainsaw( '{self.__name}', {self.__power}, "
                f"{self.__chain_speed}, '{self.manufactureer}', "
                f"{self.weight})")


# Деструктор
    def __del__(self):
        print(f"Бензопилу {self.__name} видалено.")


def main():
    saw1 = Chainsaw()
    saw2 = Chainsaw(name="Stihl MS 180", power=1500, chain_speed=11000, manufacturer="Stihl", weight=3.9)
    saw3 = Chainsaw(name="Husqvarna 120", power=1800, chain_speed=12500, manufacturer="Husqvarna", weight=4.2)
    print(saw3.weight)

    saw2.set_power(2000)
    saw2.set_chain_speed(-5)

    for saw in (saw1, saw2, saw3):
         print(f"Назва: {saw.get_name()}")
         print(f"Потужність (Bn): {saw.get_power()}")
         print(f"Обертів ланцюга (за хв): {saw.get_chain_speed()}")
         print(f"Виробник: {saw.manufacturer}")
         print(f"Вага (кг): {saw.weight}")


if __name__ == "__main__":
    main()