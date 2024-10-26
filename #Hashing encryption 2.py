#Hashing encryption
#encryption method in cryptography
def hashing():

 import hashlib
 e = hashlib.new("SHA256")
 thecorrect_password="mb1452345"
 e.update(thecorrect_password.encode())
 password_hash=e.hexdigest()
 print(password_hash)
 userpass=input("enter you password\n")
 e = hashlib.new("SHA256")
 e.update(userpass.encode())
 input_hash=e.hexdigest()
 print(input_hash == password_hash)

hashing()