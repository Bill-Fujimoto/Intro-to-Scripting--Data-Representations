#~ Write a function demystify(l1_string) that takes a string composed of the characters "l" and "1" and returns the string formed by replacing each instance of "l" by "a" and each instance of "1" by "b".


def demystify(word):
    
    new_a = word.replace("l","a")
    new_1 = new_a.replace("1","b")
    return new_1    
        
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
