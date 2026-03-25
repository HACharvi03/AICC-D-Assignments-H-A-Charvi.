#1.Check if number is odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 2.Reversal of numbers
print("Numbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# 3.Break statement
while True:
    val = int(input("Enter a number (0 to stop): "))
    if val == 0:
        break
    total_sum += val

print(f"The final sum is: {total_sum}")