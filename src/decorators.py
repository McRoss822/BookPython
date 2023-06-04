
from datetime import date
import re


def method_log(method):
    def wrapper(*args, **kwargs):
        day = date.today()
        print(f"Method called:{day.ctime()}")
        result = method(*args, **kwargs)
        return result
    return wrapper


def convention_check(func):
    def wrapper(*args, **kwargs):
        name = func.name
        if re.search("[a-z]+_[a-z]+", name):
            return func(*args, **kwargs)
        print("Function is not snake-case ", func.name)
    return wrapper
