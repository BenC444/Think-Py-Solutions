# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:13:24 2021

@author: chapperz
"""
'''Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict'''

'''The setdefault() method returns the value of the item with the specified key.

If the key does not exist, insert the key, with the specified value


dictionary.setdefault(keyname, value)
'''

#setdefault either adds the key value pair you entered if the key is new or returns the value for the key is the 
#key is allready in the dicstionary

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = key
        else:
            inverse[val].append(key)
    return inverse

def Concise_invert_dict(d):
    #this takes a dictionary as an argument and returns a new local dictionary 'inverse' as an output
    inverse=dict()
    for key in d:
        val=d[key]
        inverse.setdefault(val,(key))
    return inverse
