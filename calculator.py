print("Sum of integers")
a = []
while True:
  i = int(input("Enter number: "))
  if i < 0:
    break
  a.append(i)

print(f"Total: {sum(a)}")
