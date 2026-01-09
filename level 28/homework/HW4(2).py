#  მომხმარებელს შემოაყვანინე 5 რიცხვი, დაბეჭდე მათი ჯამი. გამოიყენე for loop და while loop.

result = 0
i = 0

while i < 5:
     number = int(input("Enter random number:"))
     result += number
     i = i + 1
print(result)