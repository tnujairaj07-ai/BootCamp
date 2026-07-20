import numpy as np

# Generate 1000 random numbers between 1 and 500
numbers = np.random.randint(1, 501, 1000)
print("Random Numbers:")
print(numbers)



# 1. Count perfect squares
square_root = np.sqrt(numbers)
perfect_square_count = np.sum(square_root == square_root.astype(int))
print("\nNumber of Perfect Squares:", perfect_square_count)


# 2. Count prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
prime_count = np.sum([is_prime(x) for x in numbers])
print("Number of Prime Numbers:", prime_count)


# 3. Replace every multiple of 7 with its square root
new_numbers = numbers.copy()
new_numbers[new_numbers % 7 == 0] = np.sqrt(new_numbers[new_numbers % 7 == 0])
print("\nArray after replacing multiples of 7 with square root:")
print(new_numbers)


# 4. Find the largest gap between consecutive sorted values
sorted_numbers = np.sort(numbers)
gaps = np.diff(sorted_numbers)
largest_gap = np.max(gaps)
print("\nLargest Gap:", largest_gap)


# 5. Compute cumulative sum
cumulative_sum = np.cumsum(numbers)
print("\nCumulative Sum:")
print(cumulative_sum)


# 6. Find first index where cumulative sum exceeds 100000
index = np.argmax(cumulative_sum > 100000)
print("\nFirst index where cumulative sum exceeds 100000:", index)