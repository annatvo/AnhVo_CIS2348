#Anh Vo
#2037824
#Assignment 6.17

# User enter password
password = input("")

# Replace characters
password = password.replace('i', '!')
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('o', '.')

# Append "q*s" to the password
password += 'q*s'

# Print the modified password
print(password)
