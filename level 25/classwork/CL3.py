# ; შექმენი list, numbers = [10, 20, 30, 40, 50], მომხმარებელს ჰკითხე ინდექსი და pop()-ით წაშალე შესაბამისი ელემენტი
# ; დაბეჭდე:
# ; წაშლილი ელემენტი
# ; განახლებული list

numbers = [10, 20, 30, 40, 50]

idk = int(input("Enter random number:"))

gg =numbers.pop(idk)

print("deleted index",gg)
print("New list",numbers)
