#1
def welcome():
    print("Welcome to Python")
welcome()

#2
def greet(name):
    print(name)
greet('hello')

#3
def square(n):
    return n*n
print(square(2))

#4
def calculator(a,b):
    return a+b, a-b, a*b
print(calculator(2,3))

#5
def country(name='India'):
    print('I am from',name)
country()

#6
def total(*nums):
    return sum(nums)
print(total(1, 2, 3))

#7
def student_info(**data):
    for k in data:
        print(k, ":", data[k])
student_info(name="Riya", age=20)

#8
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
print(count_vowels("HELLO"))

#9
cube = lambda n: n**3
print(cube(3)) 

#10
def unique_letters(text):
    u = ""
    for ch in text:
        if ch not in u:
            u += ch
    return u
print(unique_letters("mississippi"))  
