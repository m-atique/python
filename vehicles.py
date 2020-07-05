class Vehicles():
    def __init__(self,kind,engine,color,make,modal):
        
        self.kind = kind
        self.engine =  engine
        self.color = color
        self.make = make
        self.modal =modal
    def run():
        print(f"The vehicle is running")
    def kind_getter(self):
        print(f"The type of vehicle is {self.kind}")
    def kind_setter(self):
        self.kind = input("plasae enter new kind")
        print(f"new type of vehicle is {self.kind}")
        
    def color_getter(self):
        print(f"The color of vehicle is {self.color}")
    def color_setter(self):
        self.color = input("plasae enter new color")
        print(f"new color of vehicle is {self.color}")
        