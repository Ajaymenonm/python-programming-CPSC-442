def permutation(string):
    res = set([string]) # create list
    print(res)
    if len(string) == 2: # check string length
        res.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            for s in permutation(string[:i] + string[i + 1:]):
                res.add(c + s) # add the permutation to the list

    return list(res)
   


input_string = input("Enter the string : ") # take the input string

print(permutation(input_string)) # call method with giving argument