text ="I am learning python programing language in python lab"

#frequency of word

words =text.split()
count_word={}

for word in words:
    if word in count_word:
        count_word[word]+=1
    else:
        count_word[word] =1 

# frequency of char
ch_count={}
for ch in text:
    if ch!=" ":
        if ch in ch_count:
            ch_count[ch]+=1
        else:
            ch_count[ch]=1    


# main function 

print("word ferquency\n")
print(count_word)
print("char frequency\n")
print(ch_count)


