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
    list_digit = []
    for i in list_num:
        list_digit.append(int(i))
        sum_digit = sum(list_digit)
      
    return sum_digit

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
    string_number = str(n)
    string_list = list(string_number)
    # count = 1
    list_string = []
    for i in range(n, 0, -1):
        count = str(i) * n
        n = n-1
        list_string.append(count)
    return list_string[::-1]

def fibonacci_sequence(n):
    # TODO: Return a list of first n Fibonacci numbers
    fib_list = [0,1]
    for i in range(2,n):
            fib = fib_list[-1] + fib_list[-2]
            fib_list.append(fib)
        
    return fib_list

def remove_vowels(string):
    # TODO: Return the string with all vowels removed
    vowels = 'aeiouAEIOU'
    con = ''
    for strng in string:
        if strng not in vowels:
            con += strng
            vowels.strip()
            
    return con



  

def create_multiplication_table(n):
    # TODO: Return a 2D list representing multiplication table up to n
    table = []
    for x in range(1, n+1):
        x_table =[]
        for y in range(1, n+1):
            x_table.append(x*y)
        table.append(x_table)
    return table

def count_character_frequency(string):
    # TODO: Return a dictionary with character frequencies
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

    

def reverse_words(sentence):
    # TODO: Return the sentence with each word reversed
    reversed_str = sentence[::-1]
    string = str(reversed_str)
    converted_str = string.split()
    change_str =converted_str[::-1]
    return ' '.join(change_str)
  

# print(count_items([1,2,3,4]))
# print(sum_numbers([3,5,2]))
# print(find_largest([3,5,7,8]))
# print(count_even_numbers([2,4,6,8]))
# print(sum_digits(123))
# print(count_vowels('streing'))
# print(multiply_list_elements([1, 2, 3, 4]))
# print(reverse_words('hello world'))
# print(count_character_frequency('hello'))
# print(fibonacci_sequence(8))
print(remove_vowels('hello'))
print(create_number_triangle(4))
print(count_character_frequency('hello'))
print(create_multiplication_table(3))