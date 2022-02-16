import time


class Pack:
    def __init__(self, material, tightness, Pvolume, expiration):
        if type(material) == str:
            self.material = material
            print("material:", material)
        if type(tightness) == bool:
            if tightness == True:
                self.tightness = tightness
                print("tightness:", 'yes')
            else:
                print("tightness:", 'no')
        if type(Pvolume) == int or type(Pvolume) == float:
            self.Pvolume = Pvolume
            print("volume:", Pvolume, "liters")
        if type(expiration) == int:
            self.expiration = expiration
            print("expires in", expiration, "days")


p = Pack('cardboard', True, 2, 20)
print()


class Product:
    def __init__(self, expiration_date, weight, recommended_temperature, current_temperature):
        if type(expiration_date) == int:
            self.expiration_date = expiration_date
            print("expires in", expiration_date, "days")
        if type(weight) == int or type(weight) == float:
            self.weight = weight
            print("weight:", weight, "kilograms")
        if type(recommended_temperature) == int or type(recommended_temperature) == float:
            self.recommended_temperature = recommended_temperature
            print("recommended temperature:", recommended_temperature, "celsius")
        if type(current_temperature) == int or type(current_temperature) == float:
            self.current_temperature = current_temperature
            print("current temperature:", current_temperature, "celsius")


pr = Product(30, 1.5, 25, 18)
print()


class Milk(Product):
    def __init__(self, heat_treatment, fat_percent, volume, expiration_date, weight, recommended_temperature,
                 current_temperature):
        super().__init__(expiration_date, weight, recommended_temperature, current_temperature)
        if type(heat_treatment) == str:
            self.heat_treatment = heat_treatment
            print("heat_treatment:", heat_treatment)
        if type(volume) == int or type(volume) == float:
            self.volume = volume
            print("heat_treatment:", heat_treatment)
        if type(fat_percent) == int:
            self.fat_percent = fat_percent
            print("fats:", str(fat_percent) + "%")

    def mgnov_past(self):
        time.sleep(2)
        self.heat_treatment = 'sterilized'
        self.expiration_date += 3

    def fast_past(self):
        time.sleep(10)
        self.heat_treatment = 'pasterized'
        self.expiration_date += 7

    def long_past(self):
        time.sleep(20)
        self.heat_treatment = 'ultrapasterized'
        self.expiration_date += 14

    def info(self):
        print("heat_treatment:", self.heat_treatment)
        print("fats:", str(self.fat_percent)+"%")
        print("volume:", str(self.volume), 'liters')
        print("expiration date:", self.expiration_date)
        print("recommended temperature:", self.recommended_temperature)
        print("current temperature:", self.current_temperature)

    def separation(self):
        if self.volume >= 1:
            self.volume -= 1
            pm = Packed_Milk(self.heat_treatment, self.fat_percent, 1, self.expiration_date, self.weight, self.recommended_temperature,
                 self.current_temperature, 'cardboard', True, 2, 20)
            return pm

m = Milk("", 25, 50, 28, 1.2, 12, 15)
print()
m.info()
print()
m.mgnov_past()
m.info()
print()


class Packed_Milk(Milk, Pack):
    def __init__(self, heat_treatment, fat_percent, volume, expiration_date, weight, recommended_temperature,
                 current_temperature, material, tightness, Pvolume, expiration):
        Milk.__init__(self, heat_treatment, fat_percent, volume, expiration_date, weight, recommended_temperature,
                 current_temperature)
        Pack.__init__(self, material, tightness, Pvolume, expiration)


array = []
array.append(m.separation())
print(array)
