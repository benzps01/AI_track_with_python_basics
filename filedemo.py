# f = open("some_file.txt")
# file_data = f.read()
# f.close()

# print(file_data)

"""This is to demonstate the effects of not including f.close() to close the files
or the file handle will be filled up and no more files could be accessed."""
# files = []
# for i in range(10000):
#     files.append(open("some_file.txt", "r"))
#     print(i)

""" 'w' mode deletes the previous entry from the files.
To add new data to the existing file use append mode."""
# f = open("another_file.txt", "w")
# f.write("Hello This is a new file!")
# f.close()

""" using with automatically closes file if one forgets to close a file. i.e. 
the file is closed after the intended block of code is executed.
The con here is that 'f' here is a local scope. but we can utilize the file_data variable"""
with open("another_file.txt", "r") as f:
    file_data = f.read()
print(file_data)
