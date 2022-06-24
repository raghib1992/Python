# class inheritence allow one class to take method and properties to take from another class

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"device {self.name!r} is connected by ({self.connected_by})"

    def disconnected(self):
        self.disconnected = False
        print("Your device is disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} pages remaining"

    def print(self, pages):
        if not self.connected:
            print("your printer is not connected")
            return
        print("printing {pages} pages")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()

"""
device = Device("Speaker", "Bluetooth")
print(device)
device.disconnected()
"""