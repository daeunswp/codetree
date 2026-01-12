word = input()

new_word = word[0]+'a'+word[2:len(word)-2]+'a'+word[len(word)-1:len(word)]

print(new_word)