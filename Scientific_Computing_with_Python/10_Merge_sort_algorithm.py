"""In this project, you'll learn data structures by building the merge sort algorithm.
This is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data. 
That is, it 'divides' a collection into smaller sub-parts, and 'conquers' the sub-parts by sorting them independently, 
then merges the sorted sub-parts.

The merge sort algorithm mainly performs three actions:

Divide an unsorted sequence of items into sub-parts
Sort the items in the sub-parts
Merge the sorted sub-parts
The above happens recursively until the sub-parts are merged into the complete sorted sequence. Let's start by dividing the sequence."""

def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

    return array

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    print(f'Sorted array: {merge_sort(numbers)}')


# wersja chat GPT

def merge_sort(array):
    if len(array) <= 1:
        return array  # Zwracamy już posortowaną tablicę
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    left_part = merge_sort(left_part)  # Zmieniamy tutaj, aby przechować wynik rekurencji
    right_part = merge_sort(right_part)  # Zmieniamy tutaj, aby przechować wynik rekurencji

    # Łączenie dwóch posortowanych części
    sorted_array = []
    left_array_index = 0
    right_array_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            sorted_array.append(left_part[left_array_index])
            left_array_index += 1
        else:
            sorted_array.append(right_part[right_array_index])
            right_array_index += 1

    # Dodanie reszty elementów, jeśli występują
    sorted_array.extend(left_part[left_array_index:])
    sorted_array.extend(right_part[right_array_index:])

    return sorted_array  # Zwracamy wynik sortowania

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    print(f'Sorted array: {merge_sort(numbers)}')