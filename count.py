text=input("enter a sentence:")
words=text.split()
word_count={word:words.count(word)for word in words}
print("word occurence:")
for word,count in word_count.items():
    print(word,":",count)