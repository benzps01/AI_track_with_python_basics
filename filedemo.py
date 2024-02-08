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

f = open("another_file.txt", "w")
f.write("Hello This is a new file!")
f.close()
