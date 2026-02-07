# შექმენით ფუნცქცია სახელად sum_numbers რომელიც პარამეტრად მიიღებს რიცხვების სიას [10, 20,30, 100, 200, 500 ] დაწერე ფუნქცია რომელიც დააბრუნებს მოცემული რიცხვების ჯამს
def sum_numbers(numbers):
    return sum(numbers)
nums = [10, 20, 30, 100, 200, 500]
result = sum_numbers(nums)
print(result)