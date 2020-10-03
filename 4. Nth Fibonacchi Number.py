'''
Given a number N findout the Nth fibonacci number

Actually best method is to use the adding of elements in the array itself.

'''

a = [0,1]
n = 10

for i in range(2,n):
    a.append(a[i-1]+a[i-2])

print(a[-1]) # Nth fibonacci number 
print(a)     # Fibonacci Series