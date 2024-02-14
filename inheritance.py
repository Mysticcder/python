class Animal:
    def animals(self):
        print("can breath")

    def fish(self):
        print("swims in water")

    def monkey(self):
        print("can walk")


class Human(Animal):
    def mtu(self):
        print("lives on land")

being = Human()

print(being.fish())