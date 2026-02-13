class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0.")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут повинен бути в межах (0, 180).")
            
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("Кут_b обчислюється автоматично і не може задаватися вручну.")

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб: сторона = {self.side_a}, кут_a = {self.angle_a}, кут_b = {self.angle_b}"