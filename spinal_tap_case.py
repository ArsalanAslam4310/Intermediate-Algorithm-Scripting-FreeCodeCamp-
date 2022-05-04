#Expected output
'''
spinal_case("This Is Spinal Tap") should return the string this-is-spinal-tap.

spinal_case("thisIsSpinalTap") should return the string this-is-spinal-tap.

spinal_case("The_Andy_Griffith_Show") should return the string the-andy-griffith-show.

spinal_case("Teletubbies say Eh-oh") should return the string teletubbies-say-eh-oh.

spinal_case("AllThe-small Things") should return the string all-the-small-things.


'''

def spinal_case(string):
    '''
    convert to spinal casea
    '''
    beginning = 0
    lis = []
    for i in range(len(string)-1):
        if string[i] == " " or string[i] == "_":
            return string.replace(string[i], '-').lower()
        elif string[i].isupper() and i != 0:
            lis.append(string[beginning:i])
            beginning = i
    if lis:
        return '-'.join(lis).lower()

    


string = "thisIsSpinalTap"
print(spinal_case(string))
