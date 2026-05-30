# odd and even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num) 
print("Even numbers in the list:", even_numbers)
print("Odd numbers in the list:", odd_numbers)