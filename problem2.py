def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return reverse_word_list

print(master_yoda('I am home'))

print(master_yoda('we are ready'))

mylist = ['a','b', 'c']
m = 'ooo '.join(mylist)
print(m)