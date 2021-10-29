#       Recursion
#This concept refers to a function calling itself.

def function():
    function()

#function()

# When we run a function we allocate stack memory space and if there is no space left, this is called Stack Overflow.

#       Factorial calculation

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n - 1)
        return number


print(factorial(5))