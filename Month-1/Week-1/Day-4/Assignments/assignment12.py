def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

# Example
nums = [3, -2, 5, 0, -1, 8]
print(count_positive(nums))