# Generating Evens Exercise

# Write a function called generate_evens  that returns a list of the even numbers between 1 and 50(not including 50). 
# Basically, it should return a list: [2,4,6....all the way up to 48] 
# Inside the function, you can construct the list using either a loop OR list comprehension.
num_list = [num for num in range(2,50) if num % 2 == 0]
print(num_list)

def generate_evens():
    return(num_list)


# Generating evens using a loop:

# def generate_evens():
#     result = []
#     for x in range(1,50):
#         if x % 2 == 0:
#             result.append(x)
#     return result


