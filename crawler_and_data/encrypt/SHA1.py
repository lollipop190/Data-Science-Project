import hashlib
sha1 = hashlib.sha1()
data = '2333333'
sha1.update(data.encode('utf-8'))
sha1_data = sha1.hexdigest()
print(sha1_data)