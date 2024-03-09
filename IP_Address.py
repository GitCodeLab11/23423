import re

# IP Addresses

s = "129.18.21.213"

result = re.search('\d+.\d+\.\d+\.\d+', s)

print(result.group())

# Email Addresses

s = "test123@gmail.com"

result = re.search('\w+\@\w+\.\w+', s)

print(result.group())

# Physical US addresses

s = "495 Grove Street Apartment #20 New York, NY 10014 USA"

result = re.search('\d+\s\w+\s\w+\s\w+\s\#\d+\s\w+\s\w+\,\s\w+\s\d+\s\w+', s)

print(result.group())

# Password Policy

'''

The text must be 8-12 characters long 
                                                                    
import re

test = input('Password? ')

if 8 <= len(test) <=12:
    print('Success')
else:
    print('Failure')

It must include at least lowercase character [A-Z] #adddd

It must included at least one digit [0-9]

It must include at least one Uppercase Character

It must contain at least one special character

'''

import re
password = raw_input("Enter string to test: ")
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,12}', password):
    print('success')
else:
    print('failure')
