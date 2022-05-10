'''
FreeCodeCamp -> JavaScript Algorithms and Data Structures -> Intermediate Algorithm Scripting
    Problem:
        Steamroller
    Explanation:
        Flatten a nested array. You must account for varying levels of nesting.
        Inputs and expected outputs:
        steamroll_array([[["a"]], [["b"]]]) should return ["a", "b"].
        steamroll_array([1, [2], [3, [[4]]]]) should return [1, 2, 3, 4].
        steamroll_array([1, [], [3, [[4]]]]) should return [1, 3, 4].
        steamroll_array([1, {}, [3, [[4]]]]) should return [1, {}, 3, 4].
'''


def steamroll_array(arr: list) -> list:
    '''
    This function flattewns an array

    @param arr: an array with subarrays
    @return: a flattened array

    '''
    for item in arr:
        if type(item).__name__ == 'list':
            steamroll_array(item)
        else:
            new_arr.append(item)
    return new_arr


array = [1, {}, [3, [[4]]]]
new_arr = []
print(steamroll_array(array))
