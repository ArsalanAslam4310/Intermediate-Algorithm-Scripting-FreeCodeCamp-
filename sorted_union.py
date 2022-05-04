#Expected output
'''
unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]) should return [1, 3, 2, 5, 4].

unite_unique([1, 2, 3], [5, 2, 1]) should return [1, 2, 3, 5].

unite_unique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]) should return [1, 2, 3, 5, 4, 6, 7, 8].

unite_unique([1, 3, 2], [5, 4], [5, 6]) should return [1, 3, 2, 5, 4, 6].

unite_unique([1, 3, 2, 3], [5, 2, 1, 4], [2, 1]) should return [1, 3, 2, 5, 4].


'''

def unite_unique(*lists):
    '''
    Find unique value in list
    '''
    new = []
    for lis in lists:
        for num in lis:
            if num not in new:
                new.append(num)

    return new


print(unite_unique([1, 3, 2, 3], [5, 2, 1, 4], [2, 1]))
