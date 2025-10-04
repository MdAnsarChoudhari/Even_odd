numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_count = 0
odd_count = 0
prime_count = 0


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if is_prime(num):
        prime_count += 1

print("Total numbers:", len(numbers))
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Prime numbers:", prime_count)