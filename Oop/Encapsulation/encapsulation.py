# Encapsulation means data hiding making data as private(__instanceVariableName)
class Phone : 
    def __init__(self, brand, model, price) : 
        self.brand = brand 
        self._model = model                                      # Teated like private instance
        self.__price = price                                     # Name mangling acts as private instance variable                      

    def make_a_call(self, number) : 
        print(f'Calling {number} ...')

    def full_name(self) : 
        print(f'{self.brand} {self.model}')

# convension : self._price = price (_price is treated like private instance) 

phone1 = Phone('Nokia', '1100', 2000)
print(phone1.__dict__)