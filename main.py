class Aquarium:
    def __init__(self):
        self.fish = []

    def addfish(self, fish):
        self.fish.append(fish)

    def feed(self):
        for i in self.fish:
            i.feed()

    def removefish(self):
        for number, i in enumerate(self.fish):
            if i.weight > 10:
                self.fish.pop(number)

    def getstatus(self):
        for i in self.fish:
            i.status()


class Fish:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color


class Clownfish(Fish):
    def __init__(self, name, weight, color, stripecolor):
        super(Clownfish, self).__init__(name, weight, color)
        self.stripecolor = stripecolor

    def feed(self):
        self.weight = self.weight + 1

    def status(self):
        print(self.name, self.weight, self.color)


class Tang(Fish):
    def __init__(self, name, weight, color, memoryloss):
        super(Tang, self).__init__(name, weight, color)
        self.memoryloss = memoryloss

    def feed(self):
        self.weight = self.weight + 1

    def status(self):
        print(self.name, self.weight, self.color)


class Kong(Fish):
    def __init__(self, name, weight, color):
        super(Kong, self).__init__(name, weight, color)

    def feed(self):
        self.weight = self.weight + 2

    def status(self):
        print(self.name, self.weight, self.color)


fishTank1 = Aquarium()
fish1 = Clownfish("Nemo", 10, "orange", "white")
fishTank1.addfish(fish1)
fish1.status()
fishTank1.feed()
fishTank1.getstatus()
