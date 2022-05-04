#Expected output
'''
sum_fibs(1) should return a number.

sum_fibs(1000) should return 1785.

sum_fibs(4000000) should return 4613732.

sum_fibs(4) should return 5.

sum_fibs(75024) should return 60696.

sum_fibs(75025) should return 135721.


'''

def sum_fibs(num):
    '''
    sum fibonacci numbers
    '''
    prev_num = 1
    curr_num = 1
    next_num = prev_num + curr_num
    sum = 0
    sum += prev_num+curr_num

    while next_num <= num:
        prev_num = curr_num
        curr_num = next_num
        next_num = prev_num + curr_num
        if curr_num % 2 != 0:
            sum += curr_num
    return sum


print(sum_fibs(1))
