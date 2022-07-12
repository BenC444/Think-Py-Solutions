'''has_no_e that returns True if the given word doesn’t have the letter “e” in
it'''



def has_e(string):
    ''''returns True is it has Ee and false if it doesn't'''
    for char in string:
        if char in 'Ee':
            return True
    else:
        return False
        
print(has_no_e('yes'))


def has_no_e(string):
    '''returns True if it has no e and false if it has an e'''
    if has_e(string)==True:
        return False 
    else:
        return True
