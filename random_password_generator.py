import random
pass_length = int(input("Please,Enter the length of password : ")) # give length of password
keys = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password =  "".join(random.sample(keys,pass_length))
print(password)