'''
Given a sequence which may contain a sequence inside return the product sum of the total sequence, multiply the sum with the depth to which it is nested
Ex : [5, 2, [7, -1], 3, [6, [-13, 8], 4]]   ==> 12

'''
def productSum(arr, multiplier = 1):
    sums = 0
    for ele in arr:
        if type(ele) is list:
            sums += productSum(ele, multiplier+1)
        else:
            sums += ele
    return sums * multiplier

arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr))