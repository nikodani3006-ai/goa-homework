# შექმენით სია [0, 5, 0, 3, 0, 7, 8], ამ სიიდან წავშალოთ ყველა 0 რიცხვი

list =  [0, 5, 0, 3, 0, 7, 8]

for i in list:
     if i == 0:
         list.remove(i)
print(list)
