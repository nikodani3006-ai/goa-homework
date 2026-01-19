# მომხმარებელს შემოატანინე რაიმე სტრინგი,შენი დავალებაა დაითვალო თუ რამდენი ცალი ხმოვანი და რამდენი ცალი თანხმოვანი გვხვდება მის მიერ შემოყვანილ სტრინგში
vowel = 0
consonant = 0

words = ["a","e","i","o","u"]

wordss = input("Enter random word:")

for word in words:
     if len(wordss) == len(word):
         vowel = vowel + 1
     else:
         consonant = consonant + 1
print(vowel,consonant)
     
          