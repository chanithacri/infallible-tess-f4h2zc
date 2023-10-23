import re

# Define the regular expression pattern
template = r"(\d{1,2})([./])(\d{1,2})\2(\d{4})"
# Read input from the user
string = input()
# Attempt to find the pattern
match = re.match(template, string)

# Check if a valid date was found and the day and month are within appropriate ranges
if match and 1 <= int(match.group(1)) <= 31 and 1 <= int(match.group(3)) <= 12:
    # Check if there are additional characters after the year
    if match.end() == len(string):
        # Print the year (group 4)
        print(match.group(4))
    else:
        print("None")
else:
    print("None")
