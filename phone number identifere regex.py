import re


def find_phone_numbers(string):
    pattern = r'^\+(\d{1})?[-. ]?(\d{3})[-. ]?(\d{3})[-. ]?(\d{2})[-. ]?(\d{2})'
    match = re.search(pattern, string)

    if match:
        full_number = string
        country_code = match.group(1) or "N/A"
        area_code = match.group(2)
        number = match.group(3) + "-" + match.group(4) + "-" + match.group(5)

        print(f"Full number: {full_number}")
        print(f"Country code: {country_code}")
        print(f"Area code: {area_code}")
        print(f"Number: {number}")
    else:
        print("No match")


string = input()
find_phone_numbers(string)
