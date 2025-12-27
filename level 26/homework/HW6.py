# მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი და უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში, უარყოფითი რიცხვები კი პირიქით
list1 = []
list2 = []

while True:
     nums = int(input("Enter random number:"))
     if nums > 0 :
         list1.append(nums)
     else:
         list2.append(nums)
     print(list1,list2)