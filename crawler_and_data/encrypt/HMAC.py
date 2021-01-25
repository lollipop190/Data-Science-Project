import hmac
import hashlib
# 第一个参数是密钥key，第二个参数是待加密的字符串，第三个参数是hash函数
mac = hmac.new('key','hello',hashlib.md5)
mac.digest()  # 字符串的ascii格式
mac.hexdigest()  # 加密后字符串的十六进制格式