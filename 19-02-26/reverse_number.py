def pal(num):
    result = 0
    while num>0:
        last_digit = num % 10
        result = (result * 10) + last_digit
        num = num//10
    
    return result
n=57175
num = n
res = pal(num)

if(res == n):
    print("Palindrome")
else:
    print("Not palindrome")