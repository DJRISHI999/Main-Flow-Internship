a = input("Enter the string: ")

# Length of the string
print("Length of the string: ", len(a))

# Concatenation
b = input("Enter the second string: ")
print("Concatenation: ", a+b)

# Replication
print("Replication: ", a*3)

# Slicing
print("Slicing: ", a[2:5])

# Membership
print("Membership: ", 'W' in a)

# Iteration
print("Iteration: ")
for i in a:
    print(i)

# String formatting
print("String formatting: ")
print("Hello %s" %a) # %s is used for string 
print("Hello %s, your age is %d" %(a, 20)) # %d is used for integer
print("Hello %s, your age is %f" %(a, 20.5)) # %f is used for float
print("Hello %s, your age is %e" %(a, 20.5)) # %e is used for exponential
print("Hello %s, your age is %o" %(a, 20)) # %o is used for octal
print("Hello %s, your age is %x" %(a, 20)) # %x is used for hexadecimal
print("Hello %s, your age is %X" %(a, 20)) # %X is used for hexadecimal
print("Hello %s, your age is %c" %(a, 65)) # %c is used for character
print("Hello %s, your age is %r" %(a, 20.5)) # %r is used for raw string

# Capitalize
print("Capitalize: ", a.capitalize())

# Lower
print("Lower: ", a.lower())

# Upper
print("Upper: ", a.upper())

# Swapcase
print("Swapcase: ", a.swapcase()) # Converts lower case to upper case and vice versa

# Title
print("Title: ", a.title()) # Converts the first letter of each word to upper case

# Center
print("Center: ", a.center(20, '*'))

# Count
print("Count: ", a.count('l'))

# Find
print("Find: ", a.find('o'))

# Replace
print("Replace: ", a.replace('World', 'Python'))

# Split
print("Split: ", a.split())

# Strip
print("Strip: ", a.strip())
print("Strip: ", a.strip('H'))

#rstrip
print("Rstrip: ", a.rstrip())
print("Rstrip: ", a.rstrip('d'))

#lstrip
print("Lstrip: ", a.lstrip())
print("Lstrip: ", a.lstrip('H'))

# Zfill
print("Zfill: ", a.zfill(20)) # Adds zeros at the beginning of the string
# Isalnum
print("Isalnum: ", a.isalnum())

# Isalpha
print("Isalpha: ", a.isalpha())

# Isdigit
print("Isdigit: ", a.isdigit())

# Islower
print("Islower: ", a.islower())

# Isupper
print("Isupper: ", a.isupper())

# Isspace
print("Isspace: ", a.isspace())

# Istitle
print("Istitle: ", a.istitle())

# Isnumeric
print("Isnumeric: ", a.isnumeric())

# Isprintable
print("Isprintable: ", a.isprintable())

# Isidentifier
print("Isidentifier: ", a.isidentifier())

# Endswith
print("Endswith: ", a.endswith('d'))

# Startswith
print("Startswith: ", a.startswith('H'))

# Partition
print("Partition: ", a.partition(' ')) # Splits the string into three parts
print("Partition: ", a.partition('o'))




