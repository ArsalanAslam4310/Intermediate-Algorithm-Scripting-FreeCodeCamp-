#Expected output
'''
smallest_commons([1, 5]) should return a number.

smallest_commons([1, 5]) should return 60.

smallest_commons([5, 1]) should return 60.

smallest_commons([2, 10]) should return 2520.

smallest_commons([1, 13]) should return 360360.

smallest_commons([23, 18]) should return 6056820.


'''


def smallest_commons(arr: list[int]) -> int:
    '''
    check smallest common multiple
    '''
    flag = False
    start = arr[0]
    end = arr[1]
    num = end
    if arr[0] > arr[1]:
        start = arr[1]
        end = arr[0]
        num = end

    while True:
        for i in range(start, end+1):
            if num % i != 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            break
        num += 1
    return num


print(smallest_commons([18, 23]))
