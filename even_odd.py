numbers=list(map(int, input("Enter numbers separated by space: ").split()))

even_count=0
odd_count=0

for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Total numbers:",len(numbers))
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)
