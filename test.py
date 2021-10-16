from simplecrypt import encrypt, decrypt

passkey = "pickypickyfarm"
key = "hello"
cipher = encrypt(passkey, key)
print(cipher)

destr = decrypt(passkey, cipher)
print(destr)

