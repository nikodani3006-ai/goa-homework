#  შექმენი ცარიელი სია. მომხმარებელს შეაყვანინე რიცხვები სანამ "stop"-ს არ დაბეჭდავს, ყოველი ახალი რიცხვი: თუ ნაკლებია 50-ზე → ჩასვი სიის დასაწყისში (insert), თუ მეტია ან ტოლია 50-ის → დაამატე ბოლოში (append), ბოლოს დაბეჭდე სია
list = []

while True:
     numbers = input("Enter random numbers:")
     if numbers == "stop":
          break
     nums = int(numbers)
     if nums < 50:
         list.insert(nums,nums)
     else:
         list.append(nums)
print(list)
