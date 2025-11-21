data_map = [None] * 7
def hash(key):
    my_hash = 0
    for letter in key:
        print(letter)
        my_hash = ((my_hash + (ord(letter) * 23)) % len(data_map))
        print(my_hash)
    return my_hash

call_hash=hash("cat")
print(call_hash)
