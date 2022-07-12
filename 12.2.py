'''. Write a program that reads a word list from a file 
(see Section 9.1) and prints all the sets of
words that are anagrams'''

fin=open('/Users/44780/Desktop/git Think-Py-Solutions/words.txt')

#for line in fin:
    
'''yikes I lost q9 so I'm going to make a funtion to 

 build a dictionary that maps from a collection of letters to a list
of words that can be spelled with those letters. The question is, how can you represent the
collection of letters in a way that can be used as a key'''

'''you can't use lists as keys, but you can use tuples'''


letter_list=[]

for word in fin:
    letter_list.append(''.join(set(word.strip())))
letter_list.sort()
#adding all the possible letter combinations to a list (each letter once per element in list)

letter_list = list(dict.fromkeys(letter_list))
#removing dupilcates

letter_keys=tuple(letter_list)   
#making it a tuple so it can be a key

print(len(letter_list))

ans_dict={}

def find_combinations(letter_combination):
    


for letter_combination in letter_keys:
    ans_dict[letter_combination]= '''work out all the combinations of that combination that is in words'''