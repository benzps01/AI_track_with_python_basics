def mean(num_list):
    return sum(num_list) / len(num_list)


def add_five(num_list):
    return [n + 5 for n in num_list]


# if __name__ == '__main__':
#     print("Testing mean function")
#     n_list = [34, 44, 23, 46, 12, 24]
#     correct_mean = 30.5
#     assert mean(n_list) == correct_mean

#     print("Testing add_five function")
#     correct_list = [39, 49, 28, 51, 17, 29]
#     assert add_five(n_list) == correct_list

#     print("All tests_passed!")

"""
There is another way to run the __main__ block.
"""


def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert mean(n_list) == correct_mean

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert add_five(n_list) == correct_list

    print("All tests_passed!")


"""
This basically means that whenever useful_functions.py will be run 
the code specified below will be executed and if another script call this script,
then it will be able to access only this script's methods. This is because of 
if __name__ == '__main__: section.
"""
if __name__ == "__main__":
    main()
