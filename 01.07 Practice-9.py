def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    space = name_string.find(" ")
    #~ print(pace))
    first = name_string[:space]
    last = name_string[space+1:]
    #~ print(first, last)
    return last.title() +" "+ first.title()
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))
