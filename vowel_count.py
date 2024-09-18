def counting(text):
    vowels="aeiouAEIOU"
    count=0
    for i in text:
        if i in vowels:
            count+=1
    return count
text=input("Enter the text, whatever you want:")
print("{}{}{}{}".format('Total number of vowels in ',text,' = ',counting(text)))
