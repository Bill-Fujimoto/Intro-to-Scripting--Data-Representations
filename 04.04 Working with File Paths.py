"""
Examples of paths used in Python
Expects current_file.txt in same directory as this code
Expects parent_file.txt in parent directory of this code
Expects child_file.txt in sub-directory child
"""
import os

if not os.path.exists("child"):
    os.makedirs("child")


def make_file(file_name, dir=os.getcwd()):
    """
    Create new file examples
    """
    my_file = open(dir +"\\" + file_name, 'wt')
    text = "This is the contents of "+ file_name
    my_file.write(text)
##    print(my_file_text)
    my_file.close()
    
make_file("current_file.txt")
make_file("child_file.txt", "child")
make_file("parent_file.txt", "..")  # ".." moves directory up one level

def echo_file(file_name):
    """
    Open a file, read its contents, and echo to console
    """
    my_file = open(file_name, 'r')
    my_file_text = my_file.read()
    print(my_file_text)
    my_file.close()                         # close the file, Joe!
    

def run_absolute_path_examples():
    """
    Some simple examples of absolute and relative paths
    """

    # Examples using absolute paths on Windows - Use raw strings to handle backslash
    current_abs_path = r"C:\Users\redex\OneDrive\Documents\Education\Introduction to Scripting in Python\Python Data Representations\current_file.txt"
    child_abs_path = r"C:\Users\redex\OneDrive\Documents\Education\Introduction to Scripting in Python\Python Data Representations\child\child_file.txt"
    parent_abs_path = r"C:\Users\redex\OneDrive\Documents\Education\Introduction to Scripting in Python\parent_file.txt"
    echo_file(current_abs_path)
    echo_file(child_abs_path)
    echo_file(parent_abs_path)
    print()

run_absolute_path_examples()

def run_relative_path_examples():
    """
    Some simple examples of relative paths
    """

    # Examples using relative paths - current_file.txt in same directory as this code
    echo_file("current_file.txt")
    echo_file("child/child_file.txt")  # Note that "/" slash works on Windows
    echo_file("../parent_file.txt")
    print()


run_relative_path_examples()


def run_os_path_examples():
    """
    Examples of computing/manipulating paths reliably using the os module
    """

    # Get absolute path using os.path - note path uses backslashes on Windows
    current_abs_path = os.path.abspath("current_file.txt")
    print(current_abs_path)

    # Get absolute path to child_file.text using os.path
    child_abs_path = os.path.abspath("child/child_file.txt")
    print(child_abs_path)

    # Get absolute path to parent_file.text using os.path
    parent_abs_path = os.path.abspath("../parent_file.txt")
    print(parent_abs_path)

    # Get current working directory
    working_dir = os.getcwd()
    print(working_dir)

    # Construct paths using os.path.join
    child_rel_path = os.path.join(working_dir, "child", "child_file.txt")
    print(child_rel_path)

##    parent_rel_path = os.path.join(working_dir, os.pardir, "parent_file.txt")
##    print(parent_rel_path)

run_os_path_examples()