"""List Comprehension is a way to construct a new Python list from an iterable types: lists, tuples, and strings. All without using a for loop or the `.append()` list method.
In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.
The project has two phases: first you'll use a for loop to implement the program. Then you'll learn how to use List Comprehension instead of a loop to achieve the same results.

In Python, a list comprehension is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition. Apart from being briefer, list comprehensions often run faster.
A basic list comprehension consists of an expression followed by a for clause:
spam = [i * 2 for i in iterable]
The above uses the variable i to iterate over iterable. Each elements of the resulting list is obtained by evaluating the expression i * 2 at the current iteration."""

# snake_cased_char_list = []

    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)

    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string

def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))
