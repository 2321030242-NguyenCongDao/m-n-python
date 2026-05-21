class Circle:

    Pi = 3.141592

    def __init__(self, radius=1):
        self.bk = radius

    def Dien_tich(self):
        return self.bk * self.bk * Circle.Pi


c = Circle(5)

print("Diện tích hình tròn là:", c.Dien_tich())
