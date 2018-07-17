# -------------MD5加密---------------------------

import hashlib

a = 'a test string'

md5 = hashlib.md5()
md5.update(a.encode('utf-8'))
pwd = md5.hexdigest()
print(pwd)  # 32位


# —————————————SHA1加密—————————————————————————————————

import hashlib

a = 'a test string'

sha1 = hashlib.sha1()
sha1.update(a.encode('utf-8'))
pwd = sha1.hexdigest()
print(pwd)  # 40位
