#!/usr/bin/python3

if _name_ == "_main_":
"""Print the number of and list of arguments"""
imports sys

count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))
for i in range(count):
     print("{}: {}".format(i + 1, sys.argv[i + 1]))
