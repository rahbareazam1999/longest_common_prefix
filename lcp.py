def longest_commom_prefix(strs):
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)

    for i in range(min_len):
        char=strs[0][i]

        if all(s[i] == char for s in strs):
            continue
        else:
            return strs[0][:i]
        
    return strs[0][:min_len]

input=input("Enter a list of strings (comma-seperated): ").split(',')

input=[s.strip() for s in input]

result= longest_commom_prefix(input)
print("lcp: ",result)