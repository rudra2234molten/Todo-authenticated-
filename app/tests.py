import hashlib

print((hashlib.shake_128('1'.encode()).hexdigest(100)))