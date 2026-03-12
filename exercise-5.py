# ============================================================================
# TODO: Use a For Loop with a Range 

#Create a function called repeat. 
# It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# ============================================================================

def repeat(string, count):
    res=""
    for i in range(count):
        res += string + " "
    return res
print(repeat("hello", 10000))