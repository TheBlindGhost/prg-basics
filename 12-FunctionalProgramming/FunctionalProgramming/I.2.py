# takes two numbers from keyboard
n1 = int(input("Type number one"))
n2 = int(input("Type number two"))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')