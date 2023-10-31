import re


def validate_date(date):
    
    pattern = re.compile("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(1[0-9]{3}|2[0-9]{3})$")
    if pattern.match(date):
        return True
    else:
        return False


date = input()

print(validate_date(date))
