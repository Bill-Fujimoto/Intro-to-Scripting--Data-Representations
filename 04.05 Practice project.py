"""
Week 4 practice project template for Python Data Representation
Update syntax for print in CodeSkulptor Docs
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""
import os

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"


def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated; preserves indent to print if present
    """
    orig_list = line.lstrip().split(" ")
##    print(orig_list)
    if PRINT in orig_list:
        orig_list.remove(PRINT)
        while "" == orig_list[0]:
            orig_list.pop(0)
        while orig_list[-1] == "":
            orig_list.pop()
        return "{}print({})".format(" "*line.find("p"), " ".join(orig_list))

    else:
        return line
                
##    return ""

# Some simple tests
##print(update_line(""))
##print(update_line("foobar()"))  
##print(update_line("print 1 + 1"))      
##print(update_line("    print    2,  3,  4  "))
##print(update_line("print   'a    bc d'.split('b')"))



# Expect output
##
##foobar()
##print(1 + 1)
##    print(2,  3,  4)
##print('a    bc d'.split('b'))

def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.  
    Returns string corresponding to updated <pre> block with each line
    updated via update_line()
    """
    lines = pre_block.split("\n")
##    print(lines)
    updated_block = []
    
    for item in lines:
        updated_block.append(update_line(item))
##    print(updated_block)   
    return "\n".join(updated_block)

# Some simple tests
##print(update_pre_block(""))
##print(update_pre_block("foobar()"))
##print(update_pre_block("if foo():\n    bar()"))
##print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
##print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))
##print(update_pre_block("print 0xFFFF, xyz\n  print 123"))
##
### Expected output
####
####foobar()
####if foo():
####    bar()
####print()
####print(1+1)
####print(2, 3, 4)
####    print(a + b)
####    print(23 * 34)
####        print(1234)
##

def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Proces the <pre> blocks in the loaded text to update print syntax)
    Write the update text to the file specified by the string output_file_name
    """
    
    # open file and read text in file as a string
    openfile = open(input_file_name, "rt")
    
    outputfile = open(output_file_name, "at")
    
    for line in openfile.readlines():
        if PRINT not in line:
            outputfile.writelines(line)
        else:
            p_func = line.split(PREFIX)
##            print(p_func)
##            print()
            for ind in range(0, len(p_func)):
                if PRINT in p_func[ind]:
##                    print(p_func[ind])
                    p_list = p_func[ind].split(POSTFIX)
                    p_list[0] = update_pre_block(p_list[0])
                    p_func[ind]= POSTFIX.join(p_list)
##                    print(p_func[ind])
                else:
                    continue
##            print(p_func)
##            print()
            updated_line = PREFIX.join(p_func)
##            print(updated)
            outputfile.writelines(updated_line)
            
    openfile.close()   
    outputfile.close()
    
    # split text in <pre> blocks and update using update_pre_block()

    # Write the answer in the specified output file
    

# A couple of test files
update_file("table.html", "table_updated.html")
update_file("docs.html", "docs_updated.html")

### Import some code to check whether the computed files are correct
import examples3_file_diff as file_diff
file_diff.compare_files("table_updated.html", "table_updated_solution.html")
file_diff.compare_files("docs_updated.html", "docs_updated_solution_edits.html")

# Expected output
##table_updated.html and table_updated_solution.html are the same
##docs_updated.html and docs_updated_solution.html are the same
