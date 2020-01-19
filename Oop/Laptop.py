# Example : 01 
class Laptop : 
    discount_percentage = 10
    def __init__(self, brand_name, model_name, price) : 
        self.brand_name = brand_name 
        self.model_name = model_name 
        self.price = price 
        self.laptop_name = brand_name + ' ' + model_name

    def apply_discount(self) : 
        discount = self.price * (self.discount_percentage / 100.0)
        return self.price - discount

lap1 = Laptop('Hp', 'au114tx', 63000)

print(f'Brand name : {lap1.brand_name}')
print(f'Model name : {lap1.model_name}')
print(f'Laptop name : {lap1.laptop_name}')
print(f'Price : {lap1.price}')
print(f'With {lap1.discount_percentage}% discount : {lap1.apply_discount()} TK')
print()

lap2 = Laptop('Dell', 'Inspirion 14', 37000) 
lap2.discount_percentage = 50 
print(lap2.__dict__)                                                # Show the overview of the all the variables
print(f'With {lap2.discount_percentage}% discount : {lap2.apply_discount()} TK')