import time

my_dict = {"components" : {"roofbox_lidar" : 5, "roofbox_camera" : 4}}

def print_square_range(n):

    for i in range(n):
        print(i**2)

def foo(string):

    return string.split(" ")

print_square_range(9)

print(foo("Hej på dig"))

print(my_dict["components"]["roofbox_lidar"])

