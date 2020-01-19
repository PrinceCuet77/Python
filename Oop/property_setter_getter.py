class Phone : 
    def __init__(self, brand, model, price) : 
        self.brand = brand 
        self.model = model 
        self._price = max(price, 0) 
        # self.complete_specification = f'{self.brand} {self.model} and Price : {self._price}' 

    # If I assign method as 'property' then no need to call it as method. It will be accessable like other property.
    @property
    def completeSpecification(self) : 
        return f'{self.brand} {self.model} and Price : {self._price}'

    # Use like getter method of '_price' instance variable
    @property
    def price(self) : 
        return self._price

    # @price.setter will be written after getter method. It named as @GetterMethod.setter to set the instance variable
    # Here GetterMethod in Line 15 is 'price' so @price.setter will be my setter method 
    @price.setter
    def price(self, newPrice) : 
        self._price = max(0, newPrice)

    def makeACall(self, phoneNumber) : 
        print("Calling number ...", phoneNumber)

    def fullName(self) : 
        print("Full name : ", self.brand + " " + self.model)

phone1 = Phone('Nokia', '1100', -1000)
phone1.price = -500     # Calling price(self, newPrice) method which is getter method

print(f'Brand                  : {phone1.brand}')
print(f'Model                  : {phone1.model}')
print(f'Price                  : {phone1.price}')       # Calling price(self) method which is getter method
print(f'Complete Specification : {phone1.completeSpecification}')