#Hashing encryption
#encryption method in cryptography

import hashlib
e = hashlib.new("SHA256")
thecorrect_password="mb1452345"
e.update(thecorrect_password.encode())
password_hash=e.hexdigest()
print(password_hash)
userinput ="mb1452345"
e = hashlib.new("SHA256")
e.update(userinput.encode())
input_hash=e.hexdigest()
print(input_hash == password_hash)


