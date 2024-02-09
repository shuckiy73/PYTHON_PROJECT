class Celsius:
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

    @property
    def fahrenheit(self):
        return (self.value * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.value = (float(value) - 32) * 5/9


c = Celsius()
print(c.value)
print(c.fahrenheit)
c.value = 100.0
print(c.fahrenheit)
c.fahrenheit = 50.0
print(c.value)
