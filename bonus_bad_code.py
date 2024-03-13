feet_inches = input('Enter feet and inches: ')

def convert(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return f'{feet} feet and {inches} inches is equal to {meters} meters.'


print(convert(feet_inches))