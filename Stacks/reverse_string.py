def reverse_string(my_string):
    
    mylist =[]
    for c in my_string:
        mylist.append(c)
        
    new_string = ""

    for i in range(len(my_string) -1, -1, -1):
        new_string  += mylist[i]
    return new_string


my_string = 'hello'

print(reverse_string(my_string))