import re

string = input()
dates = re.compile("([1-9]|[12][0-9]|3[01])(/)([1-9]|1[012])(/)(19|20)\d\d")
result = dates.match(string)
print(result)
