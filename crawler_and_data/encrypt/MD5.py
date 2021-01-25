import hashlib
m = hashlib.md5()
m.update(str.encode("utf8"))
print(m.hexdigest())