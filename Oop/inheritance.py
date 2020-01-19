class Phone : 
    def __init__(self, brand, model, price) : 
        self.brand = brand 
        self.model = model 
        self.price = price 

    def makeACall(self, phoneNumber) :
        print("Calling ", phoneNumber)

    def fullName(self) : 
        print("Full name : ", self.brand + " " + self.model)

class Smartphone(Phone) : 
    def __init__(self, brand, model, price, ram, internanMemory, rearCamera) : 
        # Phone.__init__(self, brand, model, price)   # Uncommon way

        super().__init__(brand, model, price)
        self.ram = ram 
        self.internalMemory = internanMemory 
        self.rearCamera = rearCamera

phone = Phone("Nokia", "1100", 1000)
smartphone = Smartphone("OnePlus", "5", 30000, "6 GB", "64 GB", "20 MP")

phone.fullName()
smartphone.fullName()