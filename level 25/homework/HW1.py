#  შექმენი list: names = ["nika", "luka", "giorgi"] მომხმარებელს შეაყვანინე: ინდექსი და სახელი, insert()-ის გამოყენებით ჩასვი სახელი მითითებულ ადგილას და დაბეჭდე შედეგი
names = ["nika", "luka", "giorgi"]

index = int(input("Enter number between 0-2:"))
name = input("Enter random name:")

names.insert(index,name)

print(names)