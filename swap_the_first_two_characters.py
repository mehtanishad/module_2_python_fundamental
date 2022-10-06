# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap(string):
    start = string[0]
    end = string[-1]
     
    swapped_string = end + string[1:-1] + start
    print(swapped_string)
    
swap("tops technology")
swap("Python")
