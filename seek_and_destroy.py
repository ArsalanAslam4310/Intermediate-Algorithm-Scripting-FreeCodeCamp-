#Expected output
'''
destroyer([1, 2, 3, 1, 2, 3], 2, 3) should return [1, 1].

destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3) should return [1, 5, 1].

destroyer([3, 5, 1, 2, 2], 2, 3, 5) should return [1].

destroyer([2, 3, 2, 3], 2, 3) should return [].

destroyer(["tree", "hamburger", 53], "tree", 53) should return ["hamburger"].

destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"], "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan") should return [12,92,65].

1
'''


from unsorted_search import linear_search

def destroyer(arr, *nums):
    new = []

    for num in nums:
        while linear_search(arr, num):
            arr.remove(num)

    new.append(arr)
    return new


print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
