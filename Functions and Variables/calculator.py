# calculator program
def main(): 
    x = float(input("What is x? "))
    y = float(input("What is y? "))
    print(addition(x, y))
    x_squared = int(input("What is the number you want to square? "))
    print(f"{x_squared} squared is", square(x_squared))
    x = float(input("What is x? "))
    y = float(input("What is y? "))
    print(multiply(x, y))
    x = float(input("What is x? "))
    y = float(input("What is y? "))
    print(divide(x, y))
    
def addition(x,y): 
    return x + y

def square(n): 
    return n * n
 
def multiply(x,y): 
    return x * y

def divide(x,y): 
    return x / y

main()

# this might look a little complicated but we can use if else statements to see what the operation the user wants to perform