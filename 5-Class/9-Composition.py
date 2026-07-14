class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # ترکیب

    def start(self):
        print("Starting the car...")
        self.engine.start()

c = Car()
c.start()




# tamrin

class Battery:
    def charge(self):
        print("Battery charging...")

class Phone:
    def __init__(self):
        self.battery = Battery()

    def power_on(self):
        print("Phone is turning on...")
        self.battery.charge()


p = Phone()
p.power_on()
