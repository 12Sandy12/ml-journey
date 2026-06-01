import time as T 
import functools 



# =======================================
# def greeting(name ):
#     print(f"Hi {name} ")


# # assiging function to a variable
# run_once = greeting
# run_once("Jarvis")

# # Passing function as a parameter
# def run_twice(function, name):
#     i = 0
#     while(i <= 1):
#         function(name)
#         i += 1

# run_twice(greeting,"Jarvis")
# =======================================



# =======================================
# timer decorator function
# def timer(func):
#     def wrapper(*args, **kwargs):
#         initial_time = T.time()
#         func(*args, **kwargs)
#         final_time = T.time()
#         print(f"Time taken: {final_time - initial_time} seconds")
#     return wrapper

# # original function identity/behaviour is wrapped from now onwards in this case 
# @timer
# def greeting(name ):
#     print(f"Hi {name} ")
# greeting("Jarvis")
# =======================================


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} kwargs {kwargs}")
        func(*args, **kwargs)
    return wrapper


@logger

def greeting(name ):
    print(f"Hi {name} ")
greeting("Sandesh")        # args
greeting(name="Sandesh")   # kwargs

