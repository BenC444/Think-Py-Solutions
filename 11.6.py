fin=open('/Users/44780/Desktop/git Think-Py-Solutions/words.txt')

ans={}
def keywords():
    '''this reads words in as keys in the dictionary ans'''
    for word in fin:
        ans[word]='a'
        
keywords()

