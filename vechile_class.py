class Vechile:

    def __init__(self, vechile_number, brand, model, rental_price_per_day):
        self.vechile_number = vechile_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    @staticmethod
    def validate_days(days):
        return days > 0

    def calculate_rent(self, days):

        if not Vechile.validate_days(days):
            return "Invalid rental duration. Days must be greater than zero."

        return self.rental_price_per_day * days

    def display_vechile(self):
        print(f'-----Vechile Details--------------')

        print(f'Vechile Number: {self.vechile_number}')
        print(f'Brand : {self.brand}')
        print(f'Model : {self.model}')
        print(f'Rental_Price_Per_Day : {self.rental_price_per_day}')


class Car(Vechile):

    def __init__(self, vechile_number, brand, model, rental_price_per_day, number_of_seats):
        super().__init__(vechile_number, brand, model, rental_price_per_day)
        self.number_of_seats = number_of_seats

    def display_vechile(self):
        super().display_vechile()
        print(f'Number Of Seats : {self.number_of_seats}')


class Bike(Vechile):

    def __init__(self, vechile_number, brand, model, rental_price_per_day, engine_capacity):
        super().__init__(vechile_number, brand, model, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_vechile(self):
        super().display_vechile()
        print(f'Engine Capacity : {self.engine_capacity} cc')


if __name__ == '__main__':

    # Create 2 Cars Object
    car1 = Car('car101', 'toyota', 'Innova', 2500, 7)
    car2 = Car('car102', 'Hyundai', 'Creta', 2000, 5)

    # Create 2 Bikes Object
    bike1 = Bike('Bike101', 'Honda', 'Shine', 800, 125)
    bike2 = Bike('Bike102', 'Royal Enfield', 'classic 350', 1200, 350)

    # Display Car
    car1.display_vechile()
    print(f'Rent for 3 days : {car1.calculate_rent(3)}Rs')

    car2.display_vechile()
    print(f'Rent for 4 days : {car2.calculate_rent(4)}Rs')

    # Display Bike
    bike1.display_vechile()
    print(f'Rent for 4 days : {bike1.calculate_rent(4)}Rs')

    bike2.display_vechile()
    print(f'Rent for 7 days : {bike2.calculate_rent(7)}Rs')

    # Test Invalid rental duration
    print('\n-----------Validation Test---------------')
    print(f'Car rent for 0 days : {car1.calculate_rent(0)}')
    