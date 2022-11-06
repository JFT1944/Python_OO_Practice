"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, starter):
        self.starter = starter
        self.origin = starter

    def generate(self):
        
        print (self.starter)
        a = self.starter
        b = self.starter + 1
        self.starter = b
        print (self.starter)
        return (a)

    def reset(self):
        self.starter = self.origin
        return self.origin





seriel = SerialGenerator(starter=100)
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.generate())
print(seriel.reset())