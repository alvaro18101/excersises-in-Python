def anagram(string1,string2):
    string1 = string1.lower().replace('',' ').split()
    string2 = string2.lower().replace('',' ').split()
    string1.sort()
    string2.sort()
    return True if string1==string2 else False

print(anagram('Roma','mora'))