
from datetime import date
from exceptions import OutOfBooksException
import re


def method_log(method):
    """
    decorator for logging function call history
    """
    def wrapper(*args, **kwargs):
        day = date.today()
        print(f"Method called:{day.ctime()}")
        result = method(*args, **kwargs)
        return result
    return wrapper


def convention_check(func):
    """
    decorator for checking if function name applyies to snake case
    """
    def wrapper(*args, **kwargs):
        name = func.__name__
        if re.search("[a-z]+_[a-z]+", name):
            result = func(*args, **kwargs)
            return result
        print("Function is not snake-case ", func.__name__)
    return wrapper

def exception_logger(method):
    def wrapper(*args, **kwargs):
        try:
            method(*args, **kwargs)
        except OutOfBooksException:
            print("Out of books")
