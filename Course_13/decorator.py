from functools import wraps
from time import time
def time_it(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        s = time()
        f(*args, **kwargs) #Wrapper-ul inlocuieste codul din cf(v) si de aia se apeleaza functia f aici
        e = time()

        print(f'{f.__name__} took {e-s} seconds to execute...')
    return wrapper


@time_it
def cf(v):
    for i in range(v):
        j = 10

cf(1000000)