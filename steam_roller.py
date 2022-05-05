def stream_roller(arr):
    new=[]
    for i in range(len(arr)):
        print(arr[i])
        if type(arr[1])._name_ == 'list':
            print(arr[1])
            for  j in range(len(arr)):
                if type(arr[j])._name_ != 'list':
                    new.append(arr[j])

                else:
                    stream_roller(arr[j])
    return new



arr = [1, [2], [3, [[4]]]]
print(stream_roller(arr))
