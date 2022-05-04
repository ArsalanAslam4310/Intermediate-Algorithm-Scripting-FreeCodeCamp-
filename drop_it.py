#Expected output
'''
drop_elements([1, 2, 3, 4], function(n) {return n >= 3;}) should return [3, 4].

drop_elements([0, 1, 0, 1], function(n) {return n === 1;}) should return [1, 0, 1].

drop_elements([1, 2, 3], function(n) {return n > 0;}) should return [1, 2, 3].

drop_elements([1, 2, 3, 4], function(n) {return n > 5;}) should return [].

drop_elements([1, 2, 3, 7, 4], function(n) {return n > 3;}) should return [7, 4].

drop_elements([1, 2, 3, 9, 2], function(n) {return n > 2;}) should return [3, 9, 2].


'''

def drop_elements(lis, func):
    '''
    Drop number in list
    '''
    new = []
    for num in lis:
        if func(num):
            new.append(num)
    return new


lis = [1, 2, 3, 4, 5, 6, 1, 2]
lis = drop_elements(lis, lambda n: n >= 3)
print(lis)
