class Sheep:
    sound = 'бе бе'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say(self):
        print(self.sound)

    def feeding(self):
        print('Вы покормили', self.name)

    def shearing(self):
        print('Вы постригли', self.name)


class Goose:
    sound = 'га га'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say(self):
        print(self.sound)

    def feeding(self):
        print('Вы покормили', self.name)

    def collect_eggs(self):
        print('Вы собрали яйца у ', self.name)


class Chicken:
    sound = 'ко ко'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say(self):
        print(self.sound)

    def feeding(self):
        print('Вы покормили', self.name)

    def collect_eggs(self):
        print('Вы собрали яйца у ', self.name)


class Duck:
    sound = 'кря кря'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say(self):
        print(self.sound)

    def feeding(self):
        print('Вы покормили', self.name)

    def collect_eggs(self):
        print('Вы собрали яйца у ', self.name)


class Cow:
    sound = 'му му'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say(self):
        print(self.sound)

    def feeding(self):
        print('Вы покормили', self.name)

    def milk(self):
        print('Вы подоили', self.name)


class Goat:
    sound = 'бе бе'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say(self):
        print(self.sound)

    def feeding(self):
        print('Вы покормили', self.name)

    def milk(self):
        print('Вы подоили', self.name)