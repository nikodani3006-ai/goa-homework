score=int(input("Enter your score:"))
attendance=int(input("Enter your attendance:"))

if score >=80 and attendance >=90 :
 print("შენ შესანიშნავად დაწერე გამოცდა")
elif score >=50 and attendance >=70 :
 print("საშუალოდ დაწერე გამოცდა")
elif score >=30 and attendance >=50 :
 print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
 print("ჩაიჭერი!")