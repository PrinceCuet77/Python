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
    def __init__(self, brand, model, price, ram, internalMemory, rearCamera) : 
        # Phone.__init__(self, brand, model, price)   # Uncommon way

        super().__init__(brand, model, price)
        self.ram = ram 
        self.internalMemory = internalMemory 
        self.rearCamera = rearCamera

    # Overriding fullName() method 
    def fullName(self) : 
        print("Full name : " + self.brand + " " + self.model + " " + str(self.price))

class FlagShipPhone(Smartphone) : 
    def __init__(self, brand, model, price, ram, internalMemory, rearCamera, frontCamera) : 
        super().__init__(brand, model, price, ram, internalMemory, rearCamera) 
        self.frontCamera = frontCamera

    def fullName(self) : 
        print("Full name : " + self.brand + " " + self.model + " " + str(self.price) + " " + str(self.ram))

phone = Phone("Nokia", "1100", 1000)
smartphone = Smartphone("OnePlus", "5", 30000, "6 GB", "64 GB", "20 MP")
oneplus = FlagShipPhone("OnePlus", "5", 30000, "6 GB", "64 GB", "20 MP", "16 Mp")

phone.fullName()
smartphone.fullName()
print()

phone.fullName()
smartphone.fullName()
oneplus.fullName()
print()

# isinstance(object, class)
print(isinstance(oneplus, FlagShipPhone))
print(isinstance(oneplus, Smartphone))  # True because FlagShipPhone inherits Smartphone
print(isinstance(phone, FlagShipPhone)) # False because phone is not an object of FlagShipPhone
print()

# issubclass(childclass, parentclass) 
print(issubclass(FlagShipPhone, Smartphone)) # FlagShipPhone inherit Smartphone
print(issubclass(Smartphone, FlagShipPhone)) # FlagShipPhone can't inherit Smartphone
print()

print(FlagShipPhone.__mro__)    # mro stands for Method Resulation Order. It shows the order of class assigned
print(FlagShipPhone.mro())      # Work same like before