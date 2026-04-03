# Word Frequency Counter
# - User pastes any text
# - Count how many times each word appears
# - Show top 5 most common words
# Uses: dictionaries, strings, loops, sorting

common = {}
text = input("Enter your text :")
words = text.split()
for i in words:
    if i in common:
        common[i]+=1
    else:
        common[i]=1
sorted_common = sorted(common.items(),key=lambda x: x[1],reverse=True)
print("Top 5 most common words are :")
for word, count in sorted_common[:5]:
    print(word, ":", count)