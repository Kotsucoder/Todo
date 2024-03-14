from parsers import parse
from converters import convert

feet_inches = input('Enter feet and inches: ')


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use the slide.')