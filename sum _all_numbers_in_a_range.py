#expected_output
'''
sum_all([1, 4]) should return a number.

sum_all([1, 4]) should return 10.

sum_all([4, 1]) should return 10.

sum_all([5, 10]) should return 45.

sum_all([10, 5]) should return 45.

'''


def sum_number(lis):
    '''sum of all number in list between two index
    '''
    sum =0
    for i in range(lis[0],lis[0]):
        sum = sum +i
        i = i +1
    return sum 

print(sum_number([5,10]))
