def repeatedString(s, n):
    num_repeated_s = int(n/len(s))
    a_in_s = 0
    num_As = 0
    for idx, char in enumerate(s):
        if(char == "a"):
            a_in_s += 1

        if(idx < (n % len(s))):
            if(char == "a"):
                num_As += 1

    num_As += num_repeated_s * a_in_s
    
    return num_As

if __name__ == "__main__":
    sample_string = 'alkklsa'
    n_repeats = 120
    print(repeatedString(sample_string,n_repeats))
