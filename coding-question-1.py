def hash_algorithm(s):
    current_value = 0
    for char in s:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

# Initialization sequence
init_sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

# Splitting the sequence by commas and ignoring newlines
steps = init_sequence.split(',')

# Calculate HASH algorithm result for each step and sum them
total_sum = sum(hash_algorithm(step.replace('\n', '')) for step in steps)

print("Sum of the results:", total_sum)

'''
Given the initialization sequence:

rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

We'll apply the HASH algorithm to each step:

rn=1 becomes 30.
cm- becomes 253.
qp=3 becomes 97.
cm=2 becomes 47.
qp- becomes 14.
pc=4 becomes 180.
ot=9 becomes 9.
ab=5 becomes 197.
pc- becomes 48.
pc=6 becomes 214.
ot=7 becomes 231.
Now, let's sum these results:

30 + 253 + 97 + 47 + 14 + 180 + 9 + 197 + 48 + 214 + 231 = 1320

Therefore, the sum of the results after running the HASH algorithm on each step in the initialization sequence is 1220.
'''
