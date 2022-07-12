
def has_no_e(string):
    #has_no_e Returns True if the given word doesn’t have the letter “e” in it.
    for char in string:
        if char in 'Ee':
            return True
    return False

print(has_no_e('oo'))