"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1)>= len(line2):
        len_min = len(line2)
    else:
        len_min = len(line1)
        
    for ind in range(0, len_min + 1):
        if line1[:ind + 1] == line2[:ind + 1]:
            continue
        else:
            return ind

    return IDENTICAL

##lin1 = "abcd"
##lin2 = "abcd"

##print(singleline_diff(lin1, lin2))

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    
    if "\n" in line1 or "\r" in line1 or "\n" in line2 or "\r" in line2:
        return ""
    if idx > len(line1) or idx > len(line2) or idx < 0:
        return ""

    return str(line1 + "\n{}\n" + line2 + "\n").format("="*idx + "^")


LIN1 = "abcd"
LIN2 = "abcd"
index = singleline_diff(LIN1, LIN2)

print(singleline_diff_format(LIN1, LIN2, index))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    equal_lines = False
    
    if len(lines1)==len(lines2):
        len_min = len(lines1)
        equal_lines = True
    elif len(lines1) > len(lines2):
        len_min = len(lines2)
    else:
        len_min = len(lines1)
        
    for ind in range(0, len_min):  #check each line
        diff_index = singleline_diff(lines1[ind], lines2[ind])
        if diff_index == IDENTICAL:
            continue
        else:
            return ind, diff_index 
    if equal_lines is True:
        return (IDENTICAL, IDENTICAL)
    else:
        return (len_min, 0)
    

LISTS1 = ['here and now', 'now and then', 'up or down']
LISTS2 = ['here and now', 'now and then', 'up or down']

##print(multiline_diff(LISTS1, LISTS2))

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile = open(filename, "rt")
    lines =[]
    
    for line in openfile.readlines():
        lines.append(line.strip())
##        print(lines)
    openfile.close()
    return lines
    

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    line_list1 = get_file_lines(filename1)
    line_list2 = get_file_lines(filename2)
    print(line_list1)
    print(line_list2)
    (error_line, error_idx) = multiline_diff(line_list1, line_list2)
    print(error_line, error_idx)
    if error_line == -1 and error_idx == -1:
        return "No differences\n"
    elif error_line != 0:
        return "Line {}\n".format(error_line) + \
               singleline_diff_format\
               (line_list1[error_line], line_list2[error_line], error_idx)
    elif error_line == 0 and line_list1 == []:
        return "Line {}\n".format(error_line) + \
               singleline_diff_format\
               ("", line_list2[error_line], error_idx)
    elif error_line == 0 and line_list2 == []:
        return "Line {}\n".format(error_line) + \
               singleline_diff_format\
               (line_list1[error_line], "", error_idx)
    else:
        return "Line {}\n".format(error_line) + \
               singleline_diff_format\
               (line_list1[error_line], line_list2[error_line], error_idx)
    
##filename = "file10.txt"
file1 = "file1.txt" #input("Enter filename1: ")
file2 = "file8.txt" #input("Enter filename2: ")

print(file_diff_format(file1, file2))
