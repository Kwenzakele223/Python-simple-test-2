def count_items(items):
    # TODO: Return the number of items in the list
    list_items = []
    for i in items:
        list_items.append(i)
        item_count = len(list_items)
    if list_items == []:
        return 0
    return item_count
    

def sum_numbers(numbers):
    # TODO: Return the sum of all numbers in the list
    list_item = []
    for i in numbers:
        list_item.append(i)
        item_sum = sum(list_item)
    if  list_item == []:
        return 0
    return item_sum

def find_largest(numbers):
    # TODO: Return the largest number in the list
    larger_num = max(numbers)
    return larger_num

def count_even_numbers(numbers):
    # TODO: Return the count of even numbers in the list
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count = count + 1
    return count

def sum_digits(number):
    # TODO: Return the sum of digits in the given number
    str_num = str(number)
    list_num = list(str_num)
    count = 0
    for i in number:
       
       count = count + i
    return count
   

def count_vowels(string):
    # TODO: Return the count of vowels in the string (case-insensitive)
    vowels = 'AEIOUaeiou'
    count = 0

    for i in string:
        if i in vowels:
            count += 1
    return count

def multiply_list_elements(numbers):
    # TODO: Return the product of all elements in the list
    count = 1
    for i in numbers:
        count = count * i
    return count

def create_number_triangle(n):
    # TODO: Return a list of strings representing a number triangle
    # Example for n=3: ['1', '22', '333']
    pass

def fibonacci_sequence(n):
    # TODO: Return a list of first n Fibonacci numbers
    fib_list = [0, 1]
    for i in range(n):
        fib_list[-1] + fib_list[-2]
        fib_list.append(i)
        
    return fib_list

def remove_vowels(string):
    # TODO: Return the string with all vowels removed
    pass

def create_multiplication_table(n):
    # TODO: Return a 2D list representing multiplication table up to n
    pass

def count_character_frequency(string):
    # TODO: Return a dictionary with character frequencies
    pass

def reverse_words(sentence):
    # TODO: Return the sentence with each word reversed
    pass

# print(count_items([]))
# print(sum_numbers([]))
# print(find_largest([0]))
# print(count_even_numbers([2,4,6,8]))
# print(sum_digits(123))
# print(count_vowels('streing'))
# print(multiply_list_elements([1, 2, 3, 4])