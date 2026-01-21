#  შექმენით ქვეყნების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა სიტყვას ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო შედეგი. გამოიყენეთ while ციკლი.

words = ["GEORGIA","usa","Spain","Jamaica","india"]

i = 0

while i < len(words):
     if words[i].isupper:
         words.pop(i)
         i = i + 1
     else:
         words.upper(i)
print(words)