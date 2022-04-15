def total_chars(str):
    dic1={}
    for i in str:
        key=dic1.keys()
        if i in key:
            dic1[i]=dic1[i]+1
        else:
            dic1[i]=1
    return dic1

word=input("Enter a word-")
print(total_chars(word))
