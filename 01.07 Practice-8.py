def make_int(int_string):
    """
    Given the string int_string, return the associated integer if all 
    digits are decimal digits.  Other return -1.
    """
    
    # enter code here
    if int_string.isdigit():
        
        return int_string
    else:
        return -1
    
# Tests

print(make_int("123"))
print(make_int("00123"))
print(make_int("1.23"))
print(make_int("-123"))
