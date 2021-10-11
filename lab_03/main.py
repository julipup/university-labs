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
# - Using C-like formatting
#
print('Formatted integer numbers:')
for number in integer:
    print('Integer: ', '%5.0f' % number)

print('--------------------------')

#
# Formatting real numbers
# - Using old and new python
#   syntax.
# P.S. We'll use real_numbers array
# twice - to format numbers as numbers
# with floating point and to format
# them as numbers with fixed point
#
print('Formatted real numbers')

print('- Real numbers as numbers with floating point')
for number in real_numbers:
    print('Floating point: ', '{:10}'.format(number))

print('- Real numbers as numbers with fixed point')
for number in real_numbers:
    print('Fixed point: ', f'{number:5.2f}')

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
