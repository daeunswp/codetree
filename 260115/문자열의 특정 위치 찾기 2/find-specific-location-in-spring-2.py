alphabet = input()

word_list = ["apple", "banana", "grape", "blueberry", "orange"]

total = 0

for word in word_list:
    if(word[2]==alphabet or word[3]==alphabet):
        print(word)
        total+=1

print(total)