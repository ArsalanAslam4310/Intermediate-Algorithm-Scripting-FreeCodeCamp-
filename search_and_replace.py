#Expected output
'''
my_replace("Let us go to the store", "store", "mall") should return the string Let us go to the mall.

my_replace("He is Sleeping on the couch", "Sleeping", "sitting") should return the string He is Sitting on the couch.

my_replace("I think we should look up there", "up", "Down") should return the string I think we should look down there.

my_replace("This has a spellngi error", "spellngi", "spelling") should return the string This has a spelling error.

my_replace("His name is Tom", "Tom", "john") should return the string His name is John.

my_replace("Let us get back to more Coding", "Coding", "algorithms") should return the string Let us get back to more Algorithms.


'''

def my_replace(string, before, after):
    '''
    search and replace the value
    '''
    after = list(after)
    if before[0].isupper():
        after[0] = after[0].upper()
    else:
        after[0] = after[0].lower()
    after = ''.join(after)

    return string.replace(before, after)


print(my_replace("Let us get back to more Coding", "Coding", "algorithms"))
