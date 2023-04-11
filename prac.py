from hashlib import sha256

h= sha256()
h.update("hello".encode('utf-8'))

print(h)
