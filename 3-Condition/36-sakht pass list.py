tadad_caracter = int(input("tadad_caracter:"))
import random
import string
ramz_tolede = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + str(random.randint(0,9)) + string.punctuation
password = "".join(random.sample(ramz_tolede,tadad_caracter))

print("password:",password)