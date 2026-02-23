n=153

nod = len(str(n))
num=n 
total=0
while num>0:
    ld = num % 10
    total = total + (ld**nod)
    num = num//10

print(total)

if(total == n):
    print("Armstrong")
else:
    print("Not armstrong")
