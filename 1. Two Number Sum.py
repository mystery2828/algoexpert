'''
Given a List or an Array with unique elements return the pair whose sum is equal to 'k'.

'''

a = [3,5,-4,8,11,1,-1,6]
k = 10
h = {}

def check(a,k,h):
    for ele in a:
        h[ele] = 1

    for ele in a:
        h[ele] = 0
        if k-ele in h and h[k-ele]==1:
            return[ele,k-ele]

print(check(a,k,h))