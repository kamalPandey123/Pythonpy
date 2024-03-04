def swap(stri,length):
    str_list =list( stri)
    i=0
    temp =" "
    while i < length//2:
        temp = str_list[i]
        str_list[i] = str_list[length-1 - i]
        str_list[length-1 - i] = temp
        i += 1 
    return ''.join(str_list)

stri = input("Enter string:")
length = len(stri)
stri = swap(stri,length)
print(stri)






