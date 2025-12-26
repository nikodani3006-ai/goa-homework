# შექმენი ცარიელი სია, for ციკლით 1 დაან 10-მდე დაამატე სიაში რიცხვები, remove-ის გამოყენებით წაშალე ყველა კენტი რიცხვი  და ბოლოს დაბეჭდე საბოლოო სია]~

list = []


for i in range(0,11):
     list.append(i)

for i in list:
      if i % 2 != 0:
         list.remove(i)
print(list)