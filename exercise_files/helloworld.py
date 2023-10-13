
# My first Hellow world on Python 👍😊

#print('Hello, world!')

class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Pelitos')
my_dog2 = Dog('Panquecito')
my_dog3 = Dog('Mazpán')
# my_dog.speak()
# my_dog2.speak()
# my_dog3.speak()

def factorial(num): 
    multiplication = 1

    if num in [0,1]: return 0
    elif (type(num)!=int) or (num < 0): return 'You must enter positive integer numbers.'

    for i in range(1,num+1):
        multiplication = multiplication*i
    return multiplication

#print(factorial(6))

def factorialRecur(num):
    if (type(num)!=int) or (num < 0): return 'You must enter positive integer numbers.'
    if num in [0,1]: return 1

    return num * factorialRecur(num-1)

print(factorialRecur(5))
