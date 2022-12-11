import random
import string

def get_random_password(n) -> str:

    m = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = "".join(random.sample(m, n))
    return password

print(get_random_password(8))