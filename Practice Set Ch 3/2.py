
# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

from datetime import date
Name = input("Enter Your Name\n")
Date = str(date.today())
letter = f'''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>",Name).replace("<|Date|>",Date))