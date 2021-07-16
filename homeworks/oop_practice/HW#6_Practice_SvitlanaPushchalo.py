from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, fruits, gardener, fruit_insects):  # + vegetable_insects, vegetables
        # self.vegetables = vegetables
        self.gardener = gardener
        self.fruits = fruits
        self.fruit_insects = fruit_insects
        # self.vegetable_insects = vegetable_insects

    def show_the_garden(self):
        print(f'I am gardener - {self.gardener}')
        # print(f'I have such vegetables {self.vegetables}')
        print(f'There are {len(self.fruits)} apples in the garden.')
        print(f'There are {self.fruit_insects} fruit insects in the garden!!!')
        # print(f'There are {self.vegetable_insects} vegetable insects in the garden!!!')


# class Vegetables:
#     def __init__(self, vegetable_type):
#         self.vegetable_type = vegetable_type
#
#     states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}
#
#     @abstractmethod
#     def growth(self):
#         raise NotImplementedError('You missed me.')
#
#     @abstractmethod
#     def is_ripe(self):
#         raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


# class Tomato(Vegetables):
#     def __init__(self, vegetable_type, number_of_tomatoes):
#         Vegetables.__init__(self, vegetable_type)
#         self.number_of_tomatoes = number_of_tomatoes
#         self.states = 0
#
#     def growth(self):
#         if self.states <= 3:
#             self.states += 1
#         self.print_state()
#
#     def is_ripe(self):
#         return self.states == 3
#
#     def print_state(self):
#         print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")
#
#     def eatable(self):
#         return self.states == 3 or self.states == 2


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0

    def growth(self):
        if self.states <= 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

    def eatable(self):
        return self.states == 3 or self.states == 2

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")


# class TomatoBush:
#     def __init__(self, number_of_tomatoes, quantity_of_pests):
#         # variable for list of our objects
#         self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes)]
#         # for num in range(number_of_tomatoes):
#         #     tomato = Tomatoes('Cherry', num)
#
#     def growth_all(self):
#         for tomato in self.tomatoes:
#             tomato.growth()

    # def all_are_ripe(self):
    #   lst = []
    #   for tomato in self.tomatoes:
    #     ripe_state = tomato.is_ripe()
    #       lst.append(ripe_state)
    #   return all(lst)

    # def all_are_ripe(self):
    #     return all([tomato.is_ripe() for tomato in self.tomatoes])
    #
    # def give_away_all(self):
    #     self.tomatoes = []
    #
    # def poison_all_pests(self):
    #     self.pests = []
    #
    # def count_of_tomatoes(self):
    #     return len(self.tomatoes)


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples)]
        # self.pests = [Pests('Worm', index) for index in range(0, quantity_of_pests)]

    def count_of_apples(self):
        return len(self.apples)

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def insects_attack(self, fruit_pests):
        for _ in range(fruit_pests.pests_quantity):
            for apple in self.apples:
                index = self.apples.index(apple)
                if apple.eatable():
                    self.apples.pop(index)
                    break


class Pests:
    def __init__(self, pests_type, pests_quantity):
        self.pests_type = pests_type
        self.pests_quantity = pests_quantity

    def kill(self):
        self.pests_quantity = 0


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants
        # self.pests = Pests

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    def poison_fruit_pests(self, insects: Pests):
        if insects.pests_quantity > 0:
            insects.kill()
            print('GREAT job done! There are no fruit insects in the garden now!')
        else:
            print('There are no fruit insects in the garden! You can have a rest!')

    # def poison_vegetable_pests(self, vegetable_pests):
    #     if vegetable_pests.pests_quantity:
    #         vegetable_pests.pests_quantity = 0
    #         print('GREAT job done! There are no vegetable insects in the garden now!')
    #     else:
    #         print('There are no vegetable insects in the garden! You can have a rest!')


# tomato_bush = TomatoBush(4, 3)

apple_tree = AppleTree(6)
fruit_pests = Pests('worm', 4)
# vegetable_pests = Pests('snail', 0)

# john = Gardener('John', [tomato_bush, apple_tree])
tom = Gardener('Tom', [apple_tree])

# garden = Garden(tomato_bush, apple_tree)
garden = Garden(fruits=apple_tree.apples, gardener=tom.name, fruit_insects=fruit_pests.pests_quantity)
garden.show_the_garden()

# print('There are', len(apple_tree.apples), 'apples in the garden!!!')
# print(f'There are {apple_tree.count_of_apples()} apples in the garden!')

# print('There are', len(tomato.tomatoes), 'tomatoes in the garden!!!')
# print(f'There are {tomatoes.count_of_tomatoes()} tomatoes in the garden!')

tom.work()
tom.work()
tom.work()


apple_tree.insects_attack(fruit_pests)

garden.show_the_garden()


# tom.poison_fruit_pests(fruit_pests)
# tom.poison_vegetable_pests(vegetable_pests)
# garden.show_the_garden()

#
# tom.poison_pests()
tom.harvest()
#

# Gardener.poison_pests(tom.plants)

# print(tomato.tomatoes)
# print(apple_tree.apples)
