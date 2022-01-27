# Task 7

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * self.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}"


my_complex_1 = Complex(2, 4)
my_complex_2 = Complex(-5, 2)

print(f'Сумма: {my_complex_1 + my_complex_2}')
print(f'Произведение: {my_complex_1 * my_complex_2}')