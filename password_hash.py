from werkzeug.security import gennerate_password_hash,check_password_hash
hash= gennerate_password_hash('123456')
print(hash)
print(check_password_hash(hash,'123456'))
print(check_password_hash(hash,'654321'))