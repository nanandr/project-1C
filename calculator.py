print("Dividing integers")
a = []
res = 1
while True:
  i = int(input("Enter number: "))
  if i < 0:
    break
  a.append(i)

for val in a:
  res = res / val

print(f"Total: {res}")
