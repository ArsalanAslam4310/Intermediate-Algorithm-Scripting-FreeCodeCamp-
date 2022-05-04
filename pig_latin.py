#Expected output
'''
translate_pig_latin("california") should return the string aliforniacay.

translate_pig_latin("paragraphs") should return the string aragraphspay.

translate_pig_patin("glove") should return the string oveglay.

translate_pig_latin("algorithm") should return the string algorithmway.

translate_pig_latin("eight") should return the string eightway.

Should handle words without vowels. translatePigLatin("rhythm") should return the string rhythmay.


'''


def is_vowel(char):
    '''
    check spinal case
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(char) > 1:
        print("Invalid input!")
        return None
    if char in vowels:
        return True
    return False


def translate_pig_latin(string):

    if is_vowel(string[0]):
        string += "way"
    else:
        fragment = ''
        for char in string:
            if not is_vowel(char):
                fragment += char
            else:
                break

        string = string.replace(fragment, '')
        string += fragment + "ay"

    return string


string = "schwartz"
print(translate_pig_latin(string))
