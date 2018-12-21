PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"

def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated; preserves indent to print if present
    """
    orig_list = line.lstrip().split(" ")
    print(orig_list)
    if PRINT in orig_list:
        orig_list.remove(PRINT)
        while "" == orig_list[0]:
            orig_list.pop(0)
        while orig_list[-1] == "":
            orig_list.pop()
        return "{}print({})".format(" "*line.find(PRINT), " ".join(orig_list))

    else:
        return line
                
##    return ""

# Some simple tests
##print(update_line(""))
##print(update_line("foobar()"))  
##print(update_line("print 1 + 1"))
print(update_line("print numbers  "))
##print(update_line("    print    2,  3,  4   "))
##print(update_line("print   'a    bc d'.split('b')   "))

# Expect output
##
##foobar()
##print(1 + 1)
##XY = print(2,  3,  4)
##print(numbers)
##    print(2,  3,  4)
##print('a    bc d'.split('b'))