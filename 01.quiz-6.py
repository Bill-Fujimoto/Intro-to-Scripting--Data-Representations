def count_vowels(word):
    vcount =0
    vowels = ['a','e','i','o','u']
    for char in vowels:
        vcount = vcount + word.count(char)
    return vcount
        
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
