def change_case(orig_string: str):
    result = ""
    for char in orig_string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    
    return result

def split_in_half(orig_string: str):
    p1 = orig_string[:len(orig_string)//2]
    p2 = orig_string[len(orig_string)//2:]

    return p1, p2


def remove_special_characters(orig_string: str):
    result = ""
    for char in orig_string:
        if char.isalpha() or char.isnumeric():
            result += char
        elif char.isspace():
            result += char
    
    return result


if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)
    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)