#Expected output
'''
fear_not_letter("abce") should return the string d.

fear_not_letter("abcdefghjklmno") should return the string i.

fear_not_letter("stvwx") should return the string u.

fear_not_letter("bcdf") should return the string e.

fear_not_letter("abcdefghijklmnopqrstuvwxyz") should return undefined.


'''


def fear_not_letter(string):
    '''
    find missing letter in string
    '''
    
    a_to_z="abcdefghijklmnopqrstuvwxyz"
    
    for char in a_to_z:
        if char not in string:
            return char
    return None

string_of_letters="abcdefghijklmnopqrstuvwxyz"
print(fear_not_letter(string_of_letters))
