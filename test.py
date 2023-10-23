import re

# Define the regular expression pattern
template = r"(\d{1,2})([./])(\d{1,2})\2(\d{4})"
# Read input from the user
string = input()
# Attempt to find the pattern
match = re.search(template, string)
a, b, c = string.split()
# Check if a match was found
if len(a) <= 2 and len(b) <= 2 and len(c) == 4:
    if match is not None:
        # Print the year (group 4)
        print(match.group(4))
else:
    print("None")
