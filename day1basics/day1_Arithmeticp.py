def multiplication_or_sum(num1, num2):
    # Calculate product
    product = num1 * num2
    
    # Check if product is within the threshold
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Testing Case 1
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Testing Case 2
result = multiplication_or_sum(40, 30)
print("The result is", result)
 