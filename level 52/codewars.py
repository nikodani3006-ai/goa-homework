# codewars 1 
# def solution(number):
#     if number < 0:
#         return 0
    
#     total = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
    
#     return total
# codewarsss 2
# def check_exam(arr1, arr2):
#     score = 0
#     for i in range(len(arr1)):
#         if arr2[i] == "":
#             score += 0
#         elif arr1[i] == arr2[i]:
#             score += 4
#         else:
#             score -= 1

#     if score < 0:
#         return 0
#     return score
# codewarssss3
# def high_and_low(numbers):
#     nlist = numbers.split()
#     new_min = int(nlist[0])
#     new_max = int(nlist[0])
#     for i in nlist:
#         if new_min > int(i):
#             new_min = int(i)
#         elif new_max < int(i):
#             new_max = int(i)
#     return str(new_max) + " " + str(new_min)

# codewarrs4
# def find_short(s):
#     words = s.split()
#     shortest = len(words[0])
    
#     for word in words:
#         if len(word) < shortest:
#             shortest = len(word)
    
#     return shortest