#how to hide user input in python
from getpass import getpass
user = input ("username:")
password = getpass("password:")
print (user, password)
