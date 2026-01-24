# შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში ჩაამატეთ სახელი "NIKA", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი "GOGA", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.
names = ["nika","dato","KIRA","zviadi","Gela"]
words = []
for name in names:
     if name.lower() and name[0] == "d":
         words.append("NIKA")
     elif name.upper() or name[0] =="K":
         words.append("GOGA")
     else:
         words.append("LIDER") 
print(words)