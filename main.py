class Aquarium:
    def __init__(self):
        self.fish = []

    def addFish(self, fish):
        self.fish.append(fish)

    def feed(self):
        for i in self.fish:
            i.feed()

    def removeFish(self):
        for number, i in enumerate(self.fish):
            if i.weight > 10:
                self.fish.pop(number)

    def getStatus(self):
        for i in self.fish:
            i.status()


class Fish:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color


class Clownfish(Fish):
    def __init__(self, name, weight, color, stripeColor):
        super(Clownfish, self).__init__(name, weight, color)
        self.stripeColor = stripeColor

    def feed(self):
        self.weight = self.weight + 1

    def status(self):
        print(self.name, self.weight, self.color)



fishTank1 = Aquarium()
fish1 = Clownfish("Nemo", 10, "orange", "white")
fishTank1.addFish(fish1)
fish1.status()
fishTank1.feed()
fishTank1.getStatus()