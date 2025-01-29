a=10
b=5
sum=a+b
difference=a - b
product=a* b
divison=a/b

print("Sum:",sum)
print("Difference:",difference)
print("Product:",product)
print("Divison:",divison)

print(f"The sum of the two numbers {a} and {b} is {sum}")

x=13//2
print(x)
y=13%2
print(y)

#Boolean variables and comparisons
x = 10
y = 5

is_greater = x>y
is_equal = x==y
is_not_equal = x!=y

print("is x greater than y?",is_greater)
print("is x equal to y?",is_equal)
print("is x not equal to y?",is_not_equal)

#Variable assignment
name = "Alaa"
age = 55
is_professor = True

print(f"{name}'s age is {age}. He is a Professor is {is_professor}")

#Defining and using a function
def greet(name):
    return "Hello, "+name+"!"

my_name=input("Enter your name: ")
print(greet(my_name))

def add_number(a,b):
    return a+b

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))

addition_value = add_number(a,b)
print(f"The result of addition for {a}, {b} is {addition_value}")

message = "Hello, World"
length = len(message)
uppercase = message.upper()
lowercase = message.lower()
substring = message[7:12]

print("Original message: ", message)
print("The length is: ", length)
print("Upper case: ", uppercase)
print("Lower case: ", lowercase)
print("Part of the message is: ", substring)

#Basic input example
Last = input("Enter the last name: ")
First = input("Enter the first name: ")

print(f"{Last}, {First}")

#Numeric input example
age = int(input("Enter your age: "))
print("You will be", age+1,"years old next year.")

#Calculations with input
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
sum_result = num1 + num2
print("Sum:", sum_result)

#String concatenation with input
city = input("Enter your city: ")
country = input("Enter your country: ")
location = city+","+country
print("You are in:", location)

#Multiple inputs
name, age = input("Enter your name and age seperated by space:").split()
print(f"my name is {name} and my age is {age}")
