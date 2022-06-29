class Customer:

    def __init__(self, id, nm, pc, qt):
        self.id = id
        self.name = nm
        self.price = pc
        self.qnt = qt

    def __str__(self):
        return str(self.id) + "," + self.name + "," + str(self.price) + "," + str(self.qnt)
