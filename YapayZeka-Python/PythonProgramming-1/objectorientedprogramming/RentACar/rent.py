import datetime


class VehicleRent:

    def __init__(self, stock):
        self.stock = stock
        self.now = 0

    def display_stock(self):
        print("{} vehicle available to rent".format(self.stock))
        return self.stock

    def rent_hourly(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) for hourly at {} hours".format(
                n, self.now.hour))
            self.stock -= n
            return self.now

    def rent_daily(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) for daily at {} hours".format(
                n, self.now.hour))
            self.stock -= n
            return self.now

    def return_vehicle(self, request, brand):
        car_hourly_price = 10
        car_daily_price = car_hourly_price * 8 / 10 * 24
        bike_hourly_price = 5
        bike_daily_price = bike_hourly_price * 7 / 10 * 24

        rental_time, rental_basis, num_of_vehicle = request
        bill = 0

        if brand == "car":
            if rental_time and rental_basis and num_of_vehicle:
                self.stock += num_of_vehicle
                now = datetime.datetime.now()
                rental_period = now - rental_time

                if rental_basis == 1:  # hourly
                    bill = rental_period.seconds / 3600 * car_hourly_price * num_of_vehicle

                elif rental_basis == 2:  # daily
                    bill = rental_period.seconds / \
                        (3600 * 24) * car_daily_price * num_of_vehicle

                if 2 <= num_of_vehicle:
                    print("You have extra 20% discount")
                    bill *= 0.8

                print("Thank you for returning your car")
                print("Price: $ {}".format(bill))
                return bill
        elif brand == "bike":
            if rental_time and rental_basis and num_of_vehicle:
                self.stock += num_of_vehicle
                now = datetime.datetime.now()
                rental_period = now - rental_time

                if rental_basis == 1:  # hourly
                    bill = rental_period.seconds / 3600 * bike_hourly_price * num_of_vehicle

                elif rental_basis == 2:  # daily
                    bill = rental_period.seconds / \
                        (3600 * 24) * bike_daily_price * num_of_vehicle

                if 4 <= num_of_vehicle:
                    print("You have extra 20% discount")
                    bill *= 0.8

                print("Thank you for returning your bike")
                print("Price: $ {}".format(bill))
                return bill
        else:
            print("You do not rent a vehicle")
            return None


class CarRent(VehicleRent):

    global discount_rate
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)

    def discount(self, b):
        bill = b - (b * discount_rate) / 100
        return bill


class BikeRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)


class Customer:

    def __init__(self):
        self.bikes = 0
        self.rental_basis_b = 0
        self.rental_time_b = 0

        self.cars = 0
        self.rental_basis_c = 0
        self.rental_time_c = 0

    def request_vehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")

            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be Number")
                return -1

            if bikes < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent?")

            try:
                cars = int(cars)
            except ValueError:
                print("Number should be Number")
                return -1

            if cars < 1:
                print("Number of cars should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars

        else:
            print("Request vehicle error")

    def return_vehicle(self, brand):
        if brand == "bike":
            if self.rental_time_b and self.rental_basis_b and self.bikes:
                return self.rental_time_b, self.rental_basis_b,  self.bikes
            else:
                return 0, 0, 0
        elif brand == "car":
            if self.rental_time_c and self.rental_basis_c and self.cars:
                return self.rental_time_c, self.rental_basis_c,  self.cars
            else:
                return 0, 0, 0
        else:
            print("Return vehicle Error")
