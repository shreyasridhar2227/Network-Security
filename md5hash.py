import hashlib
tt=input("Enter Input:")
r = hashlib.md5(tt.encode())
print("This is md5 Hash :",r.hexdigest())