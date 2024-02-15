class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

car = Point(10, 20)
car.move()


artist = Point(3,4)
artist.draw()


car.x = "Hyndai"
print(car.x)

artist.y = "Leanardo de Vinci"
print(artist.y)

man = Point("Great", 4)
print(man.x)