# შექმენი list: nums = [1, 2, 3, 4] მომხმარებელს შეაყვანინე: ინდექსი და რიცხვი, თუ ინდექსი list-ის საზღვრებშია გამოიყენე insert() ჩასამატებლად, თუ ინდექსი ლისტზე დიდია მაშინ გამოიყენე append()
nums = [1, 2, 3, 4]

index = int(input("Enter random index:"))
number = int(input("Enter random number:"))
if 0 >= index:
     print(nums.insert(index,number))
else:
     print(nums.append(number))