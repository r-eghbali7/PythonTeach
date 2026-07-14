import random
import string

tadad = int(input("tol ramz:"))
x = []
password = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.octdigits + string.digits
password = "".join(random.sample(password,tadad))
print(password)
