
'''
    FreeCodeCamp -> JavaScript Algorithms and Data Structures -> Intermediate Algorithm Scripting
    Problem:
        Trurh_checker
    Explanation:
        truthCheck([{name: "Quincy", role: "Founder", isBot: false}, {name: "Naomi", role: "", isBot: false}, {name: "Camperbot", role: "Bot", isBot: true}], "isBot") should return false.

truth_check([{name: "Quincy", role: "Founder", isBot: false}, {name: "Naomi", role: "", isBot: false}, {name: "Camperbot", role: "Bot", isBot: true}], "name") should return true.

truth_check([{name: "Quincy", role: "Founder", isBot: false}, {name: "Naomi", role: "", isBot: false}, {name: "Camperbot", role: "Bot", isBot: true}], "role") should return false.

truth_check([{name: "Pikachu", number: 25, caught: 3}, {name: "Togepi", number: 175, caught: 1}], "number") should return true.

truth_check([{name: "Pikachu", number: 25, caught: 3}, {name: "Togepi", number: 175, caught: 1}, {name: "MissingNo", number: NaN, caught: 0}], "caught") should return false.

truth_check([{name: "Pikachu", number: 25, caught: 3}, {name: "Togepi", number: 175, caught: 1}, {name: "MissingNo", number: NaN, caught: 0}], "number") should return false.

truth_check([{name: "Quincy", username: "QuincyLarson"}, {name: "Naomi", username: "nhcarrigan"}, {name: "Camperbot"}], "username") should return false.

truth_check([{name: "freeCodeCamp", users: [{name: "Quincy"}, {name: "Naomi"}]}, {name: "Code Radio", users: [{name: "Camperbot"}]}, {name: "", users: []}], "users") should return true.

truth_check([{id: 1, data: {url: "https://freecodecamp.org", name: "freeCodeCamp"}}, {id: 2, data: {url: "https://coderadio.freecodecamp.org/", name: "CodeRadio"}}, {id: null, data: {}}], "data") should return true.

truth_check([{id: 1, data: {url: "https://freecodecamp.org", name: "freeCodeCamp"}}, {id: 2, data: {url: "https://coderadio.freecodecamp.org/", name: "CodeRadio"}}, {id: null, data: {}}], "id") should return false.

'''

def truth_check(collection, pre):
    '''
    This function match every value in dictionaries
    @param arr:dictionaries in array
    @return  :Bool value 
    '''    
    for dic in collection:
        for value in dic.values():
            if value == pre:
                return True
                continue
            else:
                return False

print(truth_check([{'name': "Quincy", 'role': "Founder", 'isBot': 'false'}, {'name': "Naomi", 'role': "", 'isBot': 'false'}, {'name': "Camperbot", 'role': "Bot", 'isBot': 'true'}], "isBot"))
