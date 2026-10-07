def get_most_common_letter(text):
    counter = {} #init dict
    for char in text:#loops through each character in text
        #print(counter)
        if char != " ":#specifically dropping spaces rather than editing sort to access [1][0] instead of [0][0] to skip space in sorted letters
            counter[char] = counter.get(char, 0) + 1 #for each char, find char in dict, if not found get returns 0 due to default value and +1 means created key:value pair (unique due to dict) has val 1, if found value is increased by 1
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]#for each item in counter, using counter values as value to sort by ([1] accesses value of kvp which is now 2nd element in each tuple, where the dict has transformed into a list of tuples), sort descending (change #1, add reverse = True) and access key for letter via tuple indicies
    #print(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    #print(sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0])
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
