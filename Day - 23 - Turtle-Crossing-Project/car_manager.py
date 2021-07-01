from turtle import Turtle
import random
COLORS = ["red", "orange", "firebrick", "green", "blue", "purple", "violet", "indigo"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Generates cars randomly along Y-axis
    def create_car(self):
        # Slowing down a little bit the creating of cars
        # Here it means every 6 times while loop runs(main.py),then a new car will be generated
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-260, 270)
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)

    # Moving randomly generated cars
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up_speed(self):
        self.car_speed += MOVE_INCREMENT

    # Removing blocks from the left side i.e. X-axis(-ve)
    def remove_cars(self):
        for car in range(len(self.all_cars)-1):
            if self.all_cars[car].xcor() < -320:
                self.all_cars[car].hideturtle()
                self.all_cars.pop(car)
                print(len(self.all_cars))
