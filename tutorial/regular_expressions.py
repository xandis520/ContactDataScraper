import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
694 909 897
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson                           
Mr. T
'''

# pattern = re.compile(r'coreyms\.com')
pattern = re.compile(r'\d{3}[-\s\*\.]?\d{3}[-\s\*\.]\d{3}$')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match.group())

