class Phone:
    def __init__ (self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def battery_life (self):
        if self.battery >= 4000:
            return "Excellent battery life"
        elif self.battery >= 3000:
            return "Good battery life"
        elif self.battery >= 2000:
            return "Average battery life"
        else:
            return "Poor battery life"
    


if __name__ == "__main__":

    phone1 = Phone("Samsung", "Galaxy S21", 4000)

    print (phone1.brand)
    print (phone1.model)
    print (phone1.battery)
    print (phone1.battery_life())



    