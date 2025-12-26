# შექმენი ცარიელი list მომხმარებელს შემოაყვანინე რიცხვები მანამ სანამ არ დაწერს "stop", ყველა რიცხვი დაამატე ლისთში append()ის გამოყენებით და საბოლოოდ დაბეჭდე ლისთი
list = []

while True:
     nums = input("Enter random numbers:")
     if nums == "stop":
          break 
     list.append(int(nums))
print(list)
