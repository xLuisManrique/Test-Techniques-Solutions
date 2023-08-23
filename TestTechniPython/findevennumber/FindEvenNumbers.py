def find_even_numbers(numbers_list):
    even_numbers = []
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
input_list = [1,2,3,4,5,6,7,8,9,10]
result = find_even_numbers(input_list)
print(result)