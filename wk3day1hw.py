
# Regex project
# Use python to read the file regex_test.txt and 
# print the last name on each line using regular 
# expressions and groups (return None for names with 
# no first and last name, or names that aren't 
# properly capitalized)


import re
with open('regex_test.txt') as file_:
    data=file_.readlines()

for person in data: 
    test = re.match('([A-Z][a-z]+)([\w\W]*)([A-Z][a-z]+)',person)
    if test:
        print(f'{test.groups()[0]}{test.groups()[1]}{test.groups()[2]}')
    else:
        print("None")







