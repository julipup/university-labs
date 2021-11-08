# Task summary:
# - Integer numbers:
#   size: 4,
#   number width: 3
#
# - Real numbers
#   size: 2
#   (1*) number with floating point:
#        number width: 10
#   (2*) fixed number:
#        number width: 5
#        decimal width: 2
# - String
#   number of symbols in one line: 4
# - Boolean
#   boolean: True

# Initializing variables
integer = []
real_numbers = []
string = ''
boolean = True

# Prompting user to write integer numbers
for i in range(1, 5):
    integer.append(int(input('Integer #{}: '.format(i))))

# Prompting user to write real numbers
for i in range(1, 3):
    real_numbers.append(float(input('Real number #{}: '.format(i))))

# Prompting user to write random string
string = input('Write random string:')

print('--------------------------')

#
# Formatting integer numbers
#
print('Formatted integer numbers:')
for number in integer:
    # New Python formatting
    print(f'(New Python formatting) Integer: {number:3n}')

    # Old Python formatting
    print('(Old Python formatting) Integer: ', '{:3n}'.format(number))

    # C-like Python formatting
    print('(C-like Python formatting) Integer: ', '%3i' % number)

print('--------------------------')

#
# Formatting real numbers
# P.S. We'll use real_numbers array
# twice - to format numbers as numbers
# with floating point and to format
# them as numbers with fixed point
#
print('Formatted real numbers')

print('- Real numbers as numbers with floating point')
for number in real_numbers:
    # New Python formatting
    print(f'(New Python formatting) Floating point: {number:10}')

    # Old Python formatting
    print('(Old Python formatting) Floating point: ', '{0:10}'.format(number))

    # C-like Python formatting
    print('(C-like Python formatting) Floating point: ', '%10g' % number)

print('- Real numbers as numbers with fixed point')
for number in real_numbers:
    # New Python formatting
    print(f'(New Python formatting) Fixed point: {number:5.2f}')

    # Old Python formatting
    print('(Old Python formatting) Fixed point: ', '{a:5.2f}'.format(a=number))

    # C-like Python formatting
    print('(C-like Python formatting) Fixed point: ', '%5.2f' % number)

print('--------------------------')

#
# Formatting string
#
print('Formatted string (4 symbols in 1 line)')

for i in range(0, int(len(string)/4) + 1):
    print(string[i*4:(i*4 + 4)])

print('--------------------------')

#
# Formatting boolean
#
print('Formatted boolean (True):')
print(boolean)
print('--------------------------')
