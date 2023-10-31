import re
string = input()
print("True") if re.match("@?=ucsc.cl", string) else print("False")
